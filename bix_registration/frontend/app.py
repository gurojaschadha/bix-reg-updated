from flask import Flask, render_template, request, jsonify
import requests  # Add this import

app = Flask(__name__)

# Define the Django API URL
DJANGO_API_URL = "http://localhost:8000/api/register/"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        bix_id = request.form['bix_id']
        license_number = request.form['license_number']
        aadhar_number = request.form['aadhar_number']
        duration = request.form['duration']
        boat_type = request.form['boat_type']

        data = {
            'bix_id': bix_id,
            'license_number': license_number,
            'aadhar_number': aadhar_number,
            'duration': duration,
            'boat_type': boat_type,
        }

        response = requests.post(DJANGO_API_URL, json=data)
        if response.status_code == 201:
            return render_template('success.html', message='Boat registered successfully!')
        elif response.status_code == 400:
            error_message = response.json().get('error', 'An error occurred while registering the boat.')
            return render_template('error.html', error=error_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
