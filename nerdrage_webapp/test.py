# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/diagnostics')
def welcome():
    return app.send_static_file('diagnostics.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)