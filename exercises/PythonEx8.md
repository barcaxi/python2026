# Python Exercise 8

# Lab #1

1. Open your Pycharm project `Python2026` from your main `python` folder.

1. Create a new weekly project folder called `Ex8` -  (<kbd>File</kbd> ... <kbd>New...</kbd> ... <kbd>Directory</kbd>):

## Part 1 - Exceptions

1.  In your `Ex8` folder create a Python program called `except1` with the following code:

    ```python
    try:        
        age = int(input("input your age:"))
        print(age)
    except ValueError:
        print("You didn't enter a valid age")

    print("Program continues")
    ```  
    
    Execute the code once with a valid age value and again with a string value.  Observe the alternative outputs

1.  Create a Python program called `except2` with the following code:

    ```python
    numbers = [1, 2, 3]
    print(numbers[3])
    ```

    Add a `try ... except` block to handle the exception type raised.  Print a message like "You used a list index out of range"  when you handle the exception.

1.  Create a Python program called `except3` with the following code:

    ```python
    f = open("blah.txt")             # blah.txt does not exist
    print(f.read())
    f.close()
    ```

    Run the code.  Add a `try ... except` block to handle the exception type raised.  Print a message like "No such file or directory"  when you handle the exception.

1.  Create a Python program called `except4` with the following code:

    ```python
    names = ["Alice", "Bob", "Charlie"]
    ages  = [19, 20, 0]
   
    age = int(input("input Charlie's age:"))
    ages[3] = age
    ```

    Modify the code to handle both any `ValueError` and `IndexError` exceptions. Print appropriate messages for each.

1.  Create a Python program called `except5` with the following code:

    ```python   
    age = int(input("input your age:"))
    print(age / 0)
    ```

    Modify the code to handle any possible exceptions and print appropriate messages.


2.  Create a Python program called `except6` with the following code:

    ```python
    fruit = ["apples", "pears", "oranges"]

    for i in range(4):
        print(fruit.pop())
    ```  

    Modify the code to handle any possible exception and print appropriate message.

