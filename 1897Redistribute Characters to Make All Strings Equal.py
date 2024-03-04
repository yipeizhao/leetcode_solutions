def Solution(words):
    res = ''
    for item in words:
        res+=item
    chars = list(map(chr, range(97, 123)))
    for item in chars:
        if res.count(item)%len(words)!=0:
            return False
    return True
words = ["abc","aabc","bc",'a']
print(Solution(words))