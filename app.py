from flask import Flask, render_template, request
from numbers_api import get_date_fact, get_math_fact, get_year_fact, get_trivia_fact

app = Flask(__name__)

@app.get("/")
def type_selection():
    date_fact = get_date_fact()
    math_fact = get_math_fact()
    year_fact = get_year_fact()
    trivia_fact = get_trivia_fact()
    return render_template("index.html", date_fact=date_fact, math_fact=math_fact, trivia_fact=trivia_fact, year_fact=year_fact)

@app.get("/date-fact")
def date_fact():
    value = request.args.get('date')
    get_fact = get_date_fact(value)
    return render_template("facts.html", get_fact=get_fact)

@app.get("/math-fact/<value>")
def math_fact(value):
    get_fact = get_math_fact(value)
    return render_template("facts.html", get_fact=get_fact)

@app.get("/year-fact/<value>")
def year_fact(value):
    get_fact = get_year_fact(value)
    return render_template("facts.html", get_fact=get_fact)

@app.get("/trivia-fact/<value>")
def trivia_fact(value):
    get_fact = get_trivia_fact(value)
    return render_template("facts.html", get_fact=get_fact)

#app.run(debug=True)