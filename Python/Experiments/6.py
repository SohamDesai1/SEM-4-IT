import mysql.connector as sql
import matplotlib.pyplot as plt
import numpy as np
maleSurvived = 0
maleDeath = 0
femaleSurvived = 0
femaleDeath = 0
myDatabase = sql.connect(host="localhost", user="root",passwd="", database="soham123")
myQuery= (myDatabase.cursor)
queryl="select * from fastlearner where Sex='male' and survived=1"
myQuery.execute(query(1))
myResultl= (myQuery.fetchall)
for x in myResult:
    maleSurvived = maleSurvived+ 1
    print(maleSurvived)
query2="select * from fastlearner where Sex='male' and survived=0"
myQuery.execute(query2)
myResult2= (myQuery.fetchall)
for x in myResult2:
    maleDeath = maleDeath+1
    print(maleDeath)
query3="select * from fastlearner where Sex=female' and survived=1"
myQuery.execute(query3)
myResult3 = (myQuery.fetchall)
for x in myResult3:
    femaleSurvived = femaleSurvived+1
    print(femaleSurvived)
query4="select * from fastlearner where Sex=female' and survived-0"
myQuery.execute(query4)
myResult4= myQuery.fetchall()
for x in myResult4:
    femaleDeath = femaleDeath+1
    print(femaleDeath)
w = 0.4
xLabel=["Male", "Female"]
Male = [maleSurvived, femaleSurvived]
Female = [maleDeath, femaleDeath]
barl = np.arange(len(xLabel))
bar2 = [i+w for i in bar l]
plt.bar(barl, Male, w, label="Survived")
plt.bar(bar2, Female, w, label="Death")

plt.xlabel("")
plt.ylabel()
plt.xticks(bar1+w/2, xLabel)
plt.legend()
plt.show()