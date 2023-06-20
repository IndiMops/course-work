from flask import Flask, render_template, url_for, flash, request
"""from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash"""

app = Flask(__name__)
"""
app.config['SECRET_KEY'] = 'laskjdbnlasjkd jaskldnkascj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:qwerty@localhost/users'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# DB model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True)
    favorite_color = db.Column(db.String(20))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    password_hash = db.Column(db.String(64))
    
    @property
    def password(self):
        raise AttributeError('парол не є читабельним атрибутом!')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
   
    def __repr__(self):
        return '<Name %r>' % self.name



# Форми
class UserForm(FlaskForm):
    name = StringField('Ім\'я', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    favorite_color = StringField('Улюблений колір')
    submit = SubmitField('Надіслати')


class NameForm(FlaskForm):
    name = StringField('Як тебе звати?', validators=[DataRequired()])
    submit = SubmitField('Надіслати')
"""

# Маршрути
@app.route('/')
def home():
    return render_template('index.html')



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


@app.route('/composition')
def composition():
    return render_template('composition.html')
"""
@app.route('/wtf', methods=['GET', 'POST'])
def wtf():
    name = None
    form = NameForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash('Форма була відправлена.')

    return render_template('wtf.html', name=name, form=form)




@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    global alert
    alert = 'alert-success'
    
    if form.validate_on_submit():
        user = Users.query.filter_by(email = form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data, favorite_color=form.favorite_color.data)
            db.session.add(user)
            db.session.commit()
            flash('Користувача успішно додано!')
        else:
            flash('Користувач з таким електронним адресом вже існує.')
            alert = 'alert-danger'
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        form.favorite_color.data = ''
    our_users = Users.query.order_by(Users.date_added)
    return render_template('add_user.html', form=form, name=name, our_user=our_users, alert=alert)


@app.route('/user/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    form = UserForm()
    global alert
    alert = 'alert-success'
    update_name = Users.query.get_or_404(id)
    if request.method == 'POST':
        update_name.name = request.form['name']
        update_name.email = request.form['email']
        update_name.favorite_color = request.form['favorite_color']
        try:
            db.session.commit()
            flash('Користувача оновлено!')
            return render_template('update_user.html', form=form, update_name=update_name, alert=alert)
        except:
            flash('Щось пішло не так!')
            alert = 'alert-warning'
            return render_template('update_user.html', form=form, update_name=update_name, alert=alert)
    else:
        return render_template('update_user.html', form=form, update_name=update_name, alert=alert, id=id)
    

@app.route('/user/delete/<int:id>')
def delete_user(id):
    user_to_delete = Users.query.get_or_404(id)
    name = None
    form = UserForm()
    global alert
    alert = 'alert-success'
    
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash('Користувач був видалений!')
        our_users = Users.query.order_by(Users.date_added)
        return render_template('add_user.html', form=form, name=name, our_user=our_users, alert=alert)
    except:    
        flash('Поимлка! Виникла проблема із видаленням користувача...')
        alert = 'alert-danger'
        our_users = Users.query.order_by(Users.date_added)
        return render_template('add_user.html', form=form, name=name, our_user=our_users, alert=alert)
"""

@app.route('/news')
def main_news():
    return render_template('news/news.html')

@app.route('/news/1')
def news1():
    return render_template('news/news1.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)