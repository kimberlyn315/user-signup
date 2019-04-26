from flask import Flask, request, render_template, redirect
app = Flask(__name__)
app.config['DEBUG'] = True 

@app.route("/")
def message():
    #error_message = str("Invalid input")
    #welcome_message = str("Welcome [username]")
    return render_template('index.html')
   



@app.route("/", methods=['POST'])
def username():
    username = request.form['username']
    username_error_message = ''
    password = request.form['password']
    password_error_message = ''
    if len(username) < 3 or len(username) > 20:
         username_error_message = 'The username is not correct'
         return render_template('index.html', username_error_message=username_error_message)
    
    
    elif len(password) < 3 or len(password) > 20:
        password_error_message = 'The password is not correct'
        return render_template('index.html', password_error_message=password_error_message)
    else:
        return redirect ('/welcome?username={0}'.format(username))   

@app.route("/welcome")
def welcome_page():
    username = request.args.get('username')
    return '<h1>Welcome, {0}!</h1>'.format(username)

if __name__ == '__main__':
    app.run()


 

