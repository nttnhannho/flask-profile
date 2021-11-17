from flask import Flask, render_template, request
import gspread


gc = gspread.service_account(filename="flask-profile.json")
sh = gc.open("flask-profile")
sh_profile = sh.get_worksheet(0)
sh_contacts = sh.get_worksheet(1)


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        sh_contacts.append_row([request.form["name"],
                               request.form["email"],
                               request.form["message"]])
    profile = {
        "about": sh_profile.acell("B1").value,
        "interests": sh_profile.acell("B2").value,
        "experience": sh_profile.acell("B3").value,
        "education": sh_profile.acell("B4").value
    }
    return render_template("index.html", profile=profile)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
