# Construction Stock Management System

A comprehensive web-based stock management system for construction materials built with Flask, featuring user authentication, category-based inventory tracking, and print functionality.

## Features

- **User Authentication** - Secure login/signup system with password hashing
- **Category Management** - 6 main construction material categories:
  - 🏠 Godown
  - 🏗️ Double TT
  - 🧱 Slop
  - 🪵 Column
  - 🚧 Phhty
  - 📦 Others
- **Stock Entry System** - Add, view, delete stock entries with auto-generated serial numbers
- **Print Functionality** - Print individual entries or complete category reports
- **Responsive Design** - Works on desktop and mobile devices
- **Modern UI** - Bootstrap 5 + Tailwind CSS with beautiful animations

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Frontend**: Bootstrap 5, Tailwind CSS, Vanilla JavaScript
- **Authentication**: Flask-Login with password hashing
- **Icons**: Bootstrap Icons

## Prerequisites

Before running this project, make sure you have:

- Python 3.11 or higher
- PostgreSQL database
- Visual Studio Code
- Git (optional)

## Setup Instructions for Visual Studio Code

### 1. Clone or Download the Project

```bash
git clone <repository-url>
cd construction-stock-management
```

### 2. Open in Visual Studio Code

```bash
code .
```

Or open Visual Studio Code and use `File > Open Folder` to select the project directory.

### 3. Install Python Extension

Install the Python extension for VS Code if you haven't already:
1. Go to Extensions (Ctrl+Shift+X)
2. Search for "Python"
3. Install the official Python extension by Microsoft

### 4. Set Up Virtual Environment

Open the VS Code terminal (`Ctrl+` ` or View > Terminal`) and run:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install packages manually:

```bash
pip install flask flask-sqlalchemy flask-login gunicorn psycopg2-binary werkzeug
```

### 6. Set Environment Variables

Create a `.env` file in the project root:

```env
SESSION_SECRET=your-secret-key-here-change-in-production
DATABASE_URL=postgresql://username:password@localhost:5432/stock_management
PGHOST=localhost
PGPORT=5432
PGUSER=your_username
PGPASSWORD=your_password
PGDATABASE=stock_management
```

### 7. Set Up Database

Make sure PostgreSQL is running and create the database:

```sql
CREATE DATABASE stock_management;
```

### 8. Configure VS Code Python Interpreter

1. Press `Ctrl+Shift+P` to open command palette
2. Type "Python: Select Interpreter"
3. Select the interpreter from your virtual environment (`venv/Scripts/python.exe` on Windows or `venv/bin/python` on macOS/Linux)

### 9. Run the Application

#### Option A: Using VS Code Debugger (Recommended)

1. Open `main.py` in VS Code
2. Press `F5` or click "Run and Debug" in the sidebar
3. Select "Python" if prompted
4. The application will start with debugging capabilities

#### Option B: Using Terminal

```bash
# Make sure virtual environment is activated
python main.py
```

#### Option C: Using Gunicorn (Production-like)

```bash
gunicorn --bind 0.0.0.0:5000 --reload main:app
```

### 10. Access the Application

Open your browser and navigate to:
```
http://localhost:5000
```

## VS Code Recommended Extensions

For the best development experience, install these extensions:

1. **Python** - Python language support
2. **Pylance** - Python language server
3. **Flask Snippets** - Flask code snippets
4. **HTML CSS Support** - Enhanced HTML/CSS editing
5. **Auto Rename Tag** - Automatically rename paired HTML tags
6. **Prettier** - Code formatter for HTML/CSS/JS
7. **GitLens** - Enhanced Git capabilities

## Project Structure

```
construction-stock-management/
├── app.py                 # Flask application setup
├── main.py               # Application entry point
├── models.py             # Database models
├── routes.py             # Application routes
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── static/
│   ├── css/
│   │   └── style.css     # Custom CSS styles
│   └── js/
│       └── main.js       # Custom JavaScript
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Dashboard
│   ├── category.html     # Category management
│   ├── login.html        # Login page
│   ├── signup.html       # Registration page
│   ├── print_entry.html  # Print single entry
│   └── print_category.html # Print category report
└── README.md            # This file
```

## Usage

### 1. Create Account
1. Navigate to `http://localhost:5000`
2. Click "Sign Up" to create a new account
3. Fill in username, email, and password
4. Click "Create Account"

### 2. Login
1. Use your credentials to log in
2. You'll be redirected to the main dashboard

### 3. Manage Stock
1. Click on any category card to manage stock
2. Use "Add Stock" to create new entries
3. View, print, or delete existing entries
4. Use "Print All" to generate category reports

## Troubleshooting

### Common Issues

**1. Import Errors**
- Make sure virtual environment is activated
- Verify all packages are installed: `pip list`

**2. Database Connection Errors**
- Check PostgreSQL is running
- Verify database credentials in `.env` file
- Ensure database exists

**3. Port Already in Use**
- Change port in `main.py`: `app.run(host="0.0.0.0", port=5001, debug=True)`

**4. Template Not Found**
- Ensure all template files exist in `templates/` directory
- Check file names match exactly (case-sensitive)

### VS Code Debugging

Set breakpoints by clicking in the gutter next to line numbers. Use the debug console to inspect variables and execute Python code.

## Development

### Adding New Features

1. **Models**: Add new database models in `models.py`
2. **Routes**: Add new routes in `routes.py`
3. **Templates**: Create new HTML templates in `templates/`
4. **Styles**: Add custom CSS in `static/css/style.css`
5. **Scripts**: Add JavaScript in `static/js/main.js`

### Database Migrations

When you modify models, restart the application to automatically create tables:

```bash
python main.py
```

## Deployment

For production deployment:

1. Set `DEBUG=False` in production
2. Use a production WSGI server like Gunicorn
3. Set strong `SESSION_SECRET`
4. Use environment variables for sensitive data
5. Configure PostgreSQL for production

## Built With

**dnldynamicsolutions.com**

## License

This project is built for educational and commercial use.

## Support

For support or questions, contact the development team.