class Test:
    """This is a Test."""

    def __init__(self,
                 test_number,
                 test_name):
        self.test_number = test_number
        self.test_name = test_name

    def write_test_info(self):
        info = f"The name of the test is {self.test_name}: {self.test_number}"

        print(info)
        return self.test_number + 1


test1 = Test(1, "Firstly,")
answer1 = test1.write_test_info()
print(f"the next test is: {answer1}")
test2 = Test(2, "Secondly,")
answer2 = test2.write_test_info()
print(f"the next test is: {answer2}")
test3 = Test(3, "Thirdly,")
answer3 = test3.write_test_info()
print(f"the next test is: {answer3}")
test4 = Test(4, "Fourthly")
answer4 = test4.write_test_info()
print(f"the next test is: {answer4}")
