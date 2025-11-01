# main Flask app file

from flask import Flask, render_template # import Flask which is the web framework
from dotenv import load_dotenv # import load_dotenv to load environment variables
import os # import os to access environment variables

load_dotenv() # load environment variables from .env file

app = Flask(__name__) # create a Flask app instance, where to look for templates and static files

@app.route('/') # when someone visits homepage do the below function
def home():
    #return render_template('index.html') # render the index.html template 
    return "Hello, World!"  # temporary response for testing 

if __name__ == '__main__':
    app.run(debug=True) # run the app in debug mode for development