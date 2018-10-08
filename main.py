from flask import Flask, request, redirect, render_template
import validators
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def form():
    username = ''
    password = ''
    vpassword = ''
    email = ''
    username_error = ''
    password_error = ''
    vpassword_error = ''
    email_error = ''
    return render_template('form.html', title="Signup")

@app.route("/", methods=['POST','GET'])
def submission():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        vpassword = request.form['vpassword']
        email = request.form['email']
    
    errors = validators.check_entries(username, password, vpassword, email)
    username_error = errors['username']
    password_error = errors['password']
    vpassword_error = errors['vpassword']
    email_error = errors['email']

#===================================================================================================================================
    # username_error = ''
    # password_error = ''
    # vpassword_error = ''
    # email_error = ''
    # username = 'Samrah'
#===================================================================================================================================

    if username_error == '' and password_error == '' and vpassword_error == '' and email_error == '' :
        #return redirect('/welcome', thename=username)
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('form.html', title="Signup", username=username, password=password, vpassword=vpassword, email=email,
        username_error=username_error, password_error=password_error, vpassword_error=vpassword_error, email_error=email_error)


@app.route('/welcome', methods=['POST','GET'])
def result():
        #return render_template('welcome.html', username=username)
        username = request.args.get("username")
        html_style = '<html style="font-size: 5em; font-family: Trebuchet MS, Helvetica, sans-serif; background-color: #6C648B; color: #FFF; margin-left: 15%; margin-top: 10%;"> '
        return html_style + ' Welcome, {0} ! </html>'.format(username)


app.run()