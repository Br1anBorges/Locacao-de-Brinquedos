from flask import Flask, render_template 

app = Flask(__main__)




@app.route('/')
def home():
    return render_template('main.html', main)

if __name__ == '__main__':
    app.run(debug=True)