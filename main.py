from flask import Flask, Blueprint, url_for, render_template, flash, request
from flask.config import ConfigAttribute
from flask.globals import session
import HarRef

app = Flask(__name__)
app.secret_key = "123"

@app.route("/")
def root():
    return render_template("home.html")

@app.route("/HarvardRef", methods=["POST", "GET"])
def harv():
    if request.method == "GET":
        return render_template("HarvardReference.html")
    else: 
        names: list[str] = request.form["author"].split(", ")
        output = HarRef.EJournal(
            author=HarRef.Names(names), 
            year_of_publication=request.form["year"], 
            title_of_article=request.form["article"], 
            title_of_journal=request.form["journal"], 
            volume_number=request.form["vol"], 
            part_number=request.form["part"], 
            page=int(request.form["page"]),
            url=request.form["url"]
        )
        return render_template("HarvardReference.html", output=f"{output.end_text()}")
        

if __name__ == "__main__": 
    app.run(debug=True)


