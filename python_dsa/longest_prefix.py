strs = ["flower", "flow", "flight", "fact"]
# strs = ["dog","racecar","car"]

pref = strs[0]
pref_len = len(pref)
ans = pref

for letter in strs[1:]:
    while pref != letter[0:pref_len]:  # fl != fl len = 2
        pref_len -= 1
        if pref_len == 0:
            ans = ""
        pref = pref[0:pref_len]

ans = pref
print(ans)
