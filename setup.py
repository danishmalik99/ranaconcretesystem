#!/usr/bin/env python3
"""
Setup script for Construction Stock Management System
Run this to set up the project dependencies and database
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    packages = [
        'flask==3.0.0',
        'flask-sqlalchemy==3.1.1', 
        'flask-login==0.6.3',
        'werkzeug==3.0.1',
        'gunicorn==21.2.0',
        'psycopg2-binary==2.9.9',
        'email-validator==2.1.0',
        'PyJWT==2.8.0',
        'SQLAlchemy==2.0.23'
    ]
    
    print("Installing required packages...")
    for package in packages:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"✓ Installed {package}")
        except subprocess.CalledProcessError:
            print(f"✗ Failed to install {package}")
    
    print("\nAll packages installed successfully!")

def create_env_file():
    """Create a sample .env file"""
    env_content = """# Environment variables for Construction Stock Management System
SESSION_SECRET=change-this-secret-key-in-production-to-something-secure
DATABASE_URL=postgresql://username:password@localhost:5432/stock_management

# PostgreSQL connection details
PGHOST=localhost
PGPORT=5432
PGUSER=your_username
PGPASSWORD=your_password
PGDATABASE=stock_management

# Development settings
FLASK_ENV=development
FLASK_DEBUG=True
"""
    
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✓ Created .env file with sample configuration")
        print("⚠️  Please update the database credentials in .env file")
    else:
        print("✓ .env file already exists")

def print_instructions():
    """Print setup completion instructions"""
    print("\n" + "="*50)
    print("SETUP COMPLETE!")
    print("="*50)
    print("\nNext steps:")
    print("1. Update database credentials in .env file")
    print("2. Make sure PostgreSQL is running")
    print("3. Create database: CREATE DATABASE stock_management;")
    print("4. Run the application: python main.py")
    print("5. Open browser to: http://localhost:5000")
    print("\nFor Visual Studio Code:")
    print("1. Open project folder in VS Code")
    print("2. Install Python extension")
    print("3. Select Python interpreter from virtual environment")
    print("4. Press F5 to run with debugging")
    print("\nBuilt with dnldynamicsolutions.com")

if __name__ == "__main__":
    print("Construction Stock Management System - Setup")
    print("Built with dnldynamicsolutions.com\n")
    
    install_requirements()
    create_env_file()
    print_instructions()