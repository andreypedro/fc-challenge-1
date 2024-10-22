# fc-challenge-1

# Project Setup Guide

This guide will walk you through setting up and running the project, from installation to running it in your browser.

## Prerequisites

- [ASDF](https://asdf-vm.com/) version manager installed
- Docker and Docker Compose installed

## Getting Started

### 1. Install Python

To ensure you're using the correct version of Python, install it using `asdf`:

```bash
asdf install python 3.12.6
```

### 2. Set Up the Virtual Environment

We will use pipenv to create a virtual environment specific to this project. To activate the environment, run:

```bash
pipenv shell
```

### 3. Install Django

Once inside the virtual environment, install Django:

```bash
pip install django
```

#### 4. Apply Database Migrations

Run the following command to apply any existing migrations to the database:

```bash
python manage.py migrate
```

### 5. Create an Admin User

To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

### 6. Run the Application

Start the development server to verify everything is set up correctly:

```bash
python manage.py runserver
```

Now, open your browser and go to http://127.0.0.1:8000/ to see the Django welcome page.

### 7. Accessing Admin

To access the Admin, in your browser, go to:

```
http://127.0.0.1:8000/admin
```
