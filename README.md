# FastAPI MVC Project

This project is a FastAPI application structured similarly to a Spring Boot MVC application. It includes controllers, models, services, and schemas to manage system users and customers.

## Project Structure

```
fastapi-mvc-project
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── settings.py
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── system_users_controller.py
│   │   └── customer_controller.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── system_users.py
│   │   └── customer.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── system_users_service.py
│   │   └── customer_service.py
│   └── schemas
│       ├── __init__.py
│       ├── system_users_schema.py
│       └── customer_schema.py
├── requirements.txt
└── README.md
```

## Features

- **System Users Management**: Create, read, update, and delete system users.
- **Customer Management**: Create, read, update, and delete customers with a unique ID format `cust-2025/001`.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd fastapi-mvc-project
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the FastAPI application, execute the following command:
```
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.