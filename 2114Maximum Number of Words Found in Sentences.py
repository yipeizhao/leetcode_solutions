def Solution(sentences):
    def find_space(s):
        res = 0
        for item in s:
            if item == ' ':
                res +=1
        return res
    return max([find_space(s) for s in sentences])+1

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(Solution(sentences))