import math

instructions = "LRRRLRLLLLLLLRLRLRRLRRRLRRLRRRLRRLRRRLLRRRLRRLRLRRRLRRLRRRLLRLLRRRLRRRLRLLRLRLRRRLRRLRRLRRLRLRRRLRRLRRRLLRLLRLLRRLRLLRLRRLRLRLRRLRRRLLLRRLRRRLLRRLRLRLRRRLRLRRRLLRLLLRRRLLLRRLLRLLRRLLRLRRRLRLRRLRRLLRRLRLLRLRRRLRRRLRLRRRLRLRLRRLRLRRRLRRRLRRRLRRLRRLRRRLLRLRLLRLLRRRR"


with open("8.txt") as data_file:
	textInputs = data_file.read().split("\n")

# 'MRS = (DSR, DSL)'
# position : (L, R)
myMap = {t[:3] : (t[7:10], t[12:15]) for t in textInputs}

def part1():
	position = "AAA"
	count = 0

	while position != "ZZZ":
		for step in instructions:
			index = 0 if step == "L" else 1
			position = myMap[position][index]
			count += 1

	print(count)

part1()

def part2():
	# ['JVA', 'XLA', 'DNA', 'AAA', 'SHA', 'DLA']
	positions = [key for key in myMap if key[-1] == "A"]
	print(positions)
	counts = []

	for position in positions:
		count = 0

		while position[-1] != "Z":
			for step in instructions:
				index = 0 if step == "L" else 1
				position = myMap[position][index]
				count += 1

		counts.append(count)
	print(counts)
	print(math.lcm(*counts))

part2()



# Some code to investigate cycles

# def backToStart():
# 	position = "JVA"
# 	count = 0

# 	while position != "JVA" or count == 0:
# 		for step in instructions:
# 			index = 0 if step == "L" else 1
# 			position = myMap[position][index]
# 			count += 1

# 			if position[-1] == "Z":
# 				print("at {} in {} steps, instruction was {}".format(position, count, step))

# 	print("back to start in", count)

# backToStart()

