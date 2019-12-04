#!/usr/bin/env python3
from flask import Flask, request, Response, abort, render_template, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from collections import defaultdict
import traceback
import mysql.connector

app = Flask(__name__)
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)
app.secret_key = 'secret key'

class User(UserMixin):
  def __init__(self, id, login_id, name):
    self.id = id
    self.login_id = login_id
    self.name = name

connect = mysql.connector.connect(
  host="db",
  user="root",
  passwd="2019_grad",
  database="2019_grad_db"
)

@login_manager.user_loader
def load_user(user_id):
  return User

@app.route('/')
@login_required
def home():
  return render_template("home.html")

# ログイン
@app.route('/login', methods=["POST", "GET"])
def login():
  if(request.method == "POST"):
    
    try:
      # ユーザーチェック
      cursor = connect.cursor(dictionary=True)
      sql = "SELECT * FROM users where login_id='{}' and password='{}'".format(request.form["username"], request.form["password"])
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None:
        # ユーザーが存在した場合はログイン
        user = User(row['id'], row['login_id'], row['name'])
        login_user(user)
        return render_template("home.html", name = str(user.name))
      # 認証失敗
      else:
        return render_template("login.html")
    except:
      print(traceback.print_exc())
      return abort(500)
    finally:
      cursor.close()
  else:
      return render_template("login.html")

# ログアウト
@app.route('/logout')
def logout():
  logout_user()
  return redirect("/login")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
