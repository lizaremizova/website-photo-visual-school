from flask import Flask, render_template, request, url_for, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
app = Flask(__name__)

app.config.update(
    SECRET_KEY = 'WOW SUCH SECRET'
)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(login):
    if login == 'admin':
        return User(login)

@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login = 'admin'
    password = 'admin'
    if request.method == 'POST':
        if request.form['login'] == login and request.form['password'] == password:
            user = User(login) # creating user
            login_user(user) # logging user in
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Incorrect username or password')
    return render_template('login.html')

app.run(debug=True)
