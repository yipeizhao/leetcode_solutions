def solution(version1,version2):
    version1 = version1.split('.')
    version2 = version2.split('.')
    version1 = [int(item) for item in version1]
    version2 = [int(item) for item in version2]
    for i in range(min(len(version1),len(version2))):
        if version1[i]>version2[i]:
            return 1
        elif version1[i]<version2[i]:
            return -1    
    version1 = version1[i+1:]
    version2 = version2[i+1:]
    if len(version1)==0 and sum(version2)!=0:
        return -1
    elif len(version2)==0 and sum(version1)!=0:
        return 1
    return 0
version1 = "0.1"; version2 = "1.1"
print(solution(version1,version2))