data = {
    "seid": 10000,
    "Chala": 2000,
    "Abenezer": 4000,
    "Abel": 20000,
    "Kebede": 8000,
    "Mohammed": 5000,
}

table = "| {:^10} | {:^10} | {:^10} | {:^15} |\n".format(
    "Name", "Sell", "Percent", "Fixed Salary")

l = len(table)
table += "{}\n".format('-' * l)

for name, sell in data.items():
    table += "| {:<10} | {:>10} | {:>10} | {:>15} |\n".format(
        name, sell, 0.05, 5000)
    table += "{}\n".format('-' * l)

print table
