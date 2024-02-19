from flask import Flask, render_template, request, make_response, redirect, session, url_for

app = Flask(__name__)
app.secret_key = '42'

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form.get('Login')
        email = request.form.get('Email')
        context = {'name': name}
        if name =='admin' and email == 'urmaster@gmail.com':
            response = make_response(render_template('hello.html', **context))
            response.set_cookie('email', email)
            response.set_cookie('name', name)
            return response
        else:
            return render_template('hell.html')

@app.route('/logout/')
def logout():
    response = make_response(redirect(url_for('base')))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response

if __name__=="__main__":
    app.run()