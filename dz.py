from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form.get('login')
        email = request.form.get('email')
        if name =='admin' & email == 'urmaster@gmail.com':
            return "Вы вошли как admin"
        else:
            return "Нет."

    return render_template('hello.html')

if __name__=="__main__":
    app.run()