def minheapify(arr,i):
	left=2*i+1
	right=2*i+2
	n=len(arr)

	if left<=len-1 and arr[left]<arr[i]:
		smallest=left
	if right<=len-1 and arr[right]<arr[smallest]:
		smallest=right

	if smallest!=i:
		arr[smallest],arr[i]=arr[i],arr[smallest]
	minheapify(arr,smallest)


arr=[2,4,5,1,7,10]
n=len(arr)
for i in reversed(range(n//2)):
	minheapify(arr,i)