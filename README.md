# 🎓 LearnBridge

> A modern, centralized Mobile Learning Management System (LMS) designed to bridge the gap between education providers and eager learners.

LearnBridge is a mobile learning platform that enables learners to discover, explore, enroll in, and track professional training programs while providing administrators with the tools required to manage programs, learners, enrollments, and educational content.

The project is being built as a real-world full-stack application using **Flutter** for the mobile client, **Flask** for the backend API, and **PostgreSQL** for persistent data storage.

The goal of LearnBridge is not only to provide a functional learning experience, but also to serve as a practical demonstration of building a production-oriented application with a clear separation between frontend, backend, database, authentication, business logic, and data serialization.

---

## Project Overview

Many educational institutions and training providers still rely on fragmented websites, social media platforms, or manual communication to advertise and manage training programs.

This creates friction for learners who want to:

* Discover relevant training programs
* Understand program requirements
* Enroll in available programs
* Track their learning progress
* Manage their profiles and learning history

LearnBridge aims to centralize these activities into a single mobile learning experience.

The platform provides two primary user experiences:

* **Learners**, who discover and participate in training programs.
* **Administrators**, who manage programs and monitor learner activity.

---

## Core Objectives

LearnBridge is designed around the following objectives:

* **Centralized Learning Discovery**
  Provide a unified platform where learners can discover available professional training programs.

* **Simple Enrollment**
  Allow learners to enroll in programs directly from the mobile application.

* **Program Management**
  Provide administrators with tools to create, update, publish, and manage learning programs.

* **Learning Progress Tracking**
  Allow learners to monitor their progress and identify completed learning activities.

* **Structured Learning Experience**
  Organize educational content into programs, courses, modules, and lessons as the platform evolves.

* **Scalable Architecture**
  Build the application using a maintainable, feature-first architecture that can grow as the platform gains more functionality.

---

# 👥 Target Users

## 👨‍🎓 Learners

LearnBridge is designed for learners such as:

* University students
* Recent graduates
* Working professionals
* Job seekers
* Anyone looking to acquire professional skills

### Learner Capabilities

Learners will be able to:

* Register for an account
* Log in securely
* Recover forgotten passwords
* Browse available programs
* Search for programs
* Filter programs by category
* View detailed program information
* Enroll in programs
* Track learning progress
* View completed learning activities
* Manage their profile
* View their enrolled programs
* Log out securely

---

## Administrators

Administrators represent users responsible for managing the learning platform and its educational content.

### Administrator Capabilities

Administrators will be able to:

* Securely access administrative functionality
* Create learning programs
* Update existing programs
* Delete programs
* Publish programs
* Manage program content
* View learner enrollments
* Monitor learner participation

As the platform evolves, administrator functionality may expand into a dedicated administration interface.

---

# Technology Stack

## Mobile Application

| Technology          | Purpose                                                    |
| ------------------- | ---------------------------------------------------------- |
| **Flutter**         | Cross-platform mobile application development              |
| **Dart**            | Programming language used to build the Flutter application |
| **HTTP / REST API** | Communication between the Flutter client and Flask backend |
| **JSON**            | Data exchange format between frontend and backend          |

## Backend

| Technology           | Purpose                                                    |
| -------------------- | ---------------------------------------------------------- |
| **Python**           | Backend programming language                               |
| **Flask**            | Lightweight Python web framework for building the REST API |
| **Flask-SQLAlchemy** | Database ORM and SQLAlchemy integration with Flask         |
| **Marshmallow**      | Data validation, serialization, and deserialization        |
| **PostgreSQL**       | Relational database for persistent application data        |

## Development & Tooling

| Technology | Purpose                                           |
| ---------- | ------------------------------------------------- |
| **Git**    | Version control                                   |
| **GitHub** | Source code hosting and collaboration             |
| **Figma**  | UI/UX design and high-fidelity interface planning |

---

# Architecture

LearnBridge follows a **Feature-First Architecture**.

The primary goal of this architecture is to organize the application around business features rather than grouping every file by technical type.

For example, instead of having one global folder for all models, another for all screens, and another for all services, related functionality is grouped around the feature it belongs to.

This makes the codebase easier to understand, maintain, test, and extend.

The application is divided into two major systems:

