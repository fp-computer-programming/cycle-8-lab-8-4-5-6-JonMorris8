"""
Create a Python file named lab_8-4.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a function count_a(word) that takes in a string word and returns the number of a's in the word. 
The function should count both lowercase (a) and uppercase (A)
_____________________________________________________________________________________

Create a Python file named lab_8-5.py

Write a function factorial(num) that takes in a number num 
and returns the product of all numbers from 1 up to and including num

_______________________________________________________________________________________

Create a Python file named lab_8-6.py

Write a function is_palindrome(word) that takes in a string word 
and returns the true if the word is a palindrome, false otherwise. 

A palindrome is a word that is spelled the same forwards and backwards.



"""
#8-4
#author Jon Morris

def count_a(word):
    #initialize a counter for 'a's
    a_count = 0

    #iterate through each character in the word
    for char in word:
        #check if the character is a a or a A and inceement the counter
        if char == 'a' or char == 'A':
            a_count += 1

            #return final of the 'a's
            return a_count
        

#8-5
        def factorial(num):
            #checl if the input is zero, return 1 as the factorial of 0 is 1
            if num == 0:
                return 1

            #initialize the product variable
            product = 1

            #iterate from 1 to num (inclusive) and calculate the product
            for i in range(1, num+1):
                product += i 

                #return the final product
                return product 
            
#8-6
            def is_palindrome(word):
                #compare the og word with the reverse
                return word == word[::-1]
            
            