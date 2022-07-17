"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app=app
    db.init_app(app)

class Cupcake(db.Model):
    '''Cupcake model, part one'''

    __tablename__="cupcakes"

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    flavor=db.Column(db.Text, nullable=False)
    size=db.Column(db.Text, nullable=False)
    rating=db.Column(db.Float, nullable=False)
    image=db.Column(db.Text, nullable=False, default='https://tinyurl.com/demo-cupcake')

    def serialize(self):
        '''Returns dict of cupcake'''
        return {
            'id': self.id,
            'flavor':self.flavor,
            'size':self.size,
            'rating':self.rating,
            'image':self.image
        }

    def __repr__(self):
        '''return flavor and id of cupcake'''
        return f"<Cupcake> {self.id} flavor: {self.flavor} size: {self.size}>"