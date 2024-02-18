from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form.get('Login')
        email = request.form.get('Email')
        if name =='admin' and email == 'urmaster@gmail.com':
            return render_template('hello.html')
        else:
            return render_template('hell.html')

    # return render_template('hello.html')

if __name__=="__main__":
    app.run()