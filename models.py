from app import db
from datetime import datetime

class StockEntry(db.Model):
    __tablename__ = 'stock_entries'
    
    CATEGORY_CHOICES = [
        ('godown', 'Godown'),
        ('double_tt', 'Double TT'),
        ('slop', 'Slop'),
        ('column', 'Column'),
        ('phhty', 'Phhty'),
        ('others', 'Others'),
    ]
    
    serial_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(20), nullable=False)
    size = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    product_details = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<StockEntry {self.serial_no}: {self.category}>'
    
    def to_dict(self):
        return {
            'serial_no': self.serial_no,
            'category': self.category,
            'size': self.size,
            'quantity': self.quantity,
            'product_details': self.product_details,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
