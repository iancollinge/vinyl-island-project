import os
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "shhh it's a secret"

# SqlAlchemy Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# End SqlAlchemy

# Creating model table for our CRUD database

class Data (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(200))
    title = db.Column(db.String(200))
    label = db.Column(db.String(100))
    format = db.Column(db.String(6))
    year = db.Column(db.String(4))
    condition = db.Column(db.String(4))
    
    
    def __init__ (self, artist, title, label, format, year, condition):
        self.artist = artist
        self.title = title
        self.label = label
        self.format = format
        self.year = year
        self.condition = condition

# End model

# This is the index route where we query on all our data

@app.route('/')
def index():
    all_data = Data.query.all()
 
    return render_template("index.html", collection = all_data)
 
# This route is for adding new items to collection via html forms

@app.route('/insert', methods = ['POST'])
def insert():
    
    if request.method == 'POST':
        
        artist = request.form['artist']
        title = request.form['title']
        label = request.form['label']
        format = request.form['format']
        year = request.form['year']
        condition = request.form['condition']
        
        my_data = Data (artist, title, label, format, year, condition)
        db.session.add (my_data)
        db.session.commit()
        
        flash ("New item added successfully. Your collection is growing!")
        
        return redirect (url_for('index'))
    
# This is our update route to edit existing items in the collection

@app.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
 
        my_data.artist = request.form['artist']
        my_data.title = request.form['title']
        my_data.label = request.form['label']
        my_data.format = request.form['format']
        my_data.year = request.form['year']
        my_data.condition = request.form['condition']
 
        db.session.commit()
        
        flash("Good job! The item was updated successfully.")
 
        return redirect(url_for('index'))
    
# This route is for deleting items from the collection

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Success! The item was removed from your collection")
 
    return redirect(url_for('index'))

# This route is for the contact page and form

@app.route('/contact')
def contact():
    return render_template('contact.html')

# This class is for the contact form


# This setsup the sendmail service for our contact form



# These are routes for supplementary pages

@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/help')
def help():
    return render_template ('help.html')

if __name__ == '__main__':
    app.run(debug=True)