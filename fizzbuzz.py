"""
The "Fizz-Buzz test" is an interview question designed to help
filter out the 99.5% of programming job candidates who can't
seem to program their way out of a wet paper bag.
The text of the programming assignment is as follows:
    "Write a program that prints the numbers from 1 to 100.
     But for multiples of three print “Fizz” instead of the number
     and for the multiples of five print “Buzz”. For numbers
     which are multiples of both three and five print “FizzBuzz”.
"""


def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


fizzbuzz()
