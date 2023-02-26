import mysql.connector
#aid allergy adesc
mydb = mysql.connector.connect(host="localhost",user="root",passwd="Dhruvgupta.",database="hack")
def al():
    mycursor=mydb.cursor()
    allist=[]
    mycursor.execute('select*from allergy')
    for i in mycursor:
        allist.append(i)
    return allist

def get_recipe(x):
    mycursor=mydb.cursor()
    reclist=[]
    str1='select * from recipe where aid ='+str(x)
    mycursor.execute(str1)
    for j in mycursor:
        reclist.append(j)
    return reclist

def ids(str):
    mycursor=mydb.cursor()
    allist=[]
    mycursor.execute('select*from allergy')
    for i in mycursor:
        allist.append(i)
    for i in range(0,9):
        if(str.lower()==allist[i][1].lower()):
            return i+1