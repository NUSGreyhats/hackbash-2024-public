from flask import Flask, render_template, request

app = Flask(__name__)

CONFIG = {
    'SECRET': 'flag{th1s_w4s_m34nt_t0_b3_4_s3cr3t}',
    'APP_NAME': 'First Flask App'
}

@app.route('/')
def index():
    name = request.args.get('name', 'user')
    title = "<h1>Hi {name}!</h1>".format(name=name)
    message = "<p>Welcome to {CONFIG[APP_NAME]}!</p>"
    return (title + message).format(CONFIG=CONFIG)

if __name__ == '__main__':
    app.run()
