#!/usr/bin/python

x = int(raw_input("what is your lower limit? "))
y = int(raw_input("what is your higher limit? "))
def sum(x,y):
		ans = 0.0
		for i in range(x,y+1):
			ans += ((1.0)/(i**2))
		return ans
print "answer = ", sum(x,y)

