from flask import Flask, render_template, request, redirect
import csv

# Instance of Flask application
app = Flask(__name__)

# Decorator for extra tools
@app.route('/')
def my_portfolio():
    return render_template('index.html')

# Decorator to display Thank You page
@app.route('/ThankYou.html')
def thank_you():
    return render_template('ThankYou.html')

# Method for writing to text file


def write_to_database(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


# Method for writing to .csv file
def write_to_CSV(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter='|',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        my_data = request.form.to_dict()
        # write_to_DB(my_data)
        write_to_CSV(my_data)
        return redirect('/ThankYou.html')
    return 'Uh oh! Something went wrong.'
