from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/matches')
def matches():
    return render_template('matches.html')

@app.route('/inbox')
def inbox():
    return render_template('inbox.html')

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
