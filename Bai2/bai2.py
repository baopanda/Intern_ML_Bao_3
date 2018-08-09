import csv
import pandas
import matplotlib.pyplot as plt

file = "pokemon.csv"

data = []

with open(file,"r") as filecsv:
    data_csv = csv.reader(filecsv)
    for row in data_csv:
        if(row[0] != "#"):
            data.append(row)
    # data.remove()

df = pandas.DataFrame(data)
columns = ["ID","Name","Type1","Type2","Hp","Attack","Defense","Sp.Atk","Sp.Def","Speed","Generation","Legendary"]
df.columns = columns
print(df)
a = df.query("Attack > '52' and Speed > '80'")
print(a)
print(a[['Name','Attack','Speed']])
print(columns)

x, y = zip(*sorted(zip(a['Attack'], a['Speed'])))
# a.sort_values(['Attack','Speed'])
print(a)

plt.scatter(x,y, color='#2ecc71')

for label, x ,y in zip(a['ID'], a['Attack'], a['Speed']):
    plt.annotate(label,
                 xy=(x,y),  # put the label with its point
                 xytext=(5, -5),  # but slightly offset
                 textcoords='offset points')

plt.title("Diagram with Attack >52 and Speed >80")
plt.xlabel("Attack")
plt.ylabel("Speed")
plt.show()


