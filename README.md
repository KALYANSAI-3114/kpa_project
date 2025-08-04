# KPA API Backend Assignment

This project implements a backend API for a form data application using **Django** and **Django REST Framework**. It is designed to integrate with a Flutter frontend and uses a **MySQL** database for persistence.

***

## Project Description

The assignment required the implementation of two fully functional APIs from a provided Postman collection. This project includes:
* A **`POST`** API for user login and authentication.
* A **`POST`** API for submitting `wheel-specification` data.
* A **`GET`** API for retrieving `wheel-specification` data with filtering capabilities.

All data is stored in a MySQL database, and the backend is configured to work with a local Flutter application.

***

## Technologies and Tech Stack

* **Backend Framework**: Python (Django 5.2.4)
* **API Framework**: Django REST Framework
* **Database**: MySQL
* **Frontend**: Flutter (for demonstration and integration testing)

***

## Setup Instructions

### Prerequisites
* Python 3.10+
* MySQL Server
* Flutter SDK (for the frontend)

### Backend Setup (`kpa_assignment` folder)

1.  **Clone the repository** and navigate to the backend folder:
    ```bash
    cd kpa_assignment
    ```
2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure MySQL**: Open `kpa_backend/settings.py` and update the `DATABASES` settings with your MySQL credentials.
5.  **Run Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6.  **Start the Server**:
    ```bash
    python manage.py runserver
    ```

### Frontend Setup (`KPA-ERP-FE` folder)

1.  **Navigate to the frontend folder**:
    ```bash
    cd KPA-ERP-FE
    ```
2.  **Update the API URL**: In `lib/constants/api_constant.dart`, change `baseUrl` to your local backend server:
    ```dart
    static const String baseUrl = '[http://127.0.0.1:8000](http://127.0.0.1:8000)';
    ```
3.  **Run the App**:
    ```bash
    flutter run
    ```

***

## Implemented APIs

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/users/login/` | `POST` | Authenticates a user with hardcoded phone number and password. |
| `/api/forms/wheel-specifications` | `POST` | Submits new wheel specification data to the database. |
| `/api/forms/wheel-specifications` | `GET` | Retrieves a list of wheel specifications, with optional filters. |

***

## Limitations and Assumptions

* **Login Credentials**: The user authentication is based on hardcoded credentials (`7760873976` / `to_share@123`) and does not use a proper user model or JWT.
* **Database**: The project was developed and tested using MySQL instead of PostgreSQL.
* **Input Validation**: Basic input validation is handled by Django REST Framework's serializers.
