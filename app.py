
from flask import Flask, render_template, request, redirect
from models import db, User, Car
from config import *
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config.from_object("config")

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user = User(username=request.form['username'], password=request.form['password'])
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            login_user(user)
            return redirect('/')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route('/', methods=['GET','POST'])
@login_required
def index():
    stage = request.args.get('stage', '1')
    search = request.args.get('search', '')

    if request.method == 'POST':
        car = Car(
            name=request.form['name'],
            info=request.form['info'],
            image=request.form['image'],
            stage=request.form['stage'],
            user_id=current_user.id
        )
        db.session.add(car)
        db.session.commit()
        return redirect('/')

    cars = Car.query.filter(Car.stage == stage, Car.name.contains(search)).all()
    return render_template('index.html', cars=cars, stage=stage)

@app.route('/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit(id):
    car = Car.query.get(id)
    if request.method == 'POST':
        car.name = request.form['name']
        car.info = request.form['info']
        car.image = request.form['image']
        car.stage = request.form['stage']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', car=car)

@app.route('/delete/<int:id>')
@login_required
def delete(id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
