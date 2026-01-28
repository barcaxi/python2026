$$# Python Exercise 2

# Lab #1


1. Open your Pycharm project `Python2025` from your main `python` folder.
1. Create a new weekly project folder called `Ex2` -  (<kbd>File</kbd> ... <kbd>New...</kbd> ... <kbd>Directory</kbd>):

## Part 1 - `if` statement exercises

1. In your `Ex2` folder create a Python program called `if1.py` to input two names and check whether they are equal or not. 
   
   ```
   input name 1:Mary
   input name 2:Bob
   ```
   Expected Output:
   ```
   Mary and Bob are not equal
   ```

1. Write a Python program called `if2.py` to check whether a given number is positive or negative.

    ```
    input a number:15
    ```
    
    Expected Output :
    ```
    15 is a positive number
    ```

1. Write a Python program called `if3.py` to check whether a given number is even or odd. 

    ```
    input a number:15
    ```
    
    Expected Output :
    ```
    15 is an odd number
    ```

1. Write a Python program called `if4.py` to input the age of a person and determine whether they are eligible to vote. 

    ```
    input your age:16
    ```
    
    Expected Output :
    ```
    You are eligible to vote at 18
    ```

1. Write a Python program called `if5.py` to read a temperature in celsius and display a description of the temperature using this table: 

    | temperature   |  description |
    |----------| ---- |
    | < 0 | Freezing 
    | 1-9 | Very Cold 
    | 10-19 | Cold 
    | 20-29 | Normal
    | 30-39 | It's Hot
    | >=40 | It's Very Hot

    ```
    input a temperature:42
    ```
    
    Expected Output :
    ```
    Its very hot.
    ```



1.	Write a Python program called `if6.py` to that allows you to input a mark (0-100) and print the appropriate grade for the given mark.

	| Grade	      | Mark    |
	|-------------|---------|
	| Distinction |	70-100 |
	| Merit 1 	  | 60-69  |
	| Merit 2 	  | 50-59  |
	| Pass 		  | 40-48  |
	| Fail 		  | 0-39   |

    ```
    input a mark:42
    ```
    
    Expected Output :
    ```
    Pass
    ```

	Test the correct grade is displayed even when marks such as 70, 69, 40, 39, etc. are input.

1.	In the previous solution does your code print a message such a *Invalid mark* if a mark greater than 100 or mark less than 0 is input? 
	If NOT, modify your code now to do so.

    ```
    input a mark:101
    ```
    
    Expected Output :
    ```
    Invalid mark input!
    ```

1.	Write a Python program called `if7.py` that allows you to input a number from 1 to 13 that represents card values in a suit of cards. 
	When the number is input it should print the card *face* value.
	
	| Value | Face Value |
	|-------|------------|
	| 1		| Ace        |
	| 2-10	| 2-10      |
	| 11 	| Jack       | 
	| 12	| Queen      |
	| 13	| King       |

	Use an ``if`` statement for this exercise.

    ```
    input a card value:12
    ```
    
    Expected Output :
    ```
    Queen
    ```

	
5.	Write a Python program called `if8.py` that allows the user to input a card value that represents any card in a deck of cards, i.e. 1-52.
	Print the card face value and the suit name.

	| Values | Suit     |
	|--------|----------|
	| 1-13	 | Clubs    |
	| 14-26 | Diamonds |
	| 27-39 | Hearts   |
	| 40-52 | Spades   |
		
    ```
    input a card value:1
    ```
    
    Expected Output :
    ```
    Ace of Clubs
    ```

    ```
    input a card value:15
    ```
    
    Expected Output :
    ```
    2 of Diamonds
    ```
