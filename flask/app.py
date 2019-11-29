#!/usr/bin/env python3
from flask import Flask, request, Response, abort, render_template, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from collections import defaultdict

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

# ログイン用ユーザー作成
users = {
  1: User(1, "user01", "password"),
  2: User(2, "user02", "password")
}

# ユーザーチェックに使用する辞書作成
nested_dict = lambda: defaultdict(nested_dict)
user_check = nested_dict()
for i in users.values():
  user_check[i.name]["password"] = i.password
  user_check[i.name]["id"] = i.id

@login_manager.user_loader
def load_user(user_id):
  return users.get(int(user_id))

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
    if(request.form["username"] in user_check and request.form["password"] == user_check[request.form["username"]]["password"]):
      # ユーザーが存在した場合はログイン
      # login_user(users.get(user_check[request.form["username"]]["id"]))
      login_user(users.get(1))
      
      return redirect("/")
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
