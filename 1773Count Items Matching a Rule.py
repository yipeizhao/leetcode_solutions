def Solution(items,ruleKey,ruleValue):
    dic = {
        'type':0,
        'color':1,
        'name':2
        }
    lst = [1 for item in items if item[dic[ruleKey]]==ruleValue]
    return sum(lst)

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
print(Solution(items, ruleKey, ruleValue))