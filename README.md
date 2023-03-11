# FIZZBUZZ-GAME
QUESTION STATEMENT-

Write a program that prints the numbers from 1 to N. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

Architecture-

In this code, we use a for loop to iterate over the numbers from 1 to N. For each number, we check whether it is divisible by both 3 and 5, or just 3, or just 5, or none of them. Depending on the case, we print "FizzBuzz", "Fizz", "Buzz", or the number itself.
In this code N should be an input from use

Note that the % operator gives the remainder of a division. So, i % 3 == 0 checks whether i is divisible by 3, and i % 5 == 0 checks whether i is divisible by 5. If both conditions are true, then i is divisible by both 3 and 5, and we print "FizzBuzz". If only the first condition is true, then i is divisible by 3 but not 5, and we print "Fizz". If only the second condition is true, then i is divisible by 5 but not 3, and we print "Buzz". If none of the conditions are true, then i is not divisible by 3 or 5, and we print the number itself.
