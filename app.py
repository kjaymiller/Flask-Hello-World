from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = "Hello World!"
    return render_template('index.html', message=msg)


@app.route('/<name>')
def hello_name(name):
    msg = f'Hello {name}!'
    return render_template('index.html', message=msg)

if __name__ == '__main__':
    app.run()