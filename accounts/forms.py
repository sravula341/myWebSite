from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class createUserForm(UserCreationForm):
     class Meta:
        model = User
        fields = ['username','email','password1','password2']