```text
                    LEARNBRIDGE
                         │
            ┌────────────┴────────────┐
            │                         │
      Flutter Mobile              Flask API
            │                         │
            │                  ┌──────┴──────┐
            │                  │             │
            │             SQLAlchemy    Marshmallow
            │                  │             │
            │                  └──────┬──────┘
            │                         │
            │                    PostgreSQL
            │
            └──────── HTTP / JSON ────────┘
```

The Flutter application communicates with the Flask backend through HTTP requests.

The Flask backend handles authentication, validation, business logic, authorization, and database operations.

PostgreSQL provides persistent storage for users, programs, enrollments, learning content, and progress data.

---

# Flutter Application Architecture

The Flutter application follows a feature-first structure.

```text
lib/
│
├── core/
│   ├── constants/
│   ├── errors/
│   ├── network/
│   ├── routing/
│   ├── theme/
│   ├── utils/
│   └── widgets/
│
├── features/
│   │
│   ├── auth/
│   │   ├── data/
│   │   ├── domain/
│   │   └── presentation/
│   │
│   ├── home/
│   │   ├── data/
│   │   ├── domain/
│   │   └── presentation/
│   │
│   ├── programs/
│   │   ├── data/
│   │   ├── domain/
│   │   └── presentation/
│   │
│   ├── enrollments/
│   │   ├── data/
│   │   ├── domain/
│   │   └── presentation/
│   │
│   ├── learning/
│   │   ├── data/
│   │   ├── domain/
│   │   └── presentation/
│   │
│   └── profile/
│       ├── data/
│       ├── domain/
│       └── presentation/
│
└── main.dart
```

### Feature Layers

Each feature is organized into logical layers.

### `data/`

Responsible for external data sources and data access.

Examples:

* API clients
* Repository implementations
* Data transfer objects
* JSON serialization
* Remote data sources

### `domain/`

Contains the core business concepts of the feature.

Examples:

* Entities
* Repository contracts
* Business rules
* Use cases

### `presentation/`

Responsible for everything related to the user interface.

Examples:

* Screens
* Widgets
* Controllers
* State management
* UI state

### `core/`

Contains functionality shared across multiple features.

Examples:

* Network configuration
* API client
* Application routing
* Theme configuration
* Error handling
* Shared widgets
* Constants
* Utility functions

---

# Flask Backend Architecture

The Flask backend also follows a feature-oriented structure.

```text
backend/
│
├── app/
│   │
│   ├── core/
│   │   ├── config/
│   │   ├── errors/
│   │   └── security/
│   │
│   ├── extensions/
│   │
│   ├── features/
│   │   │
│   │   ├── auth/
│   │   │   ├── routes.py
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   └── services.py
│   │   │
│   │   ├── users/
│   │   │   ├── routes.py
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   └── services.py
│   │   │
│   │   ├── programs/
│   │   │   ├── routes.py
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   └── services.py
│   │   │
│   │   ├── enrollments/
│   │   │   ├── routes.py
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   └── services.py
│   │   │
│   │   └── learning/
│   │       ├── routes.py
│   │       ├── models.py
│   │       ├── schemas.py
│   │       └── services.py
│   │
│   └── __init__.py
│
├── migrations/
├── tests/
├── config.py
├── requirements.txt
└── run.py
```

The exact structure may evolve as the application grows.

The guiding principle is that functionality belonging to the same business domain should remain close together.

---

# Request & Response Architecture

When a learner interacts with LearnBridge, data flows through multiple layers.

For example, when a learner enrolls in a program:

```text
Learner
   │
   │ Taps "Enroll"
   ▼
Flutter UI
   │
   ▼
Presentation / State
   │
   ▼
Repository
   │
   ▼
HTTP Client
   │
   │ POST /api/v1/enrollments
   ▼
Flask API
   │
   ▼
Authentication
   │
   ▼
Authorization
   │
   ▼
Request Validation
   │
   ▼
Business Logic
   │
   ▼
Flask-SQLAlchemy
   │
   ▼
PostgreSQL
   │
   ▼
Marshmallow Serialization
   │
   ▼
JSON Response
   │
   ▼
Flutter Repository
   │
   ▼
Application State
   │
   ▼
Updated UI
```

This separation allows each part of the system to have a clear responsibility.

---

# Data & Domain Model

The initial LearnBridge domain is expected to grow around the following concepts:

