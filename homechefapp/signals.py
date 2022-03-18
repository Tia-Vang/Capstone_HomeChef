from django.db.models.signals import post_save
from .models import user

def create_user():
    #logic for making user goes here
    print("user created") #for debugging

def update_user():
    #logic for updating user goes here
    print("user updated") #for debugging

def login_user():
    #logic for loging a user in
    print("user logged in") #for debugging

def logout_user():
    #logic for logging out user goes here
    print("user logged out") #for debugging
    