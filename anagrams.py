from Testing_Platform import Testing_Platform 

a = "racecar"
a_a = "racecar"

b = "Debit card"
b_b = "Bad credit"

# different size
c = "School master"
c_c ="The clasroom"

d = "School master"
d_d ="The claesroom"

e = None
e_e = "Hello"

f = "Hello"
f_f = None

g = "hello"
g_g = "hello"

h = ""
h_h = ""

test_cases = [(a,a_a), (b, b_b), (c,c_c), (d, d_d), (e, e_e), (f, f_f), (g, g_g), (h, h_h)]
test_answers = [True, True, False, False, False, False, False, True]

def anagrams((string1, string2)):
	

	if string1 == None or string2 == None:
		return False

	if not len(string1) == len(string2):
		return False

	if len(string1) == 0 and len(string2) == 0:
		return True

	# Sanatize the strings
	string1 = string1.strip().lower()
	string2 = string2.strip().lower()

	char_map = {}

	for char in string1:
		if not char in char_map.keys():
			char_map[char] = 1
		else:
			char_map[char] += 1

	for char in string2:
		if char in char_map.keys():
			char_map[char] -= 1

			if char_map[char] == -1:
				return False	
		else:
			return False

	return True


test_platform = Testing_Platform(test_cases, test_answers, anagrams)

test_platform.run_test()