```text
User
 │
 ├───────────────┐
 │               │
 │               ▼
 │          Enrollment
 │               │
 │               ▼
 │             Program
 │               │
 │               ▼
 │             Course
 │               │
 │               ▼
 │             Module
 │               │
 │               ▼
 │             Lesson
 │               │
 │               ▼
 │            Progress
 │
 └────────────── Profile
```

The initial database design will focus on the application's core requirements and evolve as learning functionality becomes more detailed.

Potential core entities include:

* Users
* Profiles
* Programs
* Categories
* Enrollments
* Courses
* Modules
* Lessons
* Learning Progress

Database relationships, constraints, indexes, and business rules will be designed deliberately as each feature is implemented.

---

# Application Navigation Flow

The initial learner navigation flow is:

```text
[Splash Screen]
        ↓
[Login / Register]
        ↓
[Home]
        ↓
[Programs]
        ↓
[Program Details]
        ↓
[Enroll]
        ↓
[My Learning]
        ↓
[Learning Progress]
```

Profile functionality is accessible to authenticated learners.

```text
[Profile]
    ├── View Profile
    ├── Edit Profile
    ├── View Enrolled Programs
    └── Logout
```

---

# User Journeys

## Learner Journey

```text
Register
   ↓
Login
   ↓
Browse Programs
   ↓
Search / Filter
   ↓
View Program Details
   ↓
Enroll
   ↓
Access My Learning
   ↓
Track Learning Progress
   ↓
Complete Learning
```

## Administrator Journey

```text
Login
   ↓
Access Administrative Features
   ↓
Create Program
   ↓
Update Program
   ↓
Publish Program
   ↓
Manage Programs
   ↓
View Learner Enrollments
   ↓
Manage Platform Content
```

---

# Core Feature Blueprint

## Authentication

The authentication system will provide:

* User registration
* Secure login
* Password recovery
* Logout
* Authentication state management
* Protected API endpoints
* Role-based authorization

---

## Home

The home experience will provide learners with:

* Personalized user experience
* Featured programs
* Popular courses
* Program categories
* Recent enrollments
* Quick access to learning activity

---

## Programs

Learners will be able to:

* Browse available programs
* Search programs
* Filter programs by category
* View program listings
* Open individual program details

---

## Program Details

Program details will include:

* Program description
* Instructor information
* Duration
* Requirements
* Enrollment availability
* Enrollment action

---

## My Learning

Learners will be able to:

* View enrolled programs
* Access their learning content
* Track progress
* View completed learning activities
* Identify completed programs

---

## Profile

Learners will be able to:

* View their profile
* Edit personal information
* View enrolled programs
* Manage account settings
* Log out

---

# Testing Strategy

Testing will be introduced alongside feature development rather than being treated as a final step.

The project will eventually include:

### Flutter Testing

* Widget tests
* Unit tests
* Repository tests
* State management tests
* Integration tests

### Flask Testing

* API endpoint tests
* Authentication tests
* Authorization tests
* Validation tests
* Service-layer tests
* Database interaction tests

### Feature Testing

Each feature should validate:

```text
Happy Path
    +
Invalid Input
    +
Unauthorized Access
    +
Forbidden Access
    +
Missing Resources
    +
Database Failures
    +
Edge Cases
```

The objective is to build confidence that each feature works correctly across both the mobile client and backend API.

---

# Roadmap

LearnBridge is intended to evolve beyond the initial MVP.

Potential future capabilities include:

### Certificates

Generate certificates when learners successfully complete programs.

### Push Notifications

Provide real-time notifications for learning activities, announcements, and program updates.

### Payments

Support paid programs and premium learning experiences through payment providers such as M-Pesa and Stripe.

### Offline Learning

Allow learners to access selected learning content during periods of limited connectivity and synchronize progress when connectivity returns.

### Video Learning

Introduce video-based lessons with playback and learning progress tracking.

### Dark Mode

Provide system-aware and user-controlled application themes.

### Instructor Communication

Introduce real-time communication between learners and instructors.

### Dedicated Administration

Expand administrative functionality into a dedicated web or mobile administration interface for managing programs, learners, enrollments, and platform content.

---

# Local Development

## Prerequisites

Before running the project locally, ensure you have:

