from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/aboutus")
def aboutus():
    return render_template("about.html")

@app.route("/Contactus")
def Contactus():
    return render_template("Contactus.html")

@app.route("/Collections")
def Collections():
    return render_template("Collections.html")

@app.route("/Collections/men/g&s")
def mengs():
    return render_template("mengs.html")

@app.route("/Collections/women/g&s")
def womengs():
    return render_template("womengs.html")

@app.route("/Collections/men/covering")
def mencover():
    return render_template("mencover.html")

@app.route("/Collections/women/covering")
def womencover():
    return render_template("womencover.html")

app.run(debug=False,host='0.0.0.0')