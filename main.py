from flask import Flask, request, render_template
app = Flask(__name__)
app.config['DEBUG'] = True 

@app.route("/")
def message():
    #error_message = str("Invalid input")
    #welcome_message = str("Welcome [username]")
    return render_template('index.html')
   



@app.route("/")
def username():
    if not valid:
        return error_message
    else:
        return welcome_message

@app.route("/")
def password():
    if not valid:
        return error_message
    else:
        return welcome_message

if __name__ == '__main__':
    app.run()


 

