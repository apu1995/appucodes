n=1000
n1=n/3
n2=n/5
n3=n/15 # which is LCM of 3 and 5
n2=n2-1
ans= ((3*n1*(n1+1))/2) + ((5*n2*(n2+1))/2) - ((15*n3*(n3+1))/2)
# formula used ( Summation )k from 1 to n is n(n+1)/2
print ans