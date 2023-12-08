# Django REST API Setup

This repository contains a Django project with a RESTful API using Django REST Framework.

## Prerequisites

- Python (version 3.x recommended)
- Django
- Django REST Framework

## Setup Instructions

## Create a Virtual Environment:
- pip install virtualenvwrapper-win
- mkvirualenv environmentname

## Install Dependencies:
- pip install django
- pip install djangorestframework

## Set up a new project with a single application
- django-admin startproject Vendor                 
- cd Vendor
- django-admin startapp Vendor_App              

## Database migration
- cd Vendor                         
- python manage.py makemigrations      
- python manage.py migrate

## Superuser creation and Token generation
- python manage.py createsuperuser
- curl -X POST -d "username=your_superuser_username&password=your_superuser_password" http://localhost:8000/api-token-auth/

## Running the server
- python manage.py runserver

## Access Django Admin:
Open the Django admin at http://127.0.0.1:8000/admin/ and log in using the superuser credentials.

# Testing or Using the API endpoints.
- we can test API endpoints using curl or httpie commands. 

## Create a vendor:
### using curl:
- curl -H "Authorization: Token your_obtained_token" -X POST http://127.0.0.1:8000/api/vendors/ -d "vendor_code=01&name=Vendor+1&contact_details=Contact+1&address=Address+1"
### using httpie:
- http POST http://127.0.0.1:8000/api/vendors/ vendor_code=01 name="Vendor 1" contact_details="Contact 1" address="Address 1" "Authorization: Token your_obtained_token"
### About this API endpoint:
- here this endpoint is used to create a vendor by providing the vendor details.

## List all Vendors details:
### using curl:

### using httpie:

## Retrieve a specific vendor's details:
### using curl:

### using httpie:

## Update a vendor's details:
### using curl:

### using httpie:

## Delete a vendor:
### using curl:

### using httpie:

## Create a purchase_order:
### using curl:

### using httpie:

## List all purchase_orders details:
### using curl:

### using httpie:

## Retrieve a specific purchase_order's details:
### using curl:

### using httpie:

## Update a purchase_order's details:
### using curl:

### using httpie:

## Delete a purchase_order:
### using curl:

### using httpie:

## Retrieve a vendor's performance metrics:
### using curl:

### using httpie:

## Update acknowledgment_data and trigger the recalculation of average_response_time:
### using curl:

### using httpie:



