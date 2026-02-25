# Python Exercise 6

# Lab #1

1. Open your Pycharm project `Python2026` from your main `python` folder.

1. Create a new weekly project folder called `Ex6` -  (<kbd>File</kbd> ... <kbd>New...</kbd> ... <kbd>Directory</kbd>):

## Part 1 - File Handling

1.  In your `Ex6` folder create a text file called `fruit.txt` with the content shown here:

    `- fruit.txt -`
    ```
    Apples
    Pears
    Oranges
    ```

2.  In your `Ex6` folder create a Python program called `file1.py` to print the contents of `fruit.txt` below:
    
    Expected output:
    ```
    Apples
    Pears
    Oranges
    ```

    Get into the habit of always closing your data files with `close()` function.

3.  In your `Ex6` folder create a Python program called `file2.py` to print the contents of `fruit.txt` below:

    Expected output:
    ```
    1. Apples

    2. Pears

    3. Oranges    
    ```

4.  Modify `file2.py` to print the contents of `fruit.txt` like below:

    Expected output:
    ```
    1. Apples
    2. Pears
    3. Oranges    
    ```

    > The `print()` function has a `end` argument that will help :wink: 

1.  In your `Ex6` folder create a text file called `numbers.txt` with the content shown here:

    `- numbers.txt -`
    ```
    1
    2
    3
    4
    5
    ```

1.  Write a Python program called `file3.py` to read the numbers from `numbers.txt` and print:

    Expected output:
    ```
    1
    2
    3
    4
    5
    ```

6.  Write a Python program `file4.py` to read the numbers from `numbers.txt` and print the total and average values:

    Expected output:
    ```
    There are 5 numbers in numbers.txt
    Total = 15
    Average = 3.0
    ```

6.  Write a Python program `file5.py` to read the numbers from `numbers.txt`, add them to a Python *list* and print the list:

    Expected output:
    ```
    [1, 2, 3, 4, 5]
    ```

1.  Write a Python program `file6.py` ask the user to input a new fruit and write it to the `fruit.txt` file:

    Expected Output:
    ```
    Input a new fruit: Bananas
    ```

    `fruits.txt` has Bananas added:
    ```
    Apples
    Pears
    Oranges
    Bananas
    ```


    ```
    Input a new fruit: Grapes
    ```

    `fruits.txt` has Grapes added:
    ```
    Apples
    Pears
    Oranges
    Bananas
    Grapes
    ```

    > Run the program at least twice to add a new fruit.

1.  Write a Python program `file7.py` that writes names from a Python list to a new file called `names.txt`:

    ```python
    names = ["Alice", "Bob", "Charlie"]
    ```

    Expected `names.txt` file:
    ```
    Alice
    Bob
    Charlie
    ```


