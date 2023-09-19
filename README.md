# Django JWT Authentication Project

## Project Overview

This Django project demonstrates JWT (JSON Web Token) authentication with a PostgreSQL database. It provides user registration, login, and token-based authentication using the Django Rest Framework and Simple JWT library.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Development Server](#running-the-development-server)
  - [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Database](#database)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Getting Started

### Prerequisites

- Python 3.7+
- Django 3.2
- PostgreSQL
- Pipenv (optional but recommended for virtual environment management)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/charlie-black/django_jwt_authentication.git
   
2. Change to the project dire4ctory:
   cd django-jwt-authentication

3. Create a virtual environment(optional but recommended)
   pipenv install
   pipenv shell

4. Install projects dependencies
   pip install -r requirements.txt

### Usage
Running the Development Server
To run the development server, use the following command:

python manage.py runserver

The server will start at http://localhost:8000/.

### API Endpoints
Register a New User: POST /authentication/api/register/
Example Request body:
{
    "email": "user@example.com",
    "password": "securepassword"
}

Example response:
{
    "user_id": "12345",
    "email": "user@example.com",
    "access_token": "your_access_token_here",
    "refresh_token": "your_refresh_token_here"
}

Login : POST /authentication/api/login/

View profile : POST /authentication/api/profile/

### Authentication
This project uses JWT (JSON Web Token) authentication. To obtain an access token, send a POST request with valid login credentials to the /authentication/api/token/ endpoint. The response will include both an access token and a refresh token.

### Database
The project uses a PostgreSQL database. Make sure to set up the database configuration in your settings.py file.

### Testing
To run tests for the project, use the following command:
python manage.py test

### Contributing
Contributions are welcome!

### License
This project is licensed under the MIT License

### Contact
If you have any questions or feedback, feel free to contact us at omwacharles@gmail.com.

