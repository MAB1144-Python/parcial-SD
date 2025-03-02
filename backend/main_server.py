from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Response from Main Server"

if __name__ == '__main__':
    app.run(host='198.162.0.1', port=0)
