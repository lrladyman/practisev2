from flask import Flask, render_template, request
app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hello! Welcome to my website you"

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data=request.form
    print form_data["email"]
    return "All ok!"

if __name__ == '__main__':
    app.run(debug=True)
