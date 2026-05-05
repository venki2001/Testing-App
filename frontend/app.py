from datetime import datetime
from flask import Flask, jsonify, render_template, request
import requests

BACKEND_URL = 'http://127.0.0.1:8000'

app = Flask(__name__)

@app.route('/')
def home():
    current_Day_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    print(current_Day_week)
    return render_template('index.html',current_Day_week=current_Day_week,current_time=current_time)

@app.route('/signup',methods=['POST'])
def signup():
    form_data=dict(request.form)
    requests.post(BACKEND_URL +'/signup' ,json=form_data)
    return "Data submitted successfully !!!"

@app.route('/get_data')
def get_data():
    response = requests.get(BACKEND_URL+'/view')
    return response.json()

print("Hello This is Venkatesh !!!! ")
if __name__ == '__main__' :
    app.run(debug=True, port=9000, host='127.0.0.1')
