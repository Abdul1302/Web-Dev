from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def about():
    return "This is the about page.hello Abdullah"

@app.route('/success/<score>')
def success(score):
    return "Your score is " + score

@app.route('/fail/<score>')
def fail(score):
    return "Your score is " + score

@app.route('/result/<int:score>')
def result(score):
    if score >= 50:
        result = 'Pass'
    else:
        result = 'Pass'

    return result    

if __name__ == '__main__':
    app.run(debug=True)
