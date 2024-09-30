from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return ('Hello, World! We are testing Linear with Github integration. We might use flask for this project !'
            'For manual linking using commit message: git commit -m your message [PRON-123]')

