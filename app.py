from flask import Flask, render_template,request,redirect
import firebase_admin 
from firebase_admin import credentials,db
app= Flask (__name__)
cred=credentials.Certificate("D:/flask.01/python-cloud-computing-firebase-adminsdk-fbsvc-f1c0fed44f.json")
if not firebase_admin._apps:
     firebase_admin.initialize_app(cred,{"databaseURL":"https://python-cloud-computing-default-rtdb.firebaseio.com/"})

@app.route('/',methods=['GET','POST'])
def Home():
    if request.method=='POST':
       branch=request.form.get('branch')
       year=request.form.get('year')
       feedback=request.form.get('feedback')
       db.reference('/index').push({'branch':branch,'year':year,'feedback':feedback})           
       return redirect('/')
    else:
     db.reference('/visits').push({'page':'index'})
     return render_template("index.html")
@app.route('/contact',methods=['GET','POST'])
def contact():          
  if request.method=='POST':
    name=request.form.get('name')
    message=request.form.get('message')
    db.reference('/contact').push({'name':name,'messsage':message})           
    return redirect('/contact')
  else:
     db.reference('/visits').push({'page':'contact'})
     return render_template("contact.html")
@app.route('/about',methods=['GET','POST'])
def about(): 
  if request.method=='POST':
    name1=request.form.get('name1')
    db.reference('/about').push({'name1':name1})           
    return redirect('/about')
  else:
     db.reference('/visits').push({'page':'about'})
     return render_template("about.html")
if __name__=='__main__':
 app.run(debug=True)