const express = require('express');
const crypto = require('crypto');
const cookieParser = require('cookie-parser')

const FLAG = process.env.FLAG || "flag{fake_flag}"
delete process.env.FLAG

const USERS = [
    {
        username: 'admin',
        password: crypto.randomBytes(16).toString('hex')
    }
]

const app = express()
app.use(express.static('static'))
app.use(express.json())
app.use(cookieParser())

app.get('/api/auth', (req, res) => {
    if (req.cookies.username) {
        res.status(200).json({ username: req.cookies.username })
    } else {
        res.status(403).json({ error: 'Unauthorized' })
    }
})

app.post('/api/register', (req, res) => {
    const username = req.body.username
    const password = req.body.password
    const user = USERS.find(u => u.username === username)
    if (user) {
        res.status(400).json({ error: 'Username already exists' })
        return
    }
    USERS.push({
        username,
        password
    })
    res.status(200).json({ username })
})

app.post('/api/login', (req, res) => {
    const username = req.body.username
    const password = req.body.password
    const user = USERS.find(u => u.username === username)
    if (!user || user.password !== password) {
        res.status(400).json({ error: 'Invalid username or password' })
        return
    }
    res.cookie('username', username, { httpOnly: true })
    res.status(200).json({ username })
})

app.get('/api/flag', (req, res) => {
    if (req.cookies.username === 'admin') {
        res.status(200).json({ flag: FLAG })
    } else {
        res.status(403).json({ error: 'Unauthorized' })
    }
})

app.listen(3000, () => {
    console.log('Server listening on port 3000')
})