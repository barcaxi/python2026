# Python Exercise 4

# Lab #1


1. Open your Pycharm project `Python2026` from your main `python` folder.
1. Create a new weekly project folder called `Ex4` -  (<kbd>File</kbd> ... <kbd>New...</kbd> ... <kbd>Directory</kbd>):

## Part 1 - Function Exercises

1.  In your `Ex4` folder create a Python program called `func1.py` to find the square of any number using the a function `sqr()`:

    ```python
    def sqr(...):
        ...


    number = 3
    print(f"sqr({number}) = {...}")
    number = 5
    print(f"sqr({number}) = {...}")
    ```

    Expected Output:
    ```
    sqr(3) = 9
    sqr(5) = 25
    ```

2.  Write a Python program called `func2.py` to find the square of a number input by the user:

    Expected Output:
    ```
    input number to square:3
    sqr(3) = 9
    ```

   
3.  Write a Python program called `func3.py` that defines four functions to perform simple arithmetic on any 2 numbers.  It should allow you to add, subtract, multiply and divide any two numbers:

    ```python
    def add(...):
        return ...


    def sub(...):
        ...


    def mul(...):
        ...


    def div(...):
        ...


    operand1 = 4
    operand2 = 2
    print(f"{operand1} + {operand2} = ...")
    print(f"{operand1} - {operand2} = ...")
    print(f"{operand1} * {operand2} = ...")
    print(f"{operand1} / {operand2} = ...")
    ```

    Expected Output:
    ```
    4 + 2 = 6
    4 - 2 = 2
    4 * 2 = 8
    4 / 2 = 2
    ```

4.  Write a Python program called `func4.py` that defines a function to determine if a given number is odd:

    ```python
    def isOdd(value):             # should return a boolean value
        ...
        ...
    

    number = 3
    if isOdd(number):
        ...
    else:
        ...

    ```

    Expected Output (`number = 3`):
    ```
    3 is odd
    ```

    Expected Output (`number = 4`):
    ```
    4 is even
    ```

5. Write a Python program called `func5.py` that defines a function `string_length()` to return the length of a given string argument.
   
    ```python
    def ...
       ...


    str = "hello"
    print(f"{str} has {string_length(str)} characters")
    ```

    Expected Output:
    ```
    hello has 5 characters
    ```

6. Write a Python program called `func6.py` that defines a function `count_char()` to return the number of times a character appears in a given string.
   
    ```python
    def count_char(character, string):
        ...


    value = "hello"
    character = 'l'
    ...
    ...    
    ```

    Expected Output:
    ```
    hello has 2 'l' character(s)
    ```

1. Write a Python program called `func7.py` that defines a function `mul_table()` that when passed a number will print a multiplication table for that number.

    Expected Output :
    ```    
    input a number:10

    Multiplication Table for 10
    10	*	1	=	10
    10	*	2	=	20
    10	*	3	=	30
    10	*	4	=	40
    10	*	5	=	50
    10	*	6	=	60
    10	*	7	=	70
    10	*	8	=	80
    10	*	9	=	90
    10	*	10	=	100
    10	*	11	=	110
    10	*	12	=	120
    ```

## Part 2 - Additional Function Exercises

1.  Write a method called ``displayStars()`` which will accept an integer value ``n`` and will display ``n`` stars on screen.

    Expected Output :
    ```    
    input number of stars:5

    *****
    ```

    Test your code.

1.  Write a Python program called `max.py` that defines a function `max()` to return the largest of any 2 numbers passed to it.
   
    ```python
    def max(num1, num2):
        ...
        ...

    print(f"The largest number is {max(10,20)}")
    ```

    Expected Output:
    ```
    The largest number is 20
    ```

    Test `max()` works with different values.

1.  Write a Python program called `prices.py` that defines a function `prices()` that takes 3 values representing the price of
3 different books.  The function will return the total price of these books.  If the total price is greater than 50 a 10% discount will be given.  

    Write a Python program that:
    - inputs in the price of 3 different books from the user
    - calls this ``prices()`` function to get the total amount owed
    - displays this total

    Assume prices input have no decimal values.

    Expected Output #1:
    ```
    Input price of book #1: 20
    Input price of book #2: 20
    Input price of book #3: 10
    Total price = 50
    ```

    Expected Output #2:
    ```
    Input price of book #1: 10
    Input price of book #2: 20
    Input price of book #3: 30
    Total price = 54.0
    ```

1.  Write a Python program called `tax.py` that defines a function `calculate_tax()` to calculate tax payable on an income value.  The function `calculate_tax()` will be passed a total income value and returns the tax payable based upon 2 bands of income.

    ```python
    def calculate_tax(income):
        ...
        ...
        ...

    income = input("Input income:")
    print(f"Tax payable = ...")
    ```


    | Income Band  | Tax %  |
    |---|---|
    | 0-40,000  | @20%  |
    | >40,000  | @40%  |

    *Example 1*
    Total Income = 30,000, tax payable = 30,000 x 20% = 6,000
    
    *Example 2*
    Total Income = 50,000, tax payable = (40,000 x 20%) + (10,000 x 40%) = 8,000 + 4,000 = 12,000

    Expected Output #1:
    ```
    Input income: 30000
    Tax payable = 6000.0
    ```

    Expected Output #2:
    ```
    Input income: 50000
    Tax payable = 12000.0
    ```





