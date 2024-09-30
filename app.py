from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return ('Hello, World! We are testing Linear with Github and first time using Flask '
            'for the FlexFlow project!')

