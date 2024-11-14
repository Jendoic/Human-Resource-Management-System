# Human Resource Management System (HRMS)

A comprehensive Human Resource Management System built using Django REST Framework. This system streamlines HR processes such as payroll, performance management, leave requests, training and development, and notifications.

## Project Overview

The HRMS API facilitates effective management of employee data and automates many aspects of HR management, including payroll processing, performance tracking, training and development, leave management, and notifications. This project is modular and scalable, making it suitable for both small and large teams.

### Key Features

1. **Employee Management**  
   Manage employee records, including personal details, job role, and department.

2. **Payroll System**  
   Automates payroll calculations with features to process payroll monthly, manually, and provides tracking of salary and deductions.

3. **Performance Management**  
   - Define performance goals for employees.
   - Provide feedback and track performance reviews.
   - Facilitate continuous performance tracking through goal setting and review comments.

4. **Training and Development**  
   Tracks employee development through training courses, certifications, and progress monitoring.

5. **Leave Requests and Approvals**  
   Allows employees to submit leave requests and managers to approve or reject them.

6. **Notifications and Email Alerts**  
   Sends notifications and emails to employees regarding important events, using Celery for task scheduling and Django signals for real-time alerts.

7. **Reports and Analytics**  
   Generate insights and reports, including attendance, payroll summaries, and performance reviews.

## Technologies Used

- **Django** & **Django REST Framework**: Backend API
- **Celery**: Task scheduling and automation for payroll and notifications
- **Redis**: Broker for Celery tasks
- **PostgreSQL**: Primary database
- **JWT Authentication**: Secures API endpoints

## Installation and Setup

### Prerequisites

- Python 3.x
- Docker
- Redis (optional, for Celery setup)

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Jendoic/Human-Resource-Management-System.git
    cd Human-Resource-Management-System
    ```

2. **Install Dependencies**

    Set up a virtual environment and install dependencies:

    ```bash
    python3 -m venv env
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Environment Variables**

    Create a `.env` file in the project root and add the following variables:

    ```plaintext
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://your_database_url
    REDIS_URL=redis://localhost:6379/0
    ```

4. **Run Migrations**

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Server**

    ```bash
    python manage.py runserver
    ```


## API Endpoints

### Employee Management

- **GET /api/employees/** - List all employees
- **POST /api/employees/** - Create a new employee
- **GET /api/employees/<id>/** - Retrieve, update, or delete an employee

### Payroll Management

- **POST /api/payroll/process/** - Process payroll for the current or specified period
- **GET /api/payroll/records/** - List payroll records

### Performance Management

- **GET /api/performance/goals/** - List all performance goals
- **POST /api/performance/goals/** - Set new goals for an employee
- **GET /api/performance/reviews/** - Retrieve performance reviews and comments
- **POST /api/performance/reviews/** - Submit feedback for an employee

### Training and Development

- **GET /api/training/courses/** - List training courses
- **POST /api/training/courses/** - Register employees for training
- **PATCH /api/training/progress/** - Log training progress

### Leave Requests

- **POST /api/leaves/request/** - Submit a leave request
- **PATCH /api/leaves/approve/** - Approve or deny leave requests

## Task Scheduling

Celery tasks are used for automated payroll processing and sending notifications.

1. **Starting Celery**

    ```bash
    celery -A core worker -l info
    ```

2. **Starting Celery Beat for Scheduling**

    ```bash
    celery -A core beat -l info
    ```

## Testing

Tests ensure each endpoint functions as expected. Run the tests with:

```bash
python manage.py test
```

## Future Enhancements

- **Advanced Reporting**: Extend reports to include filters for attendance, performance, and payroll summaries.
- **Real-Time Notifications**: Integrate WebSocket-based notifications for immediate feedback.
- **Role-Based Access Control**: Customize permissions based on roles (e.g., HR, Manager, Employee).



## Contributing

Contributions are welcome! Please submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License.

