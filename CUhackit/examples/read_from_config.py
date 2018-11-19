

tokens = list()

with open("config.dat", "r") as f:
	for line in f:
		tokens.append(line.split(" ")[1].strip("\n"))

for items in tokens:
	print(items)
