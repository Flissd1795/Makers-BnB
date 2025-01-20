import os
from lib.users import User
from lib.users_repository import UserRepository
from flask import Flask, request, render_template, session
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

def start_session():
    connection = get_flask_database_connection(app)
    email = request.form['email']
    repository = UserRepository(connection)
    user_as_dict = repository.find_user(email)
    user_as_object = User(user_as_dict['id'], user_as_dict['username'], user_as_dict['email'], user_as_dict['password'], user_as_dict['picture_id'])
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

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
