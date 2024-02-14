from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():

    return render_template('user/main.html')

@app.route('/services')
def services():

    return render_template('user/services.html')

@app.route('/masters')
def masters():

    return render_template('user/masters.html')

@app.route('/appointment')
def appointment():

    return render_template('user/appointment.html')

@app.route('/base')
def base():

    return render_template('base.html')