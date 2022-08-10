from flask import Flask,render_template,request,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,BooleanField,RadioField,SelectField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
  

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'mykey'
Bootstrap(app)
 
class MyForm(FlaskForm):  
    name = StringField("名前：",validators=[DataRequired()])
    gender = RadioField('性別',choices=[('male','男性'),('femele','女性'),('other','その他')])
    skill = SelectField('言語',choices=[('English','英語'),('thai','タイ語'),('japanese','日本語')])
    address = TextAreaField("住所：")
    isAccept=BooleanField('条件') 
    submit = SubmitField("送信") 
 
@app.route("/",methods=['GET','POST'])
def index():
    form = MyForm() 
    if form.validate_on_submit():
        flash("登録されました。")
        session['name'] =form.name.data
        session['isAccept']= form.isAccept.data
        session['gender']= form.gender.data
        session['skill'] = form.skill.data
        session['address'] =form.name.data
         #ลบข้อมูลจากแบบฟอร์ม
        form.name.data = ""
        form.isAccept.data = ""
        form.gender.data = ""
        form.skill.data = ""
        form.address.data = "" 
    return render_template('index.html',form=form) 
  
if __name__ == "__main__":  
    app.run(debug=True)


