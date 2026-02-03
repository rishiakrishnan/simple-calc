from flask import Flask, request, render_template
import argparse

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            op = request.form["op"]

            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                result = "Error: Divide by zero" if b == 0 else a / b
        except ValueError:
            result = "Error: Invalid Input"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    # 1. Setup the argument parser
    parser = argparse.ArgumentParser(description="Run the Flask Calculator")
    
    # 2. Add the --port argument (defaulting to 5000 if not provided)
    parser.add_argument("--port", type=int, default=5000, help="Port to run the app on")
    
    # 3. Parse the arguments
    args = parser.parse_args()

    # 4. Pass the port to app.run
    app.run(debug=True, port=args.port)