from flask import Flask, render_template

from controllers.wine_controller import wine_blueprint

app = Flask(__name__)

app.register_blueprint(wine_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
