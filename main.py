from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def index():
    return "<h1>Hi My name is ravi chandra and this flask app demo and deployment through heroku succesful</h1>"

if __name__== '__main__':
    app.run()