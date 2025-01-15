from collections import defaultdict
from typing import List

def groupAnagrams(strs):
    result = {}
    for str in strs:
        sortedStr = "".join(sorted(str))
        if sortedStr in result:
            result[sortedStr].append(str)
        else:
            result[sortedStr] = [str]
    print(list(result.values()))

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))