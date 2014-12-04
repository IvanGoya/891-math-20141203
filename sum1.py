#!/usr/bin/python

x = int(raw_input("what is your lower limit? "))
y = int(raw_input("what is your higher limit? "))
def sum(x,y):
		ans = 0.0
		for i in range(x,y+1):
			a = float((1)/(i**2))
			ans += a
		return ans
print sum(x,y)

