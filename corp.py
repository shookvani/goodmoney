def getdata(filename): #this will get the expense data from the file expenses.txt which has the format thing, expense
    data = []
    if filename=='None':
      filename  = 'predict.txt'
    with open(filename, 'r') as file:
        items = file.read().split('\n')
    
    for i in items:
       data.append(i.split(': '))
       
    return data

def gettaxrate(rates,income):

    for i in rates:
        rateto = i
        if int(i[0]) > income:
            continue
        else:
            break
    
    return rateto
    

def alldata(taxrate,data):
   prof= []
   prof.append("profit")
   print(data)
   prof.append(float(data[0][1])-float(data[1][1]))
   data.append(prof)

   return data

def gov(taxrate,data):
    taxmoney = []
    prof = float(data[5][1])
    '''print(taxrate[1])
    print("XX")
    print(prof)'''
    x=float(taxrate[1][1])*prof
    '''print(x)'''

    taxmoney.append("tax money")
    taxmoney.append(prof-(x))
    data.append(taxmoney)

    return data

def charitable(taxrate,data):
    taxable = data[5][1]
    print(taxable)
    taxable = taxable - float(data[3][1])
    '''print(taxable)
    print(data[3][1])
    print("XX")'''
    taxmoney = []

    taxmoney.append("tax money")
    taxmoney.append(taxable-(float(taxrate[1][1])*taxable))
    data.append(taxmoney)

    return data


def wage(taxrate,data):
    taxable = data[5][1]
    #print(taxable)
    taxable = taxable - float(data[4][1])
    #print(taxable)
    '''print(taxable)
    print(data[3][1])
    print("XX")'''
    taxmoney = []
    print(taxrate[1])
    print(taxable-(float(taxrate[1][1])*taxable))

    taxmoney.append("tax money")
    taxmoney.append(taxable-(float(taxrate[1][1])*taxable))
    data.append(taxmoney)

    return data

def addprediction(data,zfile):
    z = getdata(zfile)
    
    if len(data) >= 5:
        del data[5]
        del data[5]
    
    
    data[0][1] = str(float(data[0][1])+float(z[0][1]))
    data[1][1] = str(float(data[1][1])+float(z[1][1]))
    data[2][1] = z[2][1]
    data[3][1] = str(float(data[3][1])+float(z[3][1]))

    return data



def custommsg(taxfile,corpfile):
    x = getdata(taxfile)
    y = getdata(corpfile)
    msg = ""

    print(y)
    print("CCFERGAERG")
    alldata(x,y)

    if (y[2][1] =="employee"):
        zx = wage(x,y)
        msg = msg + "You chose to decrease taxes by your employee wage bonuses. Taxes you must pay are: "+str(zx[6][1])+"."
        del y[6]
        z = gov(x,y)
        msg = msg + " You saved "+str(y[6][1]-zx[6][1])+" by doing so."
    elif (y[2][1] =="gov"):
        z = gov(x,y)
        msg = msg + "You chose not to decrease taxes by your employee wage bonuses or charity donations. Taxes you must pay are: "+str(z[6][1])+"."
    elif (y[2][1] =="charity"):
        zx = charitable(x,y)
        msg = msg + "You chose to decrease taxes by charity donations. Taxes you must pay are: "+str(zx[6][1])+"."
        del y[6]
        z = gov(x,y)
        msg = msg + " You saved "+str((y[6][1]-zx[6][1]))+" by doing so."
    else:
        msg = "error: make sure that you selected employee, charity, or gov"
        return msg
  
    
    return msg


