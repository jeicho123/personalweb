from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Contact-Form").sheet1 

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        name = request.form["Name"]
        email = request.form["Email"]
        message = request.form["Message"]

        row = [name, email, message]
        sheet.insert_row(row, 2)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True) 