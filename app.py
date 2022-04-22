"""
Run with black for formatting, and isort for import sorting
$ isort . --profile black
$ black .

Also, we configure github actions for atomatically run the rest of toolings
"""


from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "OK"


if __name__ == "__main__":
    app.run()
