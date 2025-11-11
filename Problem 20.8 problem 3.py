f = open("aliceBook.txt")
content = f.read()
worddic = {}
wordlist = content.split()
for words in wordlist:
    worddic[words] = worddic.get(words, 0)+1

for k in worddic.keys():
    print(k, worddic[k])
    


















        
    


