def permute(s):
    ans = []
    def solve(curr, remaining):
        if len(remaining) == 0:
            ans.append(curr)
            return

        for i in range(len(remaining)):
            ch = remaining[i]
            new_remaining = remaining[:i] + remaining[i+1:]

            solve(curr + ch, new_remaining)

    solve("", s)
    return ans

print(permute("abc"))
print(permute("ab"))



