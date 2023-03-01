from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "There's nothing here!"

@app.route('/hello')
def hello():
    my_name = "John"
    return f'Hello, {my_name}!'

@app.route('/blog')
def blog_main():
    return f"This is a main blog page"

@app.route('/blog/<id>')
def blog(id):
    return f"This is blog entry #{id}"

@app.route('/message', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/hello")

@app.route('/greeting')
def greeting():
    return render_template("greeting.html")

@app.route("/warehouse")
def warehouse():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("warehouse.html", items=items, errors=errors)

@app.route("/warehouse2")
def warehouse2():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("warehouse2.html", items=items, errors=errors)

@app.route("/warehouse3")
def warehouse3():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("warehouse3.html", items=items, errors=errors)

@app.route('/mypage/me', methods=['GET'])
def me():
    return render_template("8.4_me.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
       print("We received GET")
       return render_template("8.4_kontakt.html")
    elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/kontakt")