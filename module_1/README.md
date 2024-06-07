## To start the server
- Run python3 manage.py makemigrations
- Run python3 manage.py migrate
- Run python3 manage.py runserver

### To test the server while it is running, run
- http://localhost:8000/login
- Then to get the data gotten after authentication, run
- http://localhost:8000/callback
  
# VIEWS
- login/ - Redirects the user to the authentication page
- callback/ - Gets the information after authentication and stores it in the database

# Models
- githubApp - Holds the class information for the private and public repositories
