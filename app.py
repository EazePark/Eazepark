from flask import Flask, render_template, request, redirect, url_for
import yagmail

app = Flask(__name__)

# Store car_number and money in a dictionary
payments = {}

# Gmail SMTP configuration (Replace with your Gmail credentials)
smtp_username = "test1ofpython@gmail.com"
smtp_password = "hwkwrrdtgcmolelx"

def send_email(car_number, money):
    subject = "Parking Payment Receipt"
    body = f"Car Number: {car_number}\nMoney Paid: {money}"

    try:
        # Create a yagmail SMTP connection
        yag = yagmail.SMTP(smtp_username, smtp_password)

        # Send the email
        yag.send("ineazepark@gmail.com", subject, body)

        print("Email sent successfully")
    except Exception as e:
        print(f"Email sending failed: {str(e)}")

@app.route("/pay", methods=["GET", "POST"])
def pay():
    if request.method == "POST":
        car_number = request.form.get("car_number")
        money = request.form.get("money")

        # Store car_number and money in the dictionary
        payments[car_number] = money

        # Send an email using yagmail
        send_email(car_number, money)

        # Redirect to payment_successful.html on successful payment
        return redirect(url_for("payment_successful"))

    return render_template("index.html", payments=payments)

@app.route("/payment_successful")
def payment_successful():
    return render_template("payment_successful.html")

@app.route("/")
def index():
    return render_template("index.html", payments=payments)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
