from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    auth_code = request.args.get('code')
    return f"Authorization Code: {auth_code}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)