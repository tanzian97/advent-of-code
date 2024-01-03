with open("11.txt") as data_file:
	rows = data_file.read().split("\n")

rowsWithoutGalaxies = []
def getRowsWithoutGalaxies():
	for rowIndex in range(len(rows)):
		isEmpty = True
		for char in rows[rowIndex]:
			if char == "#":
				isEmpty = False
		if isEmpty:
			rowsWithoutGalaxies.append(rowIndex)

getRowsWithoutGalaxies()
print("Rows without galaxies:", rowsWithoutGalaxies)


colsWithoutGalaxies = []
def getColsWithoutGalaxies():
	for colIndex in range(len(rows[0])):
		isEmpty = True
		for row in rows:
			if row[colIndex] == "#":
				isEmpty = False
		if isEmpty:
			colsWithoutGalaxies.append(colIndex)

getColsWithoutGalaxies()
print("Cols without galaxies:", colsWithoutGalaxies)

galaxies = []
def getGalaxies():
	for rowIndex in range(len(rows)):
		for colIndex in range(len(rows[0])):
			if rows[rowIndex][colIndex] == "#":
				galaxies.append((rowIndex, colIndex))

getGalaxies()
# print(galaxies)

def getDistance(galaxy1, galaxy2, scaleFactor):
	smallerRowIndex = min(galaxy1[0], galaxy2[0])
	largerRowIndex = max(galaxy1[0], galaxy2[0])

	smallerColIndex = min(galaxy1[1], galaxy2[1])
	largerColIndex = max(galaxy1[1], galaxy2[1])

	numColsToExpandBetweenGalaxies = 0
	for col in colsWithoutGalaxies:
		if col > smallerColIndex and col < largerColIndex:
			numColsToExpandBetweenGalaxies += 1

	numRowsToExpandBetweenGalaxies = 0
	for row in rowsWithoutGalaxies:
		if row > smallerRowIndex and row < largerRowIndex:
			numRowsToExpandBetweenGalaxies += 1

	return largerRowIndex - smallerRowIndex + largerColIndex - smallerColIndex + (numColsToExpandBetweenGalaxies + numRowsToExpandBetweenGalaxies) * (scaleFactor - 1)

def getTotalDistance(scaleFactor):
	distance = 0
	for i in range(len(galaxies)):
		for j in range(i + 1, len(galaxies)):
			distance += getDistance(galaxies[i], galaxies[j], scaleFactor)
	return distance

print("With scale factor 2, Distance = ", getTotalDistance(2))
print("With scale factor 1000000, Distance =", getTotalDistance(1000000))



# Old code which actually adds the empty space cols/rows to the matrix

# def expandCols():
# 	while colsWithoutGalaxies:
# 		colToExpand = colsWithoutGalaxies.pop()
# 		for rowIndex in range(len(rows)):
# 			rows[rowIndex] = rows[rowIndex][:colToExpand] + "." + rows[rowIndex][colToExpand:]

# expandCols()

# def expandRows():
# 	numCols = len(rows[0])
# 	emptyRow = "." * numCols

# 	while rowsWithoutGalaxies:
# 		rowToExpand = rowsWithoutGalaxies.pop()
# 		rows.insert(rowToExpand, emptyRow)

# expandRows()


