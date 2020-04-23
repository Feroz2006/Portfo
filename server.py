from flask import Flask, render_template, url_for, request, redirect
import csv

# To run this website use the following commands on the terminal:
# NOTE Use Command prompt as Powershell wont work
# cd FerozWeb
# set FLASK_APP=server.py
# set FLASK_ENV=development
# flask run
#NOTE Sometimes you have to activate the virtual environment before running the above commands
#To do this :
# Make sure you are in the FerozWeb directory and are using command prompt
# Then enter : .\Scripts\activate.bat

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home_page():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open("database.csv",newline = "", mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=[ 'POST', 'GET' ])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/ThankYou.html")
        except:
            return "Sorry ! Did not save to database !"
    else:
        return ("Something went wrong ! Please go back and try again ! ")
        






