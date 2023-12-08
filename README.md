# Django REST API Setup

This repository contains a Django project with a RESTful API using Django REST Framework.

## Prerequisites

- Python (version 3.x recommended)
- Django
- Django REST Framework

## Setup Instructions

## Create a Virtual Environment:
-pip install virtualenvwrapper-win
-mkvirualenv environmentname

## Install Dependencies:
-pip install django
-pip install djangorestframework

## Set up a new project with a single application
-django-admin startproject Vendor                  //creates a Vendor project
-cd Vendor
-django-admin startapp Vendor_App                  //creates a Vendor_App named app in Vendor project

## Database migration and user creation
-cd Vendor                         //getting into Vendor project
-python manage.py makemigrations       //making migrations
-python manage.py migrate              //migrating the migrations to database
-python manage.py createsuperuser      //creating super user

## Running the server
-python manage.py runserver           //running the server
