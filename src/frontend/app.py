from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BACKEND_URL = "http://localhost:5000"  
# later this becomes: http://backend:5000 in Docker/K8s

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        data = {
            "a": request.form["a"],
            "b": request.form["b"],
            "op": request.form["op"]
        }
        res = requests.post(BACKEND_URL, data=data)
        result = res.text
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
