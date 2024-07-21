

def longestCommonPrefix(strs: list[str]) -> str:
    longestComPrefix = ""
    strs = sorted(strs)

    first = strs[0]
    last = strs[-1]

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return longestComPrefix
        longestComPrefix += first[i]
    return longestComPrefix


print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["a"]))
print(longestCommonPrefix(["", ""]))
