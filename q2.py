def minWindow(s,t):
    if len(t)>len(s):
        return ""
    freq = {}
    for ch in t:
        freq[ch] = freq.get(ch, 0)+1
        left = 0
        count = len(t)
        min_len = float('inf')
        start = 0
        
        for right in range(len(s)):
            ch = s[right]
            if ch in freq:
                if freq[ch]>0:
                    count -= 1 
                freq[ch] -= 1
            while count == 0:
                if right-left + 1 < min_len:
                    min_len = right-left + 1
                    start = left

                left_char  = s[left]
                if left_char in freq:
                    freq[left_char] += 1
                    if freq[left_char] > 0:
                        count += 1
                left += 1

            if min_len == float('inf'):
                return ""
            return s[start:start+min_len]

print(minWindow("ADOBECODEBANC", "ABC"))
print(minWindow("a", "a"))
print(minWindow("a", "aa"))
print(minWindow("aA", "Aa"))
