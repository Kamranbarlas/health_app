# health_app
## Patient Counseling Appointment System
A RESTful API-based CRUD application developed using Django, Django Rest Framework, and SQLite database.

Project Description
This system is designed to manage patients, counselors, and appointments. It provides APIs to list active patients, active counselors, and appointments. Further features include searching for appointments of a specific patient or counselor and filtering appointments within a date range.

Schemas
Patient

Id (Unique Identifier)
Name (String)
Email (Unique Identifier)
Password (String)
Is_active (Boolean)
Counselor

Id (Unique Identifier)
Name (String)
Email (Unique Identifier)
Password (String)
Is_active (Boolean)
Appointment

Id (Unique Identifier)
Patient (Foreign key to Patient)
Counselor (Foreign key to Counselor)
Appointment_Date (Datetime)
Is_active (Boolean)
# Features
List all active patients, active counselors, and active appointments.
Fetch all appointments for a specific patient or counselor.
List active appointments between a date range, sorted by date in descending order.
Admin Dashboard to manage Patients, Counselors, and Appointments with search capabilities.

# Setup & Installation
git clone repo_url

cd healthapp

pip install -r requirements.txt

python manage.py migrate

git clone repo url


