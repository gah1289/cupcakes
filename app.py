"""Flask app for Cupcakes"""
from flask import Flask, render_template, redirect,jsonify, request
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SECRET_KEY'] = 'HopperLikesPupcakes'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False

# debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def index_page():
    '''Shows main page'''
    cupcakes=Cupcake.query.all()
    return render_template('index.html', cupcakes=cupcakes)

@app.route('/api/cupcakes')
def list_cupcake():
    '''Returns JSON with all cupcakes'''
    all_cupcakes=[cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<id>')
def get_cupcake(id):
    '''Returns JSON for one cupcake'''
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    '''Creates a new cupcake'''
    new_cupcake=Cupcake(flavor=request.json["flavor"], image=request.json["image"], rating=request.json["rating"], size=request.json["size"])
    db.session.add(new_cupcake)
    db.session.commit()
    response_json=jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)

@app.route('/api/cupcakes/<id>', methods=["PATCH"])
def update_cupcake(id):
    '''update cupcake'''
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor=request.json.get('flavor', cupcake.flavor)
    cupcake.image=request.json.get('image', cupcake.image)
    cupcake.rating=request.json.get('rating', cupcake.rating)
    cupcake.size=request.json.get('size', cupcake.size)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<id>', methods=["DELETE"])
def delete_cupcake(id):
    '''Delete cupcake'''
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")


