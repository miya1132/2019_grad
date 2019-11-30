#!/usr/bin/env python3
from flask import Flask, request, Response, abort, render_template, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from collections import defaultdict

import mysql.connector

app = Flask(__name__)
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)
# app.config['SECRET_KEY']  = "servret"
app.secret_key = 'secret key'

class User(UserMixin):
  def __init__(self, id, name, password):
    self.id = id
    self.name = name
    self.password = password
  
  def get_name(self):
    print("called")
    return self.name

#dev VdwKsbe7rgM3
mydb = mysql.connector.connect(
  host="db", #172.19.0.2
  user="root",
  passwd="VdwKsbe7rgM3",
  database="2019_grad_db"
)

mycursor = mydb.cursor()


# for i in myresult:
#   try:
#     # users.append(User(i))
#     User(i)
#     print("user",User.all)
#   except:
#     break
# ログイン用ユーザー作成
# users = {
#   1: User(1, "user01", "password"),
#   2: User(2, "user02", "password")
# }

# ユーザーチェックに使用する辞書作成
# nested_dict = lambda: defaultdict(nested_dict)
# user_check = nested_dict()
# for i in users.values():
#   user_check[i.name]["password"] = i.password
#   user_check[i.name]["id"] = i.id

@login_manager.user_loader
def load_user(user_id):
  # return users.get(int(user_id))
  return User


# @app.route('/')
# def home():
#     return Response("home: <a href='/login/'>Login</a> <a href='/protected/'>Protected</a> <a href='/logout/'>Logout</a>")

@app.route('/')
@login_required
def home():
  return render_template("home.html")

# ログイン
@app.route('/login', methods=["POST", "GET"])
def login():
  if(request.method == "POST"):
    
    # ユーザーチェック
    sql="SELECT COUNT(*) FROM users where name='{}' and password='{}'".format(request.form["username"],request.form["password"])
    print(sql)
    mycursor.execute(sql)
    myresult=len(mycursor.fetchall())
    print(myresult)
    if(myresult>0):
      mycursor.execute("SELECT id,name,password FROM users where name='{}' and password='{}'".format(request.form["username"],request.form["password"]))
      myresult=mycursor.fetchall()
      print(myresult[0][0],myresult[0][1],myresult[0][2])
      # ユーザーが存在した場合はログイン
      user=User(myresult[0][0],myresult[0][1],myresult[0][2])
      login_user(user)
      # login_user(users.get(1))
      return render_template("home.html", name=str(user.get_name()))
      # return redirect("/")
    # 認証失敗
    else:
      return abort(401)
  else:
      return render_template("login.html")

# ログアウト
@app.route('/logout')
def logout():
  logout_user()
  return redirect("/login")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
