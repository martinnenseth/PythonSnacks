from flask import Flask
app = Flask(__name__)

#Internal URL after main adress
@app.route("/")
def root():
    return "Hello world!"


if __name__ == "__main__":
    app.run()