from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route('/application-form', methods=["POST"])
def application_form():4

    return render_template("application-form.html", first_name="firstname", last_name="lastname", min_salary="salary", job_title="selection")


@app.route('/application', methods=["GET"])
def application():

    request.form.get("firstname")
    request.form.get("lastname")
    request.form.get("salary")
    request.form.get("position")

    return render_template("application-response.html")

if __name__ == "__main__":
    app.run(debug=True)
