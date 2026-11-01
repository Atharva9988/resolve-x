# ResolveX

**A Multi-Tenant Helpdesk and Ticket Management System**

ResolveX is a backend-focused helpdesk platform designed to help organizations manage customer support requests efficiently.

### Current Tech Stack

- Python
- Django 6.1
- Django REST Framework
- PostgreSQL
- Simple JWT
- Psycopg

### Planned Features

- Custom user authentication
- Role-based access control (RBAC)
- Multi-tenant organization management
- Ticket creation and management
- Ticket priorities and status tracking
- Comments and internal notes
- Notifications
- Analytics and reporting
- Background task processing using Celery and Redis

### Project Status

<text color="success" inline>🟢</text> Initial Django project setup completed.

PostgreSQL database connected and custom user model in development.

### Getting Started

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   `pip install -r requirements.txt`

4. Create a `.env` file and configure `DB_PASSWORD`.
5. Run migrations:

   `python manage.py migrate`

6. Start the development server:

   `python manage.py runserver`

### Author

Atharva Thorve