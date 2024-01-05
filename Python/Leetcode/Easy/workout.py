word1 = "abcd"
word2 = "pqrs"
s=''
if len(word2)>=len(word1):
   l=len(word1)
for i in range(l):
   s+=word1[i]+word2[i] 
   

print(s+word2[l:])