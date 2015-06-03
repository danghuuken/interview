class Testing_Platform:
	test_cases = []
	test_answers = []
	function = None


	def __init__(self, test_cases, test_answers, function):

		if not len(test_cases) == len(test_answers):
			print "Test Cases and Answers need to be the same length"
			return

		if not hasattr(function, '__call__'):
			print "The third paramter must be a function"
			return

		self.test_cases = test_cases
		self.test_answers = test_answers
		self.function = function

	def run_test(self):

		if len(self.test_answers) == 0 or len(self.test_cases) == 0  or self.function == None:
			print "Testing Platform was not created correctly."
			return

		for i, test_input in enumerate(self.test_cases):

			result = self.function(test_input)

			if test_input == None:
				test_input = " None "

			if result == self.test_answers[i]:
				print "Test " + ' '.join(test_input) + " passed! Result was: %r and expected was %r" % (result, self.test_answers[i])
			else:
				print "Test " + ' '.join(test_input) + " failed! Result was: %r and expected was  %r" % (result, self.test_answers[i])