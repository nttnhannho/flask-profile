from flask import Flask, render_template
import gspread


gc = gspread.service_account(filename="flask-profile.json")
sh = gc.open("flask-profile")
sh_profile = sh.get_worksheet(0)
sh_contacts = sh.get_worksheet(1)
sh_contacts.append_row(["Bob", "Bob@gmail.com", "Hi"])


app = Flask(__name__)


@app.route("/")
def home():
    profile = {
        "about": sh_profile.acell("B1").value,
        "interests": sh_profile.acell("B2").value,
        "experience": sh_profile.acell("B3").value,
        "education": sh_profile.acell("B4").value
    }
    return render_template("index.html", profile=profile)


app.run(debug=True)
