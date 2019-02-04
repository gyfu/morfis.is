import csv
with open("data/domarar.csv","r") as f:
    lines=csv.reader(f)
    for x in lines:
        if x[1] == "nonni":
            print(x)
