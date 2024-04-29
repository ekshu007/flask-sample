from flask import Flask, render_template

app = Flask(__name__)
JOBS = [{
    "id": 1,
    "title": "Data Analyst",
    'location': "Bengaluru, India",
    "salary": "Rs. 10,00,000"
}, {
    "id": 2,
    "title": "Data Scientist",
    'location': "Chennai, India",
    "salary": "Rs. 15,00,000"
}, {
    "id": 3,
    "title": "Front end engineer",
    'location': "Remote",
    "salary": "Rs. 9,20,000"
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Jovian")


@app.route("/api/jobs")
def list_jobs():
  return jasonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
