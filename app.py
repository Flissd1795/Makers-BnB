import os
from lib.users import User
from lib.homes import Home
from lib.users_repository import UserRepository
from lib.homes_repository import HomesRepository
from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection
from datetime import date
from lib.requests_repository import RequestRepository

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

@app.route('/seed', methods=['GET'])
def seed():
    connection = get_flask_database_connection(app)
    connection.seed('seeds/music_web_app_html.sql')
    return 'Database seeded'

@app.route('/index', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    repository = HomesRepository(connection)
    homes = repository.all_homes()
    return render_template('index.html', homes=homes)

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

@app.route('/create_account', methods = ['POST'])
def create_new_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    new_user = User(None, request.form['username'], request.form['email'], request.form['password'])
    if not new_user.is_valid():
        return render_template('create_account.html', new_user=new_user, errors=new_user.generate_errors()), 400
    repository.create_user(new_user.username, new_user.email, new_user.password)
    return redirect(url_for('get_login'))

@app.route('/logout', methods=['GET'])
def get_logout():
    session.clear()  # Clears all session data
    return redirect(url_for('get_login'))

@app.route('/create_home', methods=['GET'])
def get_create_home():
    return render_template('create_home.html', home=Home(None, None, None, None, None, None))

@app.route('/show_home/<id>', methods=['GET'])
def get_show_home(id):
    offset = int(request.args.get('offset', 0))  # Get the offset from query parameters, default to 0
    connection = get_flask_database_connection(app)
    repository = HomesRepository(connection)
    home = repository.find(id)
    user = UserRepository(connection).get_username(home.user_id)
    user = user.get('username')
    booked_dates = repository.fetch_booked_dates(id)
    days_on_calendar_page = repository.load_calendar_page(booked_dates, offset=offset)
    return render_template(
        'show_home.html', 
        home=home, 
        home_owner=user, 
        calendar_dates=days_on_calendar_page,
        calendar_month=days_on_calendar_page[10][0].strftime("%B"),
        calendar_year=days_on_calendar_page[10][0].year,  # Pass the year for better navigation context
        current_offset=offset  # Pass the current offset to the template
    )


#@app.route("/show_home/<id>", methods=["POST"])
#def book(id):
#    start_date = request.form.get("day")
#    if start_date == 1:
#        connection = get_flask_database_connection(app)
#        repository = HomesRepository(connection)
#        home = repository.find(id)
#        user = UserRepository(connection).get_username(home.user_id)
#        user = user.get('username')
#        booked_dates = repository.fetch_booked_dates(id)
#        return render_template('show_home.html', home=home, home_owner=user, month=range(1, 32), booked_dates=booked_dates, start_date=start_date)
#    else:
#        end_date = request.form.get("day")
#        print(f"start date: {start_date}, end date: {end_date}")
#        # Perform booking logic here (e.g., save to database, check availability, etc.)
#        
#    if not start_date or not end_date:
#        return "Please select both dates."
#
#        # Ensure the end date is not earlier than the start date
#        
#    if start_date > end_date:
#        return "Error: Check-out date must be after check-in date."
#    
#    return render_template("index.html")
  
#@app.route("/show_home/<id>", methods=["POST"])
#def book(id):
#    if request.method == "POST":
#        start_date = request.form.get("day")
#        end_date = request.form.get("day")
#
#        if not start_date or not end_date:
#            return "Please select both dates."
#
#        # Ensure the end date is not earlier than the start date
#        if start_date > end_date:
#            return "Error: Check-out date must be after check-in date."
#
#        # Perform booking logic here (e.g., save to database, check availability, etc.)
#        return f"Booking successful from {start_date} to {end_date}!"
#    
#    return render_template("index.html")

# @app.route('/all_requests', methods=['GET'])
# def get_all_requests():
#     connection = get_flask_database_connection(app)
#     repository = HomesRepository(connection)
#     users_id = session.get('users_id') 
#     homes = repository.find_all(users_id)
#     return render_template('all_requests.html', homes=homes)

@app.route('/all_requests', methods=['GET'])
def get_all_requests():
    connection = get_flask_database_connection(app)
    request_repository = RequestRepository(connection)
    repository = HomesRepository(connection)

    users_id = session.get('users_id')  # Get the current user's ID from the session
    if not users_id:
        return redirect(url_for('login'))  # Redirect to login if user is not logged in

    # Fetch requests made and requests received
    requests_made = request_repository.list_requests_by_user_id(users_id)
    requests_received = request_repository.list_requests_by_home_owner(users_id)
    homes = repository.find_all(users_id)
    # Pass the lists to the template
    return render_template(
        'all_requests.html',
        requests_made=requests_made,
        requests_received=requests_received,
        homes=homes
    )

@app.route('/auth_request/<id>', methods=['GET'])
def get_auth_requests(id):
    connection = get_flask_database_connection(app)
    repository = RequestRepository(connection)
    request = repository.find_request(id)
    if not request:
        return render_template('404.html'), 404
    request_details = repository.get_request_details(id)
    return render_template('auth_request.html', request=request_details)

@app.route('/confirm', methods=['POST'])
def confirm_request():
    connection = get_flask_database_connection(app)
    repository = RequestRepository(connection)
    request_id = request.form['request_id']
    repository.confirm_request(request_id)
    return redirect(url_for('get_all_requests'))

@app.route('/deny', methods=['POST'])
def deny_request():
    connection = get_flask_database_connection(app)
    repository = RequestRepository(connection)
    request_id = request.form['request_id']
    repository.delete_request(request_id)
    return redirect(url_for('get_all_requests'))

@app.route('/create_home', methods = ['POST'])
def create_home():
    users_id = session.get('users_id') 
    if not users_id:
        return redirect(url_for('get_login'))
    connection = get_flask_database_connection(app)
    repository = HomesRepository(connection)
    title = request.form['title']
    description = request.form['description']
    location = request.form['location']
    price_per_night = request.form['price_per_night']
    home = Home(None, title, description, location, price_per_night, int(users_id))
    if not home.is_valid():
        return render_template('create_home.html', home=home, errors=home.generate_errors()), 400
    repository.create_home(title, description, location, price_per_night, int(users_id))
    return redirect(url_for('get_index'))

@app.route("/book", methods=["POST"])
def book_home():
    user_id = session.get('users_id')
    db_connection = get_flask_database_connection(app)
    request_repo = RequestRepository(db_connection)
    # Extract form data
    status = request.form.get("status")
    date_submitted = date.today().strftime("%Y-%m-%d")
    home_id = request.form.get("home_id")
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")
    # Call the repository's `create_request` method
    request_repo.create_request(status, date_submitted, home_id, user_id, start_date, end_date)
    # Redirect the user to a confirmation page or another route
    return redirect(url_for("get_index"))


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.secret_key = os.environ.get('SECRET_KEY', 'super secret key')
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
