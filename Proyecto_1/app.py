from flask import Flask,render_template,request,session,logging,url_for,redirect,flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session,sessionmaker

from passlib.hash import sha256_crypt
#engine=create_engine("postgresql://postgres:@localhost:5432/proyecto_1")

#db=scoped_session(sessionmaker(blind=engine))
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/proyecto1'
db = SQLAlchemy(app)
Bootstrap(app)

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=20)])

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=20)])

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/perfil/<username>")
def perfil(username):
    user = User.query.filter_by(username=username).first()
    return render_template('perfil.html', user=user)

@app.route("/Login", methods=['GET', 'POST'])
def Login():
    form = LoginForm()

    if form.validate_on_submit():
        #user = User.query.filter_by(username=form['username'])
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            #if user.password == request.form['password']:
            if user.password == form.password.data:
                return redirect(url_for('perfil'))
        return '<h1> Contraseña o usuario invalido</h1>'
        #usuario= (request.form['username'])
        #contraseña = (request.form['password']) 
        #users = User.query.filter_by(username=username)
        #passwords = User.query.filter_by(password=password)
        
    return render_template("Login.html", form=form)

@app.route("/Registrar", methods=['GET', 'POST'])
def Registrar():
    form = RegisterForm()

    if form.validate_on_submit():
        nuevo_usuario= User(request.form['username'], request.form['password'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        #return '<h1>' + form.usuario.data + ' ' + form.contraseña.data + '<h1>'

    return render_template('Registrar.html', form=form)

if __name__ == "__main__":
    app.secret_key="123456dailweebcoding"
    app.run(debug=True)