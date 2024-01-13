from flask import Flask, render_template, request,redirect,url_for
import yagmail
app = Flask(__name__)
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
    payments[car_number] = money
    send_email(car_number, money)
    print(f'Car Number: {car_number}, Amount: {money}')
    # Add your payment processing logic here
    return redirect(url_for("payment_successful"))
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
