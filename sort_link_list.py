a = [4,9,3,1,13,2]
b = []
c = None
d = [1]
e = []
h = [2,4,-3,-6,20,5,-30,1]
g = [1,2,3,3,5,3,10,3,-10]


def sort(list):

	if list == None or len(list) == 0 or len(list) == 1:
		return list 

	current = 0

	while current < len(list):
		mover = current + 1
		minimum = current 

		while mover < len(list):
			if list[current] > list[mover] and list[minimum] > list[mover]:
				minimum = mover

			mover += 1

		temp = list[current]
		list[current] = list[minimum]
		list[minimum] = temp

		current += 1

	return list


print sort(a)
print sort(b)
print sort(c)
print sort(d)
print sort(e)
print sort(h)
print sort(g)



