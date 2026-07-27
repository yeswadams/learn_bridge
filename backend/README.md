# LearnBridge Backend

The LearnBridge backend is a REST API built with Python, Flask, PostgreSQL, Flask-SQLAlchemy, and Marshmallow.

## Technology Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- PostgreSQL
- Pipenv

## Architecture

The backend follows a feature-first architecture.

```text
app/
├── core/
├── extensions/
├── features/
│   ├── auth/
│   ├── users/
│   ├── programs/
│   ├── enrollments/
│   └── learning/
└── __init__.py

```

## Running the Project

### Install dependencies
```pipenv install```

### Run the dev server
```pipenv run python run.py```

### The API Will be accessible at:
```http://127.0.0.1:5000```