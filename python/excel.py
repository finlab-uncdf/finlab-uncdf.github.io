import csv

title_t = ""

def ulify(elements):
    string = "<ul>\n"
    for s in elements:
        string += "<li>" + str(s) + "</li>\n"
    string += "</ul>"
    return string

with open('uncdf.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    name = []
    about = []
    for row in readCSV:
        name_n = row[7]
        name.append(name_n)

for index in range(2, len(name)):
    title_t = name[index]
    splitty = title_t.split("\n")
#    print splitty
    print(ulify(splitty))
    
    


#print(ulify(splitty))