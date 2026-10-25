
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Automated Docker Image Builder</h1>
    <p>Deployed using Docker and GitHub Actions!</p>
    <p>CI Pipeline Status: Working</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
