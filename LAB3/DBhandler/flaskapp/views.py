from flaskapp import *
from dbhandler import sqlhandler
app=Flask(_name_)
@app.route("/user/register", methods=["GET","POST"])
def add_user():
    sqlhandler.Mysqlhandler().add_user("dfghjk", 234, "2001-08-04")
    
@app.route("/user/update", methods=["GET","POST"])
def update_user():
    sqlhandler.Mysqlhandler().update_user("changed", "324")
    
@app.route("/user/delete", methods=["GET","POST"])
def delete_user():
    sqlhandler.Mysqlhandler().delete_user("126")
    

@app.route("/user/view", methods=["GET"])
def display_user():
    data = sqlhandler.Mysqlhandler().display_users()
    return str(data)
