import budget as b
import corp as c
from flask import Flask, render_template,request

taxile = 'taxbyincome.txt'
corpfile ='corpthreedata.txt'

app = Flask(__name__)

@app.route('/')
def index():
  x = c.custommsg('taxbyincome.txt','corpthreedata.txt')
  y = c.customdata('taxbyincome.txt','corpthreedata.txt')
  print("here")
  print(y)
  exp=str(round(float(y[1][1]),2))
  d = str(round(float(y[3][1]),2))
  return render_template("index.html", profit = str(round(y[5][1],2)),expenses=exp,deduction=d)


@app.route('/help')
def help():
  return render_template("help-center.html")

@app.route('/profile')
def profile():
  return render_template("profile.html")

@app.route('/setting')
def setting():
  return render_template("setting.html")

@app.route('/transaction')
def transaction():
  return render_template("transaction-detail.html")

@app.route('/wallet')
def wallet():
  x = c.custommsg('taxbyincome.txt','corpthreedata.txt')
  y = c.customdata('taxbyincome.txt','corpthreedata.txt')
  print("here")
  print(y)
  t=str(round(y[6][1],2))
  p=str(round(float(y[4][1]),2))
  d = str(round(float(y[3][1]),2))
  exp = str(round(float(y[1][1]),2))
  rev = str(round(float(y[0][1]),2))
  m=str(round(y[5][1],2))
  return render_template("wallet.html", taxname = 'tax money',tax=t,profname='wage bonus',profit=p,deductname="deductable",deductable=d,expensename="expenses",expense=exp,revenuename="revenue",revenue=rev,money=m)

@app.route('/finance')
def finance():
  if request.method == 'GET':
    x = c.custommsg('taxbyincome.txt','corpthreedata.txt')
    z = str(request.args.get("myFile"))
    print(z)
    y = c.customdatapre('taxbyincome.txt','corpthreedata.txt',z)
    #y= c.predict(y,'taxbyincome.txt')
    print("here")
    print(y)
    exp=str(round(float(y[1][1]),2))
    d = str(round(float(y[3][1]),2))
    #print(request.get.args("rev"))
    return render_template("finance.html", profit = str(round(y[5][1],2)),expenses=exp,deduction=d)


if __name__ == "__main__":
  app.run('0.0.0.0', 8080)