from flask import Flask, render_template, request, redirect, url_for
import smtplib
import os

MY_EMAIL = "psmadhantruth733@gmail.com"
password = os.environ.get("PASSWORD")


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Resume")
def resume():
    return render_template("resume.html")  

@app.route("/Skills")
def skills():
    return render_template("skills.html")  

@app.route("/AWS")
def aws():
    return render_template("aws.html")

@app.route("/Devops")
def devops():
    return render_template("dev.html")

@app.route("/Python")
def python():
    return render_template("py.html")


@app.route("/Projects")
def projects():
    return render_template("projects.html")  

@app.route("/Contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        # print(data['name'])
        # print(data['email'])
        send_mail(data['name'], data['email'], data['phone'], data['message'])
        return render_template ("index.html")
    return render_template("contact.html")  

def send_mail(name, email, phone, message):
    email_message = f"subject: Important\n\nName: {name}\nEmail: {email}\nphone: {phone}\nMessage: {message}"
    
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=MY_EMAIL, password=password)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="madhanselvamani733@gmail.com", msg=email_message)

if __name__ == "__main__":
    app.run(debug=True)