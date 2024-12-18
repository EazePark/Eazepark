from flask import Flask, render_template, request, redirect, url_for
import yagmail
import os
import logging
app = Flask(__name__)
payments = {}

# Gmail SMTP configuration (Replace with your Gmail credentials)
smtp_username = "test1ofpython@gmail.com"
smtp_password = "bjwmlishuadqpvyr"

logging.basicConfig(level=logging.INFO)

def send_email(car_number, money, recipient_email="ineazepark@gmail.com"):
    subject = "Parking Payment Receipt"
    body = f"Car Number: {car_number}\nMoney Paid: {money}"

    try:
        yag = yagmail.SMTP(smtp_username, smtp_password)
        yag.send(recipient_email, subject, body)
        logging.info("Email sent successfully")
    except Exception as e:
        logging.error(f"Email sending failed: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/payment_successful', methods=['GET', 'POST'])
def payment_successful():
    return render_template('payment_successful.html')

@app.route('/process_payment', methods=['POST'])
def process_payment():
    car_number = request.form.get('carNumber')
    money = request.form.get('money')
    
    if car_number and money:
        payments[car_number] = money
        send_email(car_number, money)
        logging.info(f'Car Number: {car_number}, Amount: {money}')
        return redirect(url_for("payment_successful"))
    else:
        return "Error: Car Number and Money are required", 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
