from flask import Flask,render_template,request,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class MyForm(FlaskForm):  
    name = TextAreaField("名前：")
    submit = SubmitField("送信") 

@app.route("/",methods=['GET','POST'])
def index():
    name=()
    form = MyForm() 
    if form.validate_on_submit():
         name = form.name.data
         form.name.data = ""

    return render_template('index.html',form=form,name=name) 
  
if __name__ == "__main__":  
    app.run(debug=True)

