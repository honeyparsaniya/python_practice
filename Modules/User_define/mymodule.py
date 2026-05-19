import random
import datetime

# Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Password Checker

def is_strong_password(password):

    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    return True


# Email Validator

def is_valid_email(email):

    if "@" in email and "." in email:
        return True

    return False


# OTP Generator

def generate_otp():
    return random.randint(100000, 999999)


# Grade System

def grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 50:
        return "C"

    else:
        return "Fail"


# Weather Status

def weather_status(temp):

    if temp > 35:
        return "Hot"

    elif temp < 15:
        return "Cold"

    else:
        return "Normal"


# Current Time

def current_time():
    return datetime.datetime.now()


# Login System

users = {
    "admin": "1234",
    "harnil": "pass123"
}

def login(username, password):

    if username in users and users[username] == password:
        return "Login Successful"

    return "Invalid Username or Password"