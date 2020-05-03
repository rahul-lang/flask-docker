from flask import render_template,url_for,flash,redirect,request
from app.forms import RegistrationForm,LoginForm,UpdateAccountForm
from app import app,db
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from flask_login import login_user,current_user,logout_user,login_required


 
@app.route("/")
@app.route("/home")
def home():
    return render_template('login/home.html')

@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=RegistrationForm()
    
    if form.validate_on_submit():
           
           
           user=User(username=form.username.data,email=form.email.data,password=form.password.data)
           db.session.add(user)
           db.session.commit()
           flash(f'Account created.You are now a user', 'success')
           return redirect(url_for('login'))
           
    return render_template('login/register.html',form=form, title='Register')
        
@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and user.is_correct_password(form.password.data):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            return redirect(next_page) if next_page  else redirect(url_for('home'))
        else:
           flash('logging unsuccesful','danger')
    return render_template('login/login.html',form=form, title='Login')


@app.route("/logout")
def logout():
   logout_user()
   return redirect(url_for('home'))
@app.route("/account",methods=['GET','POST'])
@login_required
def account():
   form=UpdateAccountForm()
   if form.validate_on_submit():
      current_user.username=form.username.data
      current_user.email=form.email.data
      db.session.commit()
      flash('Your account has been updated!','success')
      return redirect(url_for('account'))
   elif request.method =='GET':
       form.username.data=current_user.username
       form.email.data=current_user.email
   return render_template('login/account.html', title='Account',form=form)

@app.route("/about")
def about():
    return render_template('login/about.html', title='About')

