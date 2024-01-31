Here is the main Python code (`main.py`) for a Flask application that tracks flight prices from Hyderabad to Mumbai, selects the lowest fare option, and displays the results:


from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        departure_date = request.form['departure_date']
        arrival_date = request.form['arrival_date']
        # Make an API call to retrieve flight data using the departure and arrival dates
        flight_data = get_flight_data(departure_date, arrival_date)
        # Select the lowest fare option from the retrieved flight data
        lowest_fare_option = select_lowest_fare_option(flight_data)
        return render_template('results.html', lowest_fare_option=lowest_fare_option)
    return render_template('index.html')

@app.route('/results')
def results():
    lowest_fare_option = request.args.get('lowest_fare_option')
    return render_template('results.html', lowest_fare_option=lowest_fare_option)

def get_flight_data(departure_date, arrival_date):
    # API call code
    # Parse and return the retrieved flight data

def select_lowest_fare_option(flight_data):
    # Code to select the lowest fare option from the flight data
    # Return the selected lowest fare option

if __name__ == '__main__':
    app.run(debug=True)


**Note:** This code provides the basic structure of the Flask application. You will need to implement the API call code and the logic to select the lowest fare option based on your specific requirements and the data format provided by the API.

To run the application, you can follow these steps:

1. Create an HTML file named 'index.html' with the necessary HTML code for the home page form.
2. Create an HTML file named 'results.html' with the necessary HTML code to display the lowest fare option.
3. Save the above Python code as 'main.py'.
4. Open a terminal or command prompt, navigate to the directory where these files are located, and run the command:


python main.py


This will start the Flask application. You can then access the application by visiting `http://localhost:5000/` in your web browser.

Remember to replace the API call code (`get_flight_data`) and the logic to select the lowest fare option (`select_lowest_fare_option`) with your actual implementation based on the specific API you are using and the data format it provides.