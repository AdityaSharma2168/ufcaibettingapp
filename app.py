from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/khamzat-whittaker')
def khamzat_whittaker():
    return render_template('khamzat_whittaker.html')

@app.route('/islam-poirier')
def islam_poirier():
    return render_template('islam_poirier.html')

@app.route('/conor-chandler')
def conor_chandler():
    return render_template('conor_chandler.html')

if __name__ == '__main__':
    app.run(debug=True, port = 5001)
