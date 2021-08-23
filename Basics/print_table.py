countries = [
    "United States", "Germany", "Canada", "Norway", "Austria", "Russia"
]

golds = [9, 10, 14, 9, 4, 3]
silvers = [15, 13, 7, 8, 6, 5]
bronzes = [13, 7, 5 ,6 ,6, 7]

data = []
longest_name = 0
for i in range(len(countries)):
    d = [countries[i], golds[i]+silvers[i]+bronzes[i]]

    data.append(d)


def print_table(table):
    output = "No.\tCountry\t\tTotal Medal\n"
    for i in range(len(table)):
        output += "{:<10}{:10}\t\t{}\n".format(i+1, table[i][0], table[i][1], )

    print output

print_table(data)