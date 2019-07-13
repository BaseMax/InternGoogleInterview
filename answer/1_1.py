###
 #
 # @Name : InternGoogleInterview/1_1.py
 # @Version : 1.0
 # @Programmer : Max
 # @Date : 2019-07-13
 # @Released under : https://github.com/BaseMax/InternGoogleInterview/blob/master/LICENSE
 # @Repository : https://github.com/BaseMax/InternGoogleInterview
 #
 ###
def check(a, b):
	n=len(a)
	m=len(b)
	for i in range(1,1000):
		if b in (a * i):
			return i
	# This does not optimize.
	return -1
print( check("abcd", "cdabcdab") ) # 3
print( check("abcd", "cdabcdabx") ) # -1

