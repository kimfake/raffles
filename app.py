from flask import Flask, request, render_template, redirect, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


from forms import RaffleForm
from models import db, get_db_uri, User, Raffle
from utils import assign_raffles_to_user, seed_raffles_into_db

from flask import Flask
from flask_mail import Mail
from flask_mail import Message

app = Flask (__name__)
mail = Mail(app)
mail = Mail() 

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



   


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = get_db_uri()
app.config['SECRET_KEY'] = 'some-random-secret-key'

db.app = app
db.init_app(app)
db.create_all()
seed_raffles_into_db()


admin = Admin(app, name='raffles', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Raffle, db.session))

@app.route('/', methods=['GET', 'POST'])
def home():
    form = RaffleForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        # check if user exists
        user = User.query.filter_by(email=email).all()
        if not user:
            user = User(email=email)
            db.session.add(user)
        else:
            user = user[0]
        # assign required raffles to user
        assign_raffles_to_user(form.raffle_count.data, user)
        return redirect(url_for('success'))

    return render_template('home.html', form=form)


@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')


#this is code to actually start the flask server 
#once we get this running without error, we can add the raffle code otherwise we'll not know if it works or not
#can you copy that error in codementor chat
#this command installs all the requirements for the project
#pip install -r requirements.txt
#error fixed..
#can you open a terminal please
#ok so you fixed that, cool.
#which code is giving you the issue ? im trying to add form where email and number of raffles and im not sure
#ok where is the code for raffle and form located i have only got the raffle code 
#what do you expect this project to do in terms of input and output ? normal
if __name__ == '__main__':
    #app.config['DEBUG'] = True
    #app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
    app.run(debug=True)
    #could you please
