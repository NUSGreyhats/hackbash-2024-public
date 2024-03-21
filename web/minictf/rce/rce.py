from flask import Flask, request
import subprocess
import platform

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip = request.form.get('ip')
        if ip:
            try:
                if platform.system().lower() == "windows":
                    output = subprocess.check_output("ping -n 1 " + ip, shell=True)
                else:
                    output = subprocess.check_output("ping -c 1 " + ip, shell=True)
                return f'<pre>{output.decode()}</pre>'
            except Exception as e:
                return str(e)
        return "No IP provided"
    else:
        return '''
            <form method="POST">
                IP: <input type="text" name="ip" required><br>
                <input type="submit" value="Ping">
            </form>
        '''

if __name__ == "__main__":
    app.run()