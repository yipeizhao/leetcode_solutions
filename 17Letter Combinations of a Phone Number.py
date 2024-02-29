def Solution(digits):
    if len(digits)==0:
        return []
    dictionary ={
        '1':'',
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
        }
    res = dictionary[digits[0]]
    if len(digits)==1:
        return res
    for i in range(1,len(digits),1):
        res = cartesian_product(res, dictionary[digits[i]])
        
    return res
def cartesian_product(lst1,lst2):
    res = []
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            res.append(lst1[i]+lst2[j])
    return res

digits = "1"
print(Solution(digits))