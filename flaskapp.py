from flask import Flask
from flask import request

#WA[
from whatsapp import Client
expected_token = 'fOaoY18Z8UpTI+XT+4P1dyUfF4I='
#]WA

app = Flask(__name__)



@app.route('/')ssssss
def hello_world():

    return 'Hello World!'

@app.route('/msg', methods = ['POST'])
def msg():
    to = request.form['to']
    return str(to)

@app.route('/sendmsg')
def sendmsg():
    to = request.args.get('to')
    msg = request.args.get('msg')
    token = request.args.get('token')
    if(str(token) == expected_token):
        client = Client(login='919439475972', password='ZpEHNPzY+b1tyfAaSFeP0Yrmpiw=')
        res = client.send_message(to, msg)  
    
    else:
        res = 'Unauthorized'
    
    return str(res)

if __name__ == '__main__':
    app.run()