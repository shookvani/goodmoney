import decimal as d 

money = 0
expenses = {}


def getdata(): #this will get the expense data from the file expenses.txt which has the format thing, expense
    with open('expenses.txt', 'r') as file:
        items = file.read().split('\n')

    costs = []
    #print(items)

    for item in items:
        try:
            costs.append(item.split(','))

        except Exception as e:
            error = str(e)
            print('Exception: Expenses File Format Incorrect')
            print(f'Error Cause: {error}')  
            return []

    return costs

def getnames(data):
    namelist = []

    for i in data:
        #print(i)
        namelist.append(i[0])

    return namelist
    

def getvaluesper(data):
    valuelist = []

    for i in data:
        #print(i)
        valuelist.append(float(i[1]))
        
    return valuelist

def populateexpenses(names, values):
    for i in range(len(names)):
        expenses[names[i]] = values[i]
    
    return expenses

def gettotalexpense(values):
    sum = 0
    for i in values:
        sum += i
    
    return sum

def gettotalavailable():
    with open('total.txt', 'r') as file:
        items = file.read().split('\n')

    costs = []
    #print(items)

    for item in items:
        try:
            costs.append(item.split(','))

        except Exception as e:
            error = str(e)
            print('Exception: Expenses File Format Incorrect')
            print(f'Error Cause: {error}')  
            return 0

    return costs


def gettotalavailablenum():
    with open('total.txt', 'r') as file:
        items = file.read().split('\n')

    costs = []
    #print(items)

    for item in items:
        try:
            costs.append(item.split(','))

        except Exception as e:
            error = str(e)
            print('Exception: Expenses File Format Incorrect')
            print(f'Error Cause: {error}')  
            return 0
    
    totavail = 0
    for i in costs:
        totavail = totavail + float(i[1])

    return totavail


def getmoneyused(exp,available):
    #print(available)
    itemsused = []
    moneyused = 0
    count = exp
    all = []
    totavail = 0
    for i in available:
        totavail = totavail + float(i[1])

    temp = totavail

    #print(totavail)
    #print(exp)
    #print(available)

    #while count != 0:
    #print(count)
    for i in available:
        #print(moneyused)
       # print(i)
        count = count - float(i[1])
        moneyused = moneyused + float(i[1])
        itemsused.append(i[0])
        #print(count)

        if count < 0:
            count = count + float(i[1])
            moneyused = moneyused - float(i[1])
            itemsused.remove(i[0])
            totavail -= moneyused
            #rint(totavail)

            if totavail > count:
                #print(totavail)
                #print(totavail - count)
                #print('ere')
                if float(i[1]) > count:
                    x = float(i[1]) - float(count)
                    y = float(i[1]) - x
                    moneyused += y
                    #print(moneyused)
                    #print(temp)
                    count -= y 
                    itemsused.append(i[0])
                else:
                    continue
                
            break

        if count == 0:
            break


    print(moneyused)
    print(temp)
    final = temp - moneyused
    all = [itemsused, moneyused, count,final]

    return all


def check(x,ex):
    return x - ex >= 0



def calculatebudget(all):
    budgetmoney = []
    budgetmoney.append(str(all[1])) #spent x money
    budgetmoney.append(str(all[0])) # using this
    budgetmoney.append(str(all[2])) # you have this much of expenses left
    budgetmoney.append(str(all[3])) #and this much money to use
    msg = ""

    x = ""

    for i in all[0]:
      x += i
      x+=', '

    budgetmoney[1] = x

    msg = msg + "you spent " + budgetmoney[0] +" using money from your: "+ budgetmoney[1] + ". You have "+budgetmoney[2]+" left to pay."

    if float(budgetmoney[2]) >0:
        msg = msg + " You will need to find different ways to come up with the money for this. You have "+budgetmoney[3]+" money left to use. This number is probably zero or not a lot. We would recommend you to find different ways to gain more money for your expenses."
    else:
        msg = msg + " You have "+budgetmoney[3]+" left to use as a budget."

    budgetmoney.append(msg)


    return budgetmoney[4]

def main():
    '''print(getdata())
    print(getnames(getdata()))
    print(getvaluesper(getdata()))
    print(populateexpenses(getnames(getdata()), getvaluesper(getdata())))
    print(gettotalexpense(getvaluesper(getdata())))
    print(gettotalavailable())
    print(calculatebudget(gettotalexpense(getvaluesper(getdata)),gettotalavailable))'''

    x = getmoneyused(float(gettotalexpense(getvaluesper(getdata()))),gettotalavailable())
    print(x)

    #print(gettotalexpense(getvaluesper(getdata())),gettotalavailablenum(),x[1])

    print(calculatebudget(getmoneyused(float(gettotalexpense(getvaluesper(getdata()))),gettotalavailable())))

if __name__ == "__main__":
  main()