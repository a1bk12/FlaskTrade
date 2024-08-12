from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    # Extract the 'code' parameter from the query string
    auth_code = request.args.get('code')
    if auth_code:
        return f"Authorization Code: {auth_code}", 200
    else:
        return "No authorization code found in the request.", 400

if __name__ == "__main__":
    app.run()