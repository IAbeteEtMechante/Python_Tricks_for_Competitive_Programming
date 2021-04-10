
import sys


def ri():
    return int(input())
 
def rl():
    return list(map(int, input().split()))


    
t,n,q = rl()

for test in range(t):
	print("1 2 3")
	sys.stdout.flush()
	judge_answer = ri() - 1
	query = [0,1,2]
	query.remove(judge_answer)
	a,b = query
	ans = [a, judge_answer, b]
	for i in range(3, n):

		k = len(ans)
		for j in range(k-2, -1, -1):
			query = [i, ans[j], ans[j+1]]
			print(" ".join([str(z + 1) for z in query]))
			sys.stdout.flush()
			judge_answer = ri() - 1

			if judge_answer == i:
				ans = ans[:j+1] + [i] + ans[j+1:]
				break

			if judge_answer == ans[j+1]:
				ans = ans[:j+2] + [i] + ans[j+2:]
				break

			if judge_answer == ans[j]:
				continue
		else:
			ans = [i] + ans

	print(" ".join([str(x+1) for x in ans]))

	judge_result = ri()

	if judge_result == -1:
		sys.exit()






