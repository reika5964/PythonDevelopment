from flask import Flask,render_template
import pymysql

app = Flask(__name__)
conn=pymysql.connect(host='localhost',user='root',password='',database='studentdb')

@app.route("/")
def hello():
    with conn:
        cur=conn.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        return render_template('index.html',datas=rows)
 
if __name__ == "__main__":
    app.run(debug=True) 