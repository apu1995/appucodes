def generate(s,counta,countb,countc,n,result):
	if counta+countb+countc==n:
		# print(counta,countb,countc)
		result.append(s)
		# print(s)
		return
	if counta+countb+countc<n and counta<n:
		generate(s+"a",counta+1,countb,countc,n,result)
	if counta+countb+countc<n and countb<1:
		generate(s+"b",counta,countb+1,countc,n,result)
	if counta+countb+countc<n and countc<2:
		generate(s+"c",counta,countb,countc+1,n,result)

result=[]
generate("",0,0,0,3,result)
print(result)