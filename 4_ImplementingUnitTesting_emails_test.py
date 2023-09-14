#!/usr/bin/env python3

import unittest    #unittest module provides a framework for systematically creating and executing unit tests.

from emails import find_email    #The following import statement allows a Python file to access the script from another Python file. In this case, we will import the function find_email, which is defined in the script emails.py.

#This test is designed to test the find_email function by providing various test cases and checking if the function behaves as expected.
class EmailsTest(unittest.Testcase):    #define EmailsTest Class
	def test_basic(self):    #define class method within EmailsTest class. Test methods must start with the word "test" and are used to test specific behaviors of the code
		testcase = [None, "Bree", "Campbell"]
		expected = "breee@abc.edu"
		self.assertEqual(find_email(testcase), expected)    #This line calls the find_email function with the test case and then uses self.assertEqual to check if the result matches the expected value

	def test_one_name(self):    #to test the case when only one name is provided in the test case.
		testcase = [None, "John"]
		expected = "Missing parameters"
		self.assertEqual(find_email(testcase), expected)

	def test_two_name(self):    #to test the case when for a name there are no emails found.
		testcase = [None, "Roy", "Cooper"]
		expected = "No email address found"
		self.assertEqual(find_email(testcase), expected)

if __name__ == "__main__":
	unittest.main()    #If the script is being run as the main program, this line invokes the unittest test runner to discover and run the test methods defined in the EmailsTest class.
