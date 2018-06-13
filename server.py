from flask import (
    Flask,
    render_template
    )
# create the application instance
app = Flask(__name__, template_folder="templates")

# create a URL route in our application for "/"
@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:    the render template 'home.html'
    """
    return render_template('home.html')

# if we're running in stand alone mode, run the application

if __name__ == '__main__':
    app.run(debug=True)
