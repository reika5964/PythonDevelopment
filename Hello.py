from flask import Flask,render_template,request,redirect,url_for
import pymysql

app = Flask(__name__)
conn=pymysql.connect(host='localhost',user='root',password='',database='studentdb')


@app.route("/")
def showdata():
    with conn:
        cur=conn.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        return render_template('index.html',datas=rows)

@app.route("/student")
def showfrom():
        return render_template('addstudent.html')

@app.route("/insert",methods=['POST'])
def insert():
    if request.method == 'POST':
        id = str(request.form.get('id'))
        fname = str(request.form.get('fname'))
        lname  = str(request.form.get('lname'))  
        phone  = str(request.form.get('phone'))
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `student` (`id`,`fname`, `lname`, `phone`) VALUES (`{id}`,`{fname}`,`{lname}`,`{phone}`);".format(id=id,fname=fname,lname=lname,phone=phone))
        conn.commit()
        return redirect(url_for('showdata'))
            

if __name__ == "__main__":
    app.run(debug=True)