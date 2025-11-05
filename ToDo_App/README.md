# ToDo App

A modern task management application with Django.

## Features

- Task creation and management
- User authentication
- Task status tracking (Pending, In Progress, Completed)
- Modern dark UI
- Responsive design

## Structure

```
tasks/             # Main app
static/            # CSS and JS
templates/         # HTML templates
db.sqlite3         # Database
manage.py          # Django CLI
```

## URLs

- `/` - Home
- `/login/` - Login
- `/signup/` - Sign up
- `/dashboard/` - Task dashboard
- `/add/` - Add task
- `/edit/<id>/` - Edit task
- `/delete/<id>/` - Delete task

## Tech

- Django 5.x
- SQLite
- Custom CSS/JS
