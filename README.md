# DjangoRF

DjangoRF is a simple REST API that allows users to manage articles, authors, and categories. The API is built with Django and the Django REST Framework.

# Installation
To use DjangoRF, follow these steps:

### Clone the repository:

`git clone https://github.com/otyomaa/DjangoRF.git`

### Install the dependencies:

`pip install -r requirements.txt`

### Apply the migrations:

`python manage.py migrate`

### Create a superuser:

`python manage.py createsuperuser`

### Run the server:

`python manage.py runserver`

## Usage
Once the server is running, you can access the API at http://localhost:8000/api/. The API endpoints are:

http://localhost:8000/notes/: allows you to list, create, and update notes.
http://localhost:8000/tags/: allows you to list, create, and update tags.
To access the endpoints that require authentication, you will need to use a client that supports authentication, such as curl or httpie. To authenticate, send a POST request to http://localhost:8000/token/ with your username and password in the request body. You will receive a JSON response with an access token. Include this token in the Authorization header of your subsequent requests.

For example, to create a new article, you can send a POST request to http://localhost:8000/notes/ with the following JSON payload:
`
{
    "title": "My Article",
    "content": "Lorem ipsum...",
    "author": 1,
    "categories": [1, 2]
}
`
Replace 1 with the ID of the author you want to associate with the article, and 1 and 2 with the IDs of the categories you want to associate with the article. Include your access token in the Authorization header of the request.

License
DjangoRF is licensed under the MIT License. See LICENSE for more information.
