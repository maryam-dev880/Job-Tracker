# JobTracker

JobTracker is a Django REST Framework based backend application for tracking job applications, interview rounds, and application statistics. It helps job seekers organize their job search process — from tracking applied companies to monitoring interview stages and overall progress.

## Features

- Full CRUD API for Companies, Applications, and Interview Rounds
- Token-based and Session-based Authentication
- Filtering applications by status and company
- Custom statistics endpoint showing application counts by status
- Django Admin panel for easy data management
- Bootstrap-powered frontend with an applications list view and a stats dashboard

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** SQLite
- **Authentication:** Token Authentication, Session Authentication
- **Filtering:** django-filter
- **Frontend:** Django Templates, Bootstrap 5

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/company/` | CRUD operations for companies |
| `/application/` | CRUD operations for job applications |
| `/interviewround/` | CRUD operations for interview rounds |
| `/application/stats/` | Returns application statistics (total, applied, interview, offer, reject counts) |
| `/api-token-auth/` | Obtain authentication token via username/password |

## Frontend Pages

| Page | URL |
|------|-----|
| Applications List | `/applications-page/` |
| Stats Dashboard | `/dashboard-page/` |

## Setup Instructions

1. Clone the repository
   ```
   git clone <repository-url>
   ```

2. Create and activate a virtual environment
   ```
   python -m venv venv
   venv\Scripts\Activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations
   ```
   python manage.py migrate
   ```

5. Create a superuser
   ```
   python manage.py createsuperuser
   ```

6. Run the development server
   ```
   python manage.py runserver
   ```

7. Access the application
   - Admin Panel: `http://127.0.0.1:8000/admin/`
   - Applications Page: `http://127.0.0.1:8000/applications-page/`
   - Dashboard: `http://127.0.0.1:8000/dashboard-page/`

## Author

Maryam — [GitHub](https://github.com/maryam-dev880)