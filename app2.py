from flask import Flask

app = Flask(__name__)

@app.route('/')

#def hello_world():
#    return 'Hello world'

def poetry():
    return "Roses are red, violets are blue"