from flask import Flask, render_template, request, session, redirect, url_for, g 

 

class User:
    def __init__(self, id, username, password):
        self.id = id 
        self.username = username
        self.password = password 

    def __repr__(self):
        return f'<User: {self.username}>'
    
users = []
users.append(User(id=1, username='Emmanuel', password='password'))
users.append(User(id=2, username='Bonisam', password='greatness'))

print(users[1].id)


app = Flask(__name__)
app.secret_key = 'secretkeyishouldknow'

@app.before_request
def before_request():
    if 'user_id' in session: 
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user 

@app.route('/')
def index ():
    return "<h1>Hello Bonisam</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']


        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))
    
        return redirect(url_for('login'))

    return render_template("login.html")

@app.route("/profile")
def profile():
    return render_template('profile.html')




