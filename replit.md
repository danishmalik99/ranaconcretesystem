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
- **SQLite**: Default database (configurable via environment variable)
- **Database URL**: Configurable through `DATABASE_URL` environment variable

## Deployment Strategy

### Environment Configuration
- **Secret Key**: Configurable via `SESSION_SECRET` environment variable
- **Database URL**: Configurable via `DATABASE_URL` environment variable
- **Debug Mode**: Enabled for development (should be disabled in production)

### Application Setup
- **Host**: Configured to run on `0.0.0.0` for external access
- **Port**: Default port 5000
- **Proxy Support**: ProxyFix middleware for production deployment behind proxies

### Database Management
- **Auto-creation**: Database tables are automatically created on application startup
- **Connection Pooling**: Configured with pool recycling and pre-ping for reliability

## Changelog
- July 07, 2025. Initial setup

## User Preferences

Preferred communication style: Simple, everyday language.