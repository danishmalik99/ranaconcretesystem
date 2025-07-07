from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from app import app, db
from models import StockEntry, User
from sqlalchemy import extract

# Category configuration with colors and icons
CATEGORIES = {
    'godown': {
        'name': 'Godown',
        'icon': '🏠',
        'color': 'bg-blue-500',
        'gradient': 'from-blue-400 to-blue-600'
    },
    'double_tt': {
        'name': 'Double TT',
        'icon': '🏗️',
        'color': 'bg-green-500',
        'gradient': 'from-green-400 to-green-600'
    },
    'slop': {
        'name': 'Slop',
        'icon': '🧱',
        'color': 'bg-red-500',
        'gradient': 'from-red-400 to-red-600'
    },
    'column': {
        'name': 'Column',
        'icon': '🪵',
        'color': 'bg-yellow-500',
        'gradient': 'from-yellow-400 to-yellow-600'
    },
    'phhty': {
        'name': 'Phhty',
        'icon': '🚧',
        'color': 'bg-purple-500',
        'gradient': 'from-purple-400 to-purple-600'
    },
    'others': {
        'name': 'Others',
        'icon': '📦',
        'color': 'bg-gray-500',
        'gradient': 'from-gray-400 to-gray-600'
    }
}

@app.route('/')
def index():
    """Landing page with category cards"""
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    
    # Calculate statistics for each category
    category_stats = {}
    for category_key in CATEGORIES.keys():
        entries = StockEntry.query.filter_by(category=category_key).all()
        category_stats[category_key] = {
            'total_items': len(entries),
            'total_quantity': sum(entry.quantity for entry in entries),
            'last_entry': entries[-1].timestamp.strftime('%m/%d') if entries else 'Never'
        }
    
    # Overall statistics
    total_entries = StockEntry.query.count()
    from datetime import datetime
    current_month = datetime.now().month
    current_year = datetime.now().year
    monthly_entries = StockEntry.query.filter(
        extract('month', StockEntry.timestamp) == current_month,
        extract('year', StockEntry.timestamp) == current_year
    ).count()
    
    # Last entry date
    last_entry = StockEntry.query.order_by(StockEntry.timestamp.desc()).first()
    last_entry_date = last_entry.timestamp.strftime('%m/%d') if last_entry else 'Never'
    
    return render_template('index.html', 
                         categories=CATEGORIES,
                         category_stats=category_stats,
                         total_entries=total_entries,
                         monthly_entries=monthly_entries,
                         last_entry_date=last_entry_date)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            flash('Please enter both username and password', 'error')
            return render_template('login.html')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Signup page"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if not all([username, email, password, confirm_password]):
            flash('Please fill in all fields', 'error')
            return render_template('signup.html')
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('signup.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters long', 'error')
            return render_template('signup.html')
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return render_template('signup.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'error')
            return render_template('signup.html')
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        
        try:
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Error creating account. Please try again.', 'error')
    
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    """Logout user"""
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('login'))

@app.route('/category/<category_name>')
@login_required
def category_view(category_name):
    """View stock entries for a specific category"""
    if category_name not in CATEGORIES:
        flash('Invalid category', 'error')
        return redirect(url_for('index'))
    
    entries = StockEntry.query.filter_by(category=category_name).order_by(StockEntry.timestamp.desc()).all()
    category_info = CATEGORIES[category_name]
    
    return render_template('category.html', 
                         entries=entries, 
                         category=category_name,
                         category_info=category_info)

@app.route('/add_stock', methods=['POST'])
@login_required
def add_stock():
    """Add new stock entry"""
    try:
        category = request.form.get('category')
        size = request.form.get('size')
        quantity = request.form.get('quantity')
        product_details = request.form.get('product_details', '')
        
        if not all([category, size, quantity]):
            flash('Size and Quantity are required fields', 'error')
            return redirect(url_for('category_view', category_name=category))
        
        if category not in CATEGORIES:
            flash('Invalid category', 'error')
            return redirect(url_for('index'))
        
        # Create new stock entry
        new_entry = StockEntry(
            category=category,
            size=size,
            quantity=int(quantity),
            product_details=product_details
        )
        
        db.session.add(new_entry)
        db.session.commit()
        
        flash(f'Stock entry added successfully! Serial No: {new_entry.serial_no}', 'success')
        
    except ValueError:
        flash('Invalid quantity. Please enter a valid number.', 'error')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding stock entry: {str(e)}', 'error')
    
    return redirect(url_for('category_view', category_name=category))

@app.route('/delete_stock/<int:serial_no>')
@login_required
def delete_stock(serial_no):
    """Delete a stock entry"""
    try:
        entry = StockEntry.query.get_or_404(serial_no)
        category = entry.category
        
        db.session.delete(entry)
        db.session.commit()
        
        flash(f'Stock entry #{serial_no} deleted successfully', 'success')
        
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting stock entry: {str(e)}', 'error')
    
    return redirect(url_for('category_view', category_name=category))

@app.route('/print_entry/<int:serial_no>')
@login_required
def print_entry(serial_no):
    """Print a single stock entry"""
    entry = StockEntry.query.get_or_404(serial_no)
    category_info = CATEGORIES[entry.category]
    
    return render_template('print_entry.html', 
                         entry=entry, 
                         category_info=category_info)

@app.route('/print_category/<category_name>')
@login_required
def print_category(category_name):
    """Print all entries for a category"""
    if category_name not in CATEGORIES:
        flash('Invalid category', 'error')
        return redirect(url_for('index'))
    
    entries = StockEntry.query.filter_by(category=category_name).order_by(StockEntry.timestamp.desc()).all()
    category_info = CATEGORIES[category_name]
    
    return render_template('print_category.html', 
                         entries=entries, 
                         category=category_name,
                         category_info=category_info)

@app.template_filter('format_datetime')
def format_datetime(value):
    """Format datetime for display"""
    if value:
        return value.strftime('%Y-%m-%d %H:%M:%S')
    return ''

@app.template_filter('format_date')
def format_date(value):
    """Format date for display"""
    if value:
        return value.strftime('%Y-%m-%d')
    return ''
