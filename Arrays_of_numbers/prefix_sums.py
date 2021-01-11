
def prefix_sums(aa):
    """
    input an array of numbers aa 
    output prefix sums array
    """
    n = len(aa)
    pp = [0] * n
    pp[0] = aa[0]
    for k in range(1, n):
        pp[k] = pp[k - 1] + aa[k]
    return pp

def count_total(pp, i, j):
    """
    count the sum of aa values from i to j, BOTH i and j included
    """
    return (pp[j] - pp[i - 1] if i > 0 else pp[j])

#example use:
aa = [2,5,4,7,8,3,1,4,2,5,6]
pp = prefix_sums(aa)
print(pp)
print(count_total(pp, 3,6)) #19