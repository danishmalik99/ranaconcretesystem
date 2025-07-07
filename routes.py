from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app, db
from models import StockEntry

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
    return render_template('index.html', categories=CATEGORIES)

@app.route('/category/<category_name>')
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
def print_entry(serial_no):
    """Print a single stock entry"""
    entry = StockEntry.query.get_or_404(serial_no)
    category_info = CATEGORIES[entry.category]
    
    return render_template('print_entry.html', 
                         entry=entry, 
                         category_info=category_info)

@app.route('/print_category/<category_name>')
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
