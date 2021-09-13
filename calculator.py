#기본 계산기
def add(a,b):
	return a+b

def subract(a,b):
	return a-b

def multiply(a,b):
	return a*b
	
def divide_new(a,b):
	return a/b

def get_Remainder(a,b):
	return a//b

def test(num):
	if num>0:
		return num
	else:
		return -num


def get_Percent(a,b):
	return (a/b) * 100

def getMedian(a, b):
    return (a+b)/2

def get_Sum_ver1(a,b):
	return n(n+1)/2

def factorial(n):
	num =1
	while n >= 1:
		num = num * n
		n = n -1
	return num