def customdata(taxfile,corpfile):
    x = getdata(taxfile)
    y = getdata(corpfile)
    msg = ""

    print(y)
    print("CCFERGAERG")
    alldata(x,y)

    if (y[2][1] =="employee"):
        zx = wage(x,y)
        msg = msg + "You chose to decrease taxes by your employee wage bonuses. Taxes you must pay are: "+str(zx[6][1])+"."
        del y[6]
        z = gov(x,y)
        msg = msg + " You saved "+str(y[6][1]-zx[6][1])+" by doing so."
    elif (y[2][1] =="gov"):
        z = gov(x,y)
        msg = msg + "You chose not to decrease taxes by your employee wage bonuses or charity donations. Taxes you must pay are: "+str(z[6][1])+"."
    elif (y[2][1] =="charity"):
        zx = charitable(x,y)
        msg = msg + "You chose to decrease taxes by charity donations. Taxes you must pay are: "+str(zx[6][1])+"."
        del y[6]
        z = gov(x,y)
        msg = msg + " You saved "+str((y[6][1]-zx[6][1]))+" by doing so."
    else:
        msg = "error: make sure that you selected employee, charity, or gov"
        return msg
    

    
    return y


def customdatapre(taxfile,corpfile,zfile):
    x = getdata(taxfile)
    y = getdata(corpfile)
    msg = ""

    print(y)
    print("CCFERGAERG")
    alldata(x,y)

    if (y[2][1] =="employee"):
        zx = wage(x,y)
        msg = msg + "You chose to decrease taxes by your employee wage bonuses. Taxes you must pay are: "+str(zx[6][1])+"."
        del y[6]
        z = gov(x,y)
        msg = msg + " You saved "+str(y[6][1]-zx[6][1])+" by doing so."
    elif (y[2][1] =="gov"):
        z = gov(x,y)
        msg = msg + "You chose not to decrease taxes by your employee wage bonuses or charity donations. Taxes you must pay are: "+str(z[6][1])+"."
    elif (y[2][1] =="charity"):
        zx = charitable(x,y)
        msg = msg + "You chose to decrease taxes by charity donations. Taxes you must pay are: "+str(zx[6][1])+"."
        del y[6]
        z = gov(x,y)
        msg = msg + " You saved "+str((y[6][1]-zx[6][1]))+" by doing so."
    else:
        msg = "error: make sure that you selected employee, charity, or gov"
        return msg
    
    count=1
    if count==1:
        predict(y,taxfile,zfile)
        count-=1
    
    return y


def customnum(taxfile,y):
    x = getdata(taxfile)
    msg = ""

    print(y)
    alldata(x,y)

    if (y[2][1] =="employee"):
        zx = wage(x,y)
        msg = msg + "You chose to decrease taxes by your employee wage bonuses. Taxes you must pay are: "+str(zx[6][1])+"."
        del y[6]
        z = gov(x,y)
        msg = msg + " You saved "+str(y[6][1]-zx[6][1])+" by doing so."
    elif (y[2][1] =="gov"):
        z = gov(x,y)
        msg = msg + "You chose not to decrease taxes by your employee wage bonuses or charity donations. Taxes you must pay are: "+str(z[6][1])+"."
    elif (y[2][1] =="charity"):
        zx = charitable(x,y)
        msg = msg + "You chose to decrease taxes by charity donations. Taxes you must pay are: "+str(zx[6][1])+"."
        del y[6]
        z = gov(x,y)
        msg = msg + " You saved "+str((y[6][1]-zx[6][1]))+" by doing so."
    else:
        msg = "error: make sure that you selected employee, charity, or gov"
        return msg
    
    
    return msg

def predict(data,taxfile,zfile):
    x = addprediction(data,zfile)
    return customnum(taxfile,x)
    

def main():
    x = custom('corpthreedata.txt','taxbyincome.txt')
    
    '''y = getdata('corpthreedata.txt')
   #print(taxrates('taxbyincome.txt'))
   x = gettaxrate(getdata('taxbyincome.txt'),20000)
   alldata(x, y) #adds profit and gets tax rate

   #value you would pay gov
   #print(gov(x,y))

   #value you would pay if you choose 501
   #print(charitable(x,y))

   #value you would pay if you have wage bonus
   print(wage(x,y))
'''

if __name__ == "__main__":
  main()