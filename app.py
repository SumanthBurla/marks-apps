import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    res = conn.execute('SELECT * FROM halfyearly_exam_marks').fetchall()
    tops = conn.execute('SELECT * FROM halfyearly_exam_marks ORDER BY (grade) DESC LIMIT 3;').fetchall()
    conn.close()
    return render_template('index.html', marks=res, top=tops)

@app.route('/add')
def add():
    return render_template('add.html')
   
@app.route('/result', methods=['POST'])
def result():
    std_name=request.form['std_name']
    maths=request.form['maths']
    physics=request.form['physics']
    coding=request.form['coding']
    summ = (int(maths)+int(physics)+int(coding))/300
    grade= int(summ*100)
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO halfyearly_exam_marks (std_name, maths, physics, coding, grade) VALUES (?, ?, ?, ?, ?)",
            (std_name, maths, physics, coding, grade)
            )
    res = conn.execute('SELECT * FROM halfyearly_exam_marks').fetchall()
    tops = conn.execute('SELECT * FROM halfyearly_exam_marks ORDER BY (grade) DESC LIMIT 3;').fetchall()
    conn.commit()
    conn.close()
    return render_template('index.html', marks=res, top=tops)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/bar')
def bar():
    stds=[]
    grades=[]
    conn = get_db_connection()
    cur = conn.cursor()
    res = conn.execute('SELECT * FROM halfyearly_exam_marks').fetchall()
    conn.commit()
    conn.close()
    for r in res:
        stds.append(r['std_name'])
        grades.append(r['grade'])
    return render_template('bar.html', title='Students performance.', max=100, labels=stds, values=grades)


if __name__ == "__main__":
    app.run(debug=True)
