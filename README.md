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
- curl -H "Authorization: Token your_obtained_token" http://127.0.0.1:8000/api/vendors/
### using httpie:
- http http://127.0.0.1:8000/api/vendors/ "Authorization: Token your_obtained_token"
### About this API endpoint:

## Retrieve a specific vendor's details:
### using curl:
- curl -H "Authorization: Token your_obtained_token" http://127.0.0.1:8000/api/vendors/{vendor_id}/
### using httpie:
- http http://127.0.0.1:8000/api/vendors/{vendor_id}/ "Authorization: Token your_obtained_token"
### About this API endpoint:

## Update a vendor's details:
### using curl:
- curl -H "Authorization: Token your_obtained_token" -X PUT http://127.0.0.1:8000/api/vendors/{vendor_id}/ -d "vendor_code=updated code&name=Updated Vendor Name&contact_details=Updated Contact Details&address=Updated Address"
### using httpie:
- http PUT http://127.0.0.1:8000/api/vendors/{vendor_id}/ name="Updated Vendor Name" contact_details="Updated Contact Details" address="Updated Address" "Authorization: Token your_obtained_token"
### About this API endpoint:

## Delete a vendor:
### using curl:
- curl -H "Authorization: Token your_obtained_token" -X DELETE http://127.0.0.1:8000/api/vendors/{vendor_id}/
### using httpie:
- http DELETE http://127.0.0.1:8000/api/vendors/{vendor_id}/ "Authorization: Token your_obtained_token"
### About this API endpoint:

## Create a purchase_order:
### using curl:
- curl -H "Authorization: Token your_obtained_token" -X POST http://127.0.0.1:8000/api/purchase_orders/ -d "po_number=01&vendor=01&order_date=2023-01-01T12:00:00&delivery_date=2023-01-10T12:00:00&items=[{\"item_name\":\"Item 1\",\"quantity\": 10 },{\"item_name\":\"Item 2\",\"quantity\": 10 }]&quality_rating=4.5&issue_date=2023-01-01T12:00:00&status=updated&acknowledgment_date=2023-01-02T12:00:00&quantity=8"
### using httpie:
- http POST http://127.0.0.1:8000/api/purchase_orders/ po_number=01 vendor=01 order_date="2023-01-01" items="Item 1" quantity=10 status="Pending" "Authorization: Token your_obtained_token"
### About this API endpoint:

## List all purchase_orders details:
### using curl:
- curl -H "Authorization: Token your_obtained_token" http://127.0.0.1:8000/api/purchase_orders/
### using httpie:
- http http://127.0.0.1:8000/api/purchase_orders/ "Authorization: Token your_obtained_token"
### About this API endpoint:

## Retrieve a specific purchase_order's details:
### using curl:
- curl -H "Authorization: Token your_obtained_token" http://127.0.0.1:8000/api/purchase_orders/{po_id}/
### using httpie:
- http http://127.0.0.1:8000/api/purchase_orders/{po_id}/ "Authorization: Token your_obtained_token"
### About this API endpoint:

## Update a purchase_order's details:
### using curl:
- curl -H "Authorization: Token your_obtained_token" -X PUT http://127.0.0.1:8000/api/purchase_orders/{po_id}/ -d "po_number=updatedno&vendor=updatedvno&order_date=2023-01-02T12:00:00&delivery_date=2023-01-15T12:00:00&items=[{\"item_name\":\"updated item 2\",\"quantity\": 10 },{\"item_name\":\"updated Item 2\",\"quantity\": 10 }]&quality_rating=5&issue_date=2023-01-01T12:00:00&status=updated&acknowledgment_date=2023-01-01T12:00:00"
### using httpie:
- http PUT http://127.0.0.1:8000/api/purchase_orders/{po_id}/ po_number="UpdatedPO001" order_date="2023-01-02T12:00:00" delivery_date="2023-01-15T12:00:00" items:='[{"item_name": "Updated Item", "quantity": 20 }]' quality_rating:=4.8 status="updated" "Authorization: Token your_obtained_token"
### About this API endpoint:

## Delete a purchase_order:
### using curl:
- curl -H "Authorization: Token your_obtained_token" -X DELETE http://127.0.0.1:8000/api/purchase_orders/{po_id}/
### using httpie:
- http DELETE http://127.0.0.1:8000/api/purchase_orders/{po_id}/ "Authorization: Token your_obtained_token"
### About this API endpoint:

## Retrieve a vendor's performance metrics:
### using curl:
- curl -H "Authorization: Token your_obtained_token" http://127.0.0.1:8000/api/vendors/1/performance/
### using httpie:
- http http://127.0.0.1:8000/api/vendors/1/performance/ "Authorization: Token your_obtained_token"
### About this API endpoint:

## Update acknowledgment_data and trigger the recalculation of average_response_time:
### using curl:
- curl -H "Authorization: Token your_obtained_token" -X POST http://127.0.0.1:8000/api/purchase_orders/{po_id}/acknowledge/
### using httpie:
- http POST http://127.0.0.1:8000/api/purchase_orders/{po_id}/acknowledge/ "Authorization: Token your_obtained_token"
### About this API endpoint:

