import random

##### 2048 algorithm ##########
def lineSolve(li):
	global SCORE
	global BOOL
	row = len(li)
	li = [i for i in li if i != 0] 
	index = 0
	while index <= len(li) - 2:
		if li[index] == li[index + 1]:
			if BOOL: SCORE += li[index]
			li[index] = li[index + 1] + li[index]
			del li[index + 1]
		index += 1
	for i in range(len(li), row):
		li.append(0)
	return li
	
##### Matrice manipulation #####	
def rot(mat):
	return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat))]
	
def rev(mat):
	return [mat[i][::-1] for i in range(len(mat))]
	
def mSolve(mat):
	return [lineSolve(mat[i]) for i in range(len(mat))]

##### Directions ###############
def left(mat):
	return mSolve(mat)
	
def right(mat):
	return rev(mSolve(rev(mat)))
	
def up(mat):
	return rot(mSolve(rot(mat)))

def down(mat):
	return rot(mSolve(rev(rot(mat))))[::-1]

##### Matrix generator ###########
def genM(row):
	M = [[] for i in range(row)]
	for i in range(row):
		for j in range(row):
			M[i].append(random.randrange(3) * 2)
	return M
	
##### Visual #####################	
def printScreen(mat):
	print()
	for i in range(len(mat)):
		print(mat[i])
	print()	
	
##### Losing condition ###########
def condition(mat):
	global BOOL
	BOOL = False
	return not left(mat) == right(mat) == up(mat) == down(mat)

##### Random insertion ###########
def randomIns(mat):
	tup = [(i,j) for i in range(len(mat)) for j in range(len(mat)) if not mat[i][j]]
	randNb = random.randrange(len(tup))
	mat[tup[randNb][0]][tup[randNb][1]] = 2 * (random.randrange(2) + 1)
	return mat

##### MAIN #######################
def main():
	print("\nStart the game already!")
	global SCORE
	global BOOL
	SCORE = 0
	BOOL = False
	row = 2
	notQuit = True
	mat = genM(row)
	printScreen(mat)
	while condition(mat) and notQuit:
		BOOL = True
		cmd = input("Direction(wasd): ")
		if cmd == "w":
			if mat != up(mat):
				mat = up(mat)
				mat = randomIns(mat)
				printScreen(mat)
			else: print("Error : cannot go up")
		elif cmd == "a":
			if mat != left(mat):
				mat = left(mat)
				mat = randomIns(mat)
				printScreen(mat)
			else: print("Error : cannot go left")
		elif cmd == "s":
			if mat != down(mat):
				mat = down(mat)
				mat = randomIns(mat)
				printScreen(mat)
			else: print("Error : cannot go down")
		elif cmd == "d":
			if mat != right(mat):
				mat = right(mat)
				mat = randomIns(mat)
				printScreen(mat)
			else: print("Error : cannot go right")
		elif cmd == "q":
			print("quitting ...")
			notQuit = False
		else:
			print("Error : invalid command")
		
	if notQuit:print("Game Over")	
	print("Your score is:", SCORE,"\n")
	
		
if __name__ == "__main__":
    main()


