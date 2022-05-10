# Here we are importing the Flask module and creating a 
# Flask web server from the Flask module.
from flask import Flask, render_template

# __name__ means this current file. In this case, it will
# be main.py. This current file will represent my web application.

# We are creating an instance of the Flask class and calling it app. 
# Here we are creating a new web application.
app = Flask(__name__)


# It represents the default page. For example, if I go to a website
# such as “google.com/” with nothing after the slash. Then this will 
# be the default page of Google.


@app.route("/")
# When the user goes to my website and they go to the default page 
# (nothing after the slash), then the function below will get activated.

def home():
    return render_template("home.html")


# added a new route, this time to /DevOps
@app.route("/about")
def about():
    return render_template("about.html")


# When you run your Python script, Python assigns the name “__main__”
# to the script when executed.
if __name__ == "__main__":
    # This will run the application. Having debug=True allows possible Python
    # errors to appear on the web page. This will help us trace the errors.
    app.run(debug=True)
