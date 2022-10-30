# Overview

This web app is a login system that I created to be able to use with different applications. you can create an account, or login with an existing account. to start a test server i opened my virtual environment, and run the command "python manage.py runserver" . In order to open it you enter "http://127.0.0.1:8000/accounts/"

My pupose for writing this software is to learn Django, and write a web app to gain experience with it.


[Software Demo Video](https://youtu.be/Rlsg6cDSYvI)

# Web Pages

 Home, create account, login, authorized, not authorized.

 I made a home page with links to a login page and a create account page.
 The create account page allows you to enter a username and password, when you click the submit button it will take you back to the home page.
 The login page allows you to enter your username and password. If they are correct it takes you to a page that tells you that you are authorized, and has a link to take you back home.
 If the username and password are not correct it takes you to a page that says you are not authorized, and has a link to click to try again.

# Development Environment

The tool I used to write this was Virtual Studio Code.

Writen in python using the Django library, and Html.

# Useful Websites

* [W3Schools](https://www.w3schools.com/django/index.php)
* [youtube](https://www.youtube.com/watch?v=rHux0gMZ3Eg)

# Future Work

* Create an option to delete an account.
* Style the web pages.
* Ensure two acccounts can't have the same username.
