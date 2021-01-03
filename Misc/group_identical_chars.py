from itertools import groupby

ss = "111112222333445"
aa = [x for x in ss]
print("initial list:")
print(aa)

print("groups")
result = [list(grp) for k, grp in groupby(aa)]
print(result)

#just the values
print("\njust the values")
result = [k for k, grp in groupby(aa)]
print(result)

#just the lengths
print("\njust the lengths")
result = [len(list(grp)) for k, grp in groupby(aa)]
print(result)

#combo
print("\ncombo")
result = [(k,len(list(grp))) for k, grp in groupby(aa)]
print(result)