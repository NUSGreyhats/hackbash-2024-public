import puppeteer from 'puppeteer'
import express from 'express'
import rateLimit from 'express-rate-limit'

const app = express()
app.use(express.static('static'))
app.use(express.json())

app.set('trust proxy', 1);

const port = 8000

let browser

async function visit(url) {
    const ctx = await browser.createIncognitoBrowserContext()
    const page = await ctx.newPage()

    try {
        await page.goto(url, { timeout: 10000, waitUntil: 'networkidle2' })
        await page.waitForTimeout(10000)
    } finally {
        await page.close()
        await ctx.close()
    }
}

app.use(
    '/visit',
    rateLimit({
        windowMs: 60 * 1000,
        max: 3,
        message: { error: 'Too many requests, try again later' }
    })
)

app.post('/visit', async (req, res) => {
    var url = req.body.url
    if (
        url === undefined ||
        (!url.startsWith('http://') && !url.startsWith('https://'))
    ) {
        return res.status(400).send({ error: 'Invalid URL' })
    }
	
	const urlObj = new URL(url)
    if (urlObj.hostname === 'challs.nusgreyhats.org') {
        urlObj.hostname = 'username-gen-easy-app'
        urlObj.port = '80'
        url = urlObj.toString()
    }

    try {
        console.log(`[*] Visiting ${url}`)
        await visit(url)
        console.log(`[*] Done visiting ${url}`)
        return res.sendStatus(200)
    } catch (e) {
        console.error(`[-] Error visiting ${url}: ${e.message}`)
        return res.status(400).send({ error: e.message })
    }
})

app.listen(port, async () => {
    browser = await puppeteer.launch({
        pipe: true,
        dumpio: true,
        args: [
            '--disable-dev-shm-usage', // Docker stuff
            '--js-flags=--jitless' // No Chrome n-days please
        ]
    })
    console.log(`[*] Listening on port ${port}`)
})
