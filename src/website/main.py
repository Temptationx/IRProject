from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import ir

# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True
))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ir')
def ir_index():
    return render_template('ir/index.html')

@app.route('/ir/irdata')
def ir_data():
    with app.open_resource('data.json', mode='r') as f:
        return f.read()

@app.route('/ir/sendcode')
def ir_sendcode():
    code = request.args.get('code')
    device = request.args.get('device')
    print(code, device)
    if ir.writeCode(device, int(code, 0)):
        return 'ok'
    else:
        return 'fail'

ir.init('/dev/ttyACM0')

app.run(host='0.0.0.0', port=8000)