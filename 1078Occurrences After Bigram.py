def Solution(text,first,second):
    res = []
    
    text=list(text.split(' '))
    for i in range(len(text)-2):
        if text[i] == first and text[i+1]== second:
            res.append(text[i+2])
    return res
            

text = "alice is a good girl she is a good student"
first = "a"
second = "good"

print(Solution(text, first, second))