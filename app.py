import os
from lib.users import User
from lib.users_repository import UserRepository
from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

def start_session():
    connection = get_flask_database_connection(app)
    email = request.form['email']
    repository = UserRepository(connection)
    user_as_dict = repository.find_user(email)
    user_as_object = User(user_as_dict['id'], user_as_dict['username'], user_as_dict['email'], user_as_dict['password'])
    session['users_id'] = user_as_object.id
    session['username'] = user_as_object.username

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Get email and password from the form
    connection = get_flask_database_connection(app)
    email = request.form['email']
    password = request.form.get('password') 
    repository = UserRepository(connection)
    if repository.check_password(email, password):
        start_session()
        return redirect(url_for('get_index')) # Redirect to the main page after successful login
    else:
        return redirect('/create_account') # Redirect to create account page if email not found

@app.route('/create_account', methods=['GET'])
def get_create_account():
    return render_template('create_account.html')

@app.route('/create_home', methods=['GET'])
def get_create_home():
    return render_template('create_home.html')

@app.route('/show_home', methods=['GET'])
def get_show_home():
    return render_template('show_home.html')

@app.route("/show_home", methods=["POST"])
def book():
    if request.method == "POST":
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")

        if not start_date or not end_date:
            return "Please select both dates."

        # Ensure the end date is not earlier than the start date
        if start_date > end_date:
            return "Error: Check-out date must be after check-in date."

        # Perform booking logic here (e.g., save to database, check availability, etc.)
        return f"Booking successful from {start_date} to {end_date}!"
    
    return render_template("index.html")

@app.route('/all_requests', methods=['GET'])
def get_all_requests():
    return render_template('all_requests.html')

@app.route('/auth_requests', methods=['GET'])
def get_auth_requests():
    return render_template('auth_request.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
