# Zero Matrix 

def zeroMatrix(arr):
	rows=len(arr)
	cols=len(arr[0])
	if rows==0:
		return arr
	rowZero=False
	colZero=False
	for i in range(rows):
		if arr[i][0]:
			rowZero=True
			break
	for j in range(cols):
		if arr[0][j]:
			colZero=True
			break

	for i in range(1,rows):
		for j in range(1,cols):
			if arr[i][j]==True:
				arr[i][0]=True
				arr[0][j]=True
			else:
				arr[i][j]= arr[i][0] or arr[0][j]

	if rowZero:
		for i in range(rows):
			arr[i][0]=True
	if colZero:
		for j in range(cols):
			arr[0][j]=True

	return arr


arr=[[True,False,False],[False,False,False],[False,False,False]]
print(zeroMatrix(arr))



