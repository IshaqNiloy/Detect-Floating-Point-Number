# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
class Verify():
    def __init__(self, n):
        self.n = n

    def verify_N(self):
        if re.findall('^\+[0-9]+[.][0-9]+$', n) or re.findall('^\-[0-9]+[.][0-9]+$', n) or re.findall('^\.[0-9]+[.][0-9]+$', n) or re.findall('^[0-9]+[.][0-9]+$', n) or re.findall('^\+[.][0-9]+$', n):
            print('True')
        else:
            print('False')


if __name__ == '__main__':
    number_of_test_cases = int(input())

    for i in range(number_of_test_cases):
        n = input()
        my_object = Verify(n)
        my_object.verify_N()
