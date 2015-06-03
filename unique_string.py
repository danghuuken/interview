from Testing_Platform import Testing_Platform 

a = None
b = ""
c = "a"
d = "aba"
e = "abcdfea"
f = "asdfghj"

test = [a,b,c,d,e,f]
test_answers = [False, False, True, False, False, True]

 
def all_unique_data(input):

	if input == None or len(input) == 0:
		return False 

	if len(input) == 1:
		return True

	map_char = {}

	for char in input:
		if char in map_char.keys():
			return False
		else:
			map_char[char] = 1;

	return True

def all_unique_no_data(input):

	if input == None or len(input) == 0:
		return False 

	if len(input) == 1:
		return True

	for i, char in enumerate(input):
		lead = i +1
		while lead < len(input):
			if char == input[lead]:
				return False
			
			lead += 1

	return True


def run_test(funct):
	for i, test_input in enumerate(test):

		result = funct(test_input)

		if test_input == None:
			test_input = " None "

		if result == test_answers[i]:
			print "Test " + test_input + " passed! Result was: %r and expected was %r" % (result, test_answers[i])
		else:
			print "Test " + test_input + " failed! Result was: %r and expected was  %r" % (result, test_answers[i])

test_platform_data = Testing_Platform(test, test_answers , all_unique_data)
test_platform_data.run_test()
test_platform_no_data = Testing_Platform(test, test_answers , all_unique_no_data)
test_platform_no_data.run_test()

