""" Angry Children - https://www.hackerrank.com/challenges/angry-children
	Reduce the unfairness as much as possible
	N
	K
	A set of n nos

	formula: max(x1,x2,x3 .....) - min(x1,x2,x3....) = unfairness
	choose it such that x1,x2,x3 .. should be combinations of k and the result
	should be minimum
"""

import itertools

def angry_children(n,k,candies):
	candies_combinations = itertools.combinations(candies,k)
	fairness = 100001
	for combination in candies_combinations:
		calc = max(combination) - min(combination)
		if calc < fairness:
			fairness = calc
	return fairness


n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()
result = angry_children(n,k,candies)
print result
#min_diff = ## Write code here to compute the answer using (n, k, candies)

#print min_diff