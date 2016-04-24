from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route('/application-form', methods=["POST"])
def application_form():

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    min_salary = request.form.get("salary")
    job_title = request.form.get("position")

    return render_template("application_form.html", first_name="firstname", last_name="lastname", min_salary="salary", job_title="selection")


@app.route('/application', methods=["GET"])
def application():

    request.form.get("firstname")
    request.form.get("lastname")
    request.form.get("salary")
    request.form.get("position")

    return render_template("application_response.html")

if __name__ == "__main__":
    app.run(debug=True)
