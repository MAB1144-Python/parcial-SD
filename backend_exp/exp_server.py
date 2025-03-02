from flask import Flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def experiment():
    app = Flask(__name__)

    @app.route('/')
    def experiment():
        response = jsonify({"error": "Experimental Server encountered an issue"})
        response.status_code = 500
        return response

    if __name__ == '__main__':
        app.run(host='198.162.0.1', port=0)

if __name__ == '__main__':
    app.run(host='198.162.0.1', port=0)
