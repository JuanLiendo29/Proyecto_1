from flask import Flask
from flask import Flask,render_template,request,session,logging,url_for,redirect,flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session,sessionmaker
from flask import json
import pandas as pd
import csv
from sqlalchemy import or_

from passlib.hash import sha256_crypt
#engine=create_engine("postgresql://postgres:@localhost:5432/proyecto_1")

#db=scoped_session(sessionmaker(blind=engine))
app= Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/proyecto1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kparykko:euHJqLkE9npPS9wD6V2bxu0snUsZvf96@drona.db.elephantsql.com:5432/kparykko'
db = SQLAlchemy(app)
Bootstrap(app)




class usuarios(db.Model):
    usuario = db.Column(db.VARCHAR(255), primary_key=True)
    password = db.Column(db.VARCHAR(255))

    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password

    def __repr__(self):
        return '<usuarios %r>' % self.usuario


class libros(db.Model):
    isbn= db.Column(db.VARCHAR(255), primary_key=True)
    title= db.Column(db.VARCHAR(255))
    author= db.Column(db.VARCHAR(255))
    year= db.Column(db.VARCHAR(255))

    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year




class LoginForm(FlaskForm):
    usuario = StringField('usuario', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=20)])

class RegisterForm(FlaskForm):
    usuario = StringField('usuario', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=20)])

class busquedaForm(FlaskForm):
    busqueda = StringField('busqueda', validators=[InputRequired(), Length(min=4, max=200)])
    





@app.route("/")
def home():
    return render_template("index.html")




@app.route("/perfil/<usuario>")
def perfil(usuario):
    user = usuarios.query.filter_by(usuario=usuario).first()
    return render_template('perfil.html', user=user)







@app.route("/busqueda", methods=['GET', 'POST'])
def busqueda():
    form = busquedaForm()
    
    

    if form.validate_on_submit() and request.method == 'POST':
        busquedalib = request.form.get('busqueda')
        search = "%{}%".format(busquedalib)       
        libros2 = libros.query.filter(
            (libros.isbn.like(search)) | (libros.title.like(search)) | (libros.author.like(search))
        )

        return render_template("libro.html", libro_autor=libros2)     


    return render_template("busqueda.html", form=form)

    @app.route("/logout")
    def logout():
        session.clear()

    return redirect(url_for("home"))






@app.route("/Login", methods=['GET', 'POST'])
def Login():
    form = LoginForm()

    if form.validate_on_submit() and request.method == 'POST':

        usuario = request.form.get('usuario')
        userpassword = request.form.get('password')
        user = usuarios.query.filter_by(usuario=usuario, password=userpassword).first()

        if not user:
            #flash('Please check your login details and try again.')
            return render_template("Login.html", form=form)
            # if user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        return render_template("perfil.html", user=user, form=form)
        
    return render_template("Login.html", form=form)







@app.route("/Registrar", methods=['GET', 'POST'])
def Registrar():
    form = RegisterForm()

    if form.validate_on_submit():
        nuevo_usuario= usuarios(request.form['usuario'], request.form['password'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        #return '<h1>' + form.usuario.data + ' ' + form.contraseña.data + '<h1>'

    return render_template('Login.html', form=form, message="Te Registraste exitosamente!")






# def main():
#     f = open("books.csv")
#     reader = csv.reader(f)

#     for isbn, title, author, year in reader:
#         db.execute("INSERT INTO libros (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", {"isbn": isbn, "title":title, "author":author, "year":year})
#         print(f"isbn: {isbn} - title: {title} - author: {author} - year: {year} ")
#     db.session.commit()



if __name__ == "__main__":
    app.secret_key="123456dailweebcoding"
    app.run(debug=True)