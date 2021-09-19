
from flask import Flask, render_template, url_for, redirect
from datetime import datetime
import re


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content="vpn")
    
@app.route("/template")
def testsite():
    return render_template("index.html", content="testing")

        # @app.route("/hello/<name>")
        # def hello_there(name):
        #     now = datetime.now()
        #     formatted_now = now.strftime("%A, %d %B, %Y at %X")
        #     match_obj = re.match("[a-zA-Z]+", name)

        #     if match_obj:
        #         clean_name = match_obj.group(0)
        #     else:
        #         clean_name = "Friend"

        #     content = "Hello, " + clean_name + "! Ir is " + formatted_now
        #     return content

if __name__ == "__main__":
    app.run(debug=True)