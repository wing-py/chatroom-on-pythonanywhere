from flask import Flask,render_template,request
import os

here = os.path.dirname(os.path.abspath(__file__))
static = os.path.join(here, 'static')

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def chatroom():
    return render_template("home.html")
@app.route('/chatroom',methods=["GET","POST"])
def home():
    chat=os.path.join(static,"chat.txt")
    f=open(chat,"r")
    x=f.read()
    f.close()
    if request.method=="POST":
        message=request.form['message']
        f=open(chat,"a")
        f.write(message+"\n")
        f.close()
        f=open(chat,"r")
        x=f.read()
        f.close()
        return render_template("chatroom.html",boardtxt=x)
    return render_template("chatroom.html",boardtxt=x)

if __name__=="__main__":
    app.run(debug=True)
