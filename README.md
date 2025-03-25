# MakersBnB
Full-Stack web application built using legacy code in a group project as part of Makers Academy bootcamp in January 2025.

# Overview
MakersBnB is a web application replicating the core functionalities of the AirBnB platform.

# Tech Stack
Python, Flask, HTML, CSS, PostgreSQL, Playwright, Pytest

# Timeline
5 days 

# My Contributions
Creation of classes, repositories and tests for: 
   - Users, home and requests



## Setup

```shell
# Set up the virtual environment
; python -m venv makersbnb-venv

# Activate the virtual environment
; source makersbnb-venv/bin/activate 

# Install dependencies
(makersbnb-venv); pip install -r requirements.txt

# Install the virtual browser we will use for testing
(makersbnb-venv); playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
(makersbnb-venv); createdb YOUR_PROJECT_NAME
(makersbnb-venv); createdb YOUR_PROJECT_NAME_TEST

# Open lib/database_connection.py and change the database names
(makersbnb-venv); open lib/database_connection.py

# Run the tests (with extra logging)
(makersbnb-venv); pytest -sv

# Run the app
(makersbnb-venv); python app.py

# Now visit http://localhost:5001/index in your browser
```
