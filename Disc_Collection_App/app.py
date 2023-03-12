from flask import Flask, request, render_template, redirect, url_for

from forms import DiscCollection
from models import discs

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/discs/", methods=["GET", "POST"])
def discs_collection():
    form = DiscCollection()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            discs.create(form.data)
            discs.save_all()
        return redirect(url_for("discs_collection"))

    return render_template("discs.html", form=form, discs=discs.all(), error=error)


@app.route("/discs/<int:disc_id>/", methods=["GET", "POST"])
def discs_details(disc_id):
    disc = discs.get(disc_id - 1)
    form = DiscCollection(data=disc)

    if request.method == "POST":
        if form.validate_on_submit():
            discs.update(disc_id - 1, form.data)
        return redirect(url_for("discs_collection"))
    return render_template("disc.html", form=form, disc_id=disc_id)


if __name__ == "__main__":
    app.run(debug=True)