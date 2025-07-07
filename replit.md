# Construction Stock Management System

## Overview

This is a Flask-based web application for managing construction materials inventory. The system provides a dashboard-style interface for tracking stock across six main categories of construction materials: Godown, Double TT, Slop, Column, Phhty, and Others. Each category has its own dedicated management interface for adding and viewing stock entries.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Database**: SQLAlchemy ORM with SQLite as default database
- **Application Structure**: Modular design with separate files for models, routes, and application configuration
- **Middleware**: ProxyFix for handling proxy headers in production environments

### Frontend Architecture
- **Styling**: Hybrid approach using Bootstrap 5 and Tailwind CSS
- **Template Engine**: Jinja2 (Flask's default templating engine)
- **JavaScript**: Vanilla JavaScript with Bootstrap components
- **Responsive Design**: Mobile-first approach with responsive grid layouts

### Database Schema
- **Single Entity Model**: StockEntry table with the following fields:
  - `serial_no`: Primary key (auto-increment)
  - `category`: String field for material category
  - `size`: String field for material size specifications
  - `quantity`: Integer field for stock quantity
  - `product_details`: Optional text field for additional details
  - `timestamp`: DateTime field (auto-populated)

## Key Components

### Models (models.py)
- **StockEntry**: Main data model representing individual stock entries
- **Category Validation**: Predefined category choices ensuring data consistency
- **Serialization**: Built-in `to_dict()` method for JSON responses

### Routes (routes.py)
- **Dashboard Route**: Main landing page displaying category cards
- **Category Management**: Individual category views for stock management
- **CRUD Operations**: Create, read, update, and delete stock entries
- **Category Configuration**: Centralized category metadata including colors and icons

### Templates
- **Base Template**: Shared layout with navigation and common styling
- **Index Template**: Dashboard with category cards and statistics
- **Category Template**: Individual category management interface

### Static Assets
- **CSS**: Custom styling for enhanced visual appeal
- **JavaScript**: Form validation and user interaction handling

## Data Flow

1. **User Access**: Users start at the main dashboard displaying all categories
2. **Category Selection**: Users click on category cards to access specific stock management
3. **Stock Entry**: Users add new stock entries through modal forms
4. **Data Persistence**: Form data is validated and stored in SQLite database
5. **Display**: Stock entries are retrieved and displayed in responsive tables
6. **Feedback**: Success/error messages provide user feedback

## External Dependencies

### Python Packages
- **Flask**: Web framework
- **Flask-SQLAlchemy**: Database ORM
- **Werkzeug**: WSGI utilities and middleware

### Frontend Libraries
- **Bootstrap 5**: UI component framework
- **Tailwind CSS**: Utility-first CSS framework
- **Bootstrap Icons**: Icon library

### Database
- **SQLite3**: Simple file-based database (stock_management.db)
- **Auto-creation**: Database file is created automatically on first run

## Deployment Strategy

### Environment Configuration
- **Secret Key**: Configurable via `SESSION_SECRET` environment variable (optional, has default)
- **Database**: SQLite3 file-based database (stock_management.db)
- **Debug Mode**: Enabled for development (should be disabled in production)

### Application Setup
- **Host**: Configured to run on `0.0.0.0` for external access
- **Port**: Default port 5000
- **Proxy Support**: ProxyFix middleware for production deployment behind proxies

### Database Management
- **Auto-creation**: Database tables are automatically created on application startup
- **Connection Pooling**: Configured with pool recycling and pre-ping for reliability

## Recent Changes

### July 07, 2025 - Fixed Dashboard Statistics & Category Counts
- **Fixed Quick Overview section** - Now displays real-time statistics instead of "--"
- **Fixed Category Cards** - Now showing actual entry counts and last entry dates
- **Improved Dashboard Route** - Added proper statistics calculation for all categories
- **Database Integration** - Statistics now update automatically when entries are added
- **SQLite3 Database** - Confirmed working perfectly with automatic table creation
- **Authentication System** - Fully functional with protected routes and user management
- **Category Navigation** - All category cards now link properly to their respective pages
- **Real-time Data** - Dashboard shows current month entries, total entries, and category breakdowns

### July 07, 2025 - Database Migration & Authentication System Update
- **Switched from PostgreSQL to SQLite3** for easier setup and deployment
- Updated all configuration files to use SQLite3 database
- Removed PostgreSQL dependencies from setup instructions
- Added complete user authentication system with Flask-Login
- Created beautiful login and signup pages with form validation
- Implemented secure password hashing and user registration
- Protected all stock management routes with login requirements
- Added user dropdown menu with logout functionality
- Updated all branding to include "dnldynamicsolutions.com"
- Created comprehensive README.md with Visual Studio Code setup instructions
- Added setup.py script for easy project installation

### July 07, 2025 - Initial Setup
- Built Flask-based construction stock management system
- Implemented 6 category dashboard with responsive design
- Created stock entry system with print functionality
- Integrated Bootstrap 5 + Tailwind CSS for modern UI

## Deployment Information

The system now requires user authentication before accessing any stock management features. Users must create an account and log in to access the dashboard. All pages display "Built with dnldynamicsolutions.com" branding.

## User Preferences

Preferred communication style: Simple, everyday language.