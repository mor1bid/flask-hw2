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
        response = make_response("Cookie installed")
        if name =='admin' and email == 'urmaster@gmail.com':
            response.set_cookie('email', email)
            response.set_cookie('name', name)
            # session['name'] = request.form.get('name')
            # return response
            return render_template('hello.html', **context)
        else:
            response.set_cookie('email', email)
            response.set_cookie('name', name)
            return render_template('hell.html')
    return response

@app.route('/logout/')
def logout():
    # session.pop('name', None)
    response = make_response("Cookie deleted")
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response
    return redirect(url_for('base'))

if __name__=="__main__":
    app.run()