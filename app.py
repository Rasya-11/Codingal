"""
1) Import the required Flask tools.
   a) Use `Flask` to create the web app.
   b) Use `render_template` to show HTML pages.
   c) Use `request` to read form data submitted by the user.


"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    units = int(request.form["units"])
    bills = units * 5

    if units <= 100:
        message = "Great! You are an energy saver! 🌱"
    elif units <= 200:
        message = "Not bad! Try saving a little more! 👍"
    else:
        message = "Whoa! Time to switch off some lights! 💡"

    return render_template("index.html", units=units, bill=bills, message=message)

if __name__ == "__main__":
    app.run(debug=True)

"""

2) Create the Flask app.
   a) Store the Flask application in the `app` variable.

3) Create the home route.
   a) Use `@app.route("/")` for the main page.
   b) Create the `home()` function.
   c) Show the `index.html` page using `render_template()`.

4) Create the calculate route.
   a) Use `@app.route("/calculate", methods=["POST"])`.
   b) Create the `calculate()` function.
   c) Read the electricity units from the form.
   d) Convert the units value into an integer.
   e) Calculate the bill by multiplying units by 5.

5) Use conditions to create an energy-saving message.
   a) If units are 100 or less, show the energy saver message.
   b) If units are 200 or less, show the moderate usage message.
   c) Otherwise, show the high usage warning message.

6) Show the result on the HTML page.
   a) Send units, bill, and message back to `index.html`.

7) Run the Flask app.
   a) Use `if __name__ == "__main__"` to start the app directly.
   b) Run the app in debug mode using `app.run(debug=True)`.
"""