* [Flutter SDK](https://docs.flutter.dev/get-started/install)
* [Dart SDK](https://dart.dev/get-started)
* Python 3.x
* PostgreSQL
* Git
* An Android/iOS emulator or physical development device

The exact supported versions will be documented as the project stabilizes.

---

## Flutter Application

Install Flutter dependencies:

```bash
flutter pub get
```

Analyze the project:

```bash
flutter analyze
```

Run the application:

```bash
flutter run
```

---

## Flask Backend

The backend setup will include:

1. Creating a Python virtual environment
2. Installing Python dependencies
3. Configuring environment variables
4. Creating the PostgreSQL database
5. Running database migrations
6. Starting the Flask development server

Example workflow:

```bash
python -m venv .venv
```

Activate the virtual environment.

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the backend:

```bash
flask run
```

The exact commands and environment configuration will be documented as the backend foundation is finalized.

---

# Environment Configuration

Sensitive configuration should never be committed directly to source control.

The application will use environment variables for values such as:

```text
DATABASE_URL
SECRET_KEY
JWT_SECRET_KEY
FLASK_ENV
```

A local `.env` file may be used during development.

Example:

```text
DATABASE_URL=postgresql://username:password@localhost:5432/learnbridge
SECRET_KEY=your-development-secret
JWT_SECRET_KEY=your-development-jwt-secret
```

> Never commit real credentials, production secrets, API keys, or database passwords to GitHub.

---

# 🤝 Development Philosophy

LearnBridge is being developed as a practical full-stack learning project with an emphasis on understanding how modern applications actually work.

The development process prioritizes:

* Understanding before abstraction
* Feature-first organization
* Clear separation of responsibilities
* API-driven development
* Strong database fundamentals
* Secure authentication
* Explicit validation
* Automated testing
* Maintainable code
* Incremental feature development

The goal is to understand the entire application lifecycle:

```text
Idea
  ↓
Requirements
  ↓
Domain Design
  ↓
Database Design
  ↓
Backend API
  ↓
Flutter Client
  ↓
Testing
  ↓
Deployment
  ↓
Monitoring
  ↓
Iteration
```

---

# 📚 Learning Objectives

While building LearnBridge, the project will be used to develop practical mastery of:

### Flutter & Dart

* Dart fundamentals
* Flutter widgets
* State management
* Navigation
* Forms and validation
* Networking
* JSON serialization
* Repository patterns
* Feature-first architecture
* Error handling
* Local persistence
* Testing

### Python & Flask

* Python fundamentals
* Flask application architecture
* Application factories
* Blueprints
* REST API design
* Request handling
* Authentication
* Authorization
* Validation
* Business logic
* Error handling
* Testing

### PostgreSQL & SQLAlchemy

* Relational database design
* SQL fundamentals
* Tables and relationships
* Primary and foreign keys
* Constraints
* Indexes
* Transactions
* SQLAlchemy ORM
* Flask-SQLAlchemy
* Database migrations

### API Development

* HTTP
* REST
* JSON
* HTTP methods
* Status codes
* Authentication
* Authorization
* API versioning
* Pagination
* Filtering
* Search
* Error responses

The long-term objective is to develop the ability to design and implement complete, maintainable full-stack applications independently.

---

# 📁 Repository Structure

At a high level, LearnBridge is organized into:

```text
learnbridge/
│
├── mobile/              # Flutter mobile application
│
├── backend/             # Flask REST API
│
├── docs/                # Architecture and project documentation
│
├── .gitignore
└── README.md
```

The repository structure may evolve as the application grows.

---

# 📝 Project Details

* **Project:** LearnBridge
* **Project Type:** Mobile Learning Management System
* **Frontend:** Flutter / Dart
* **Backend:** Python / Flask
* **Database:** PostgreSQL
* **ORM:** Flask-SQLAlchemy / SQLAlchemy
* **Serialization & Validation:** Marshmallow
* **Architecture:** Feature-First Architecture
* **Version Control:** Git / GitHub
* **Design:** Figma
* **Project Context:** Flutter Development Internship
* **Author:** Adams Yeswa

---

## 🚧 Project Status

**Currently in active development.**

The initial project foundation has been established. Development is progressing feature by feature, beginning with the backend architecture, database foundation, API development, and Flutter integration.

The application will evolve incrementally from a functional MVP into a more complete learning platform.

---

> **LearnBridge**
> *Building a bridge between learners and opportunity.*
