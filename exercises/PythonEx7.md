# Python Exercise 7

# Lab #1

1. Open your Pycharm project `Python2025` from your main `python` folder.

1. Create a new weekly project folder called `Ex7` -  (<kbd>File</kbd> ... <kbd>New...</kbd> ... <kbd>Directory</kbd>):

## Part 1 - Basic JSON

1.  In your `Ex7` folder create a Python program called `player1.py` to convert the Python dictionary below to a JSON string and print it:

    ```
    player = {
        "name": "Lionel Messi",
        "club": "Paris Saint-Germain",
        "country": "Argentina",
        "caps": 164,
        "goals": 90
    }    
    ```  
    Expected output:
    ```
    {"name": "Lionel Messi", "club": "Paris Saint-Germain", "country": "Argentina", "caps": 164, "goals": 90}
    ```

    You must use the `json.dump()` function    

1.  In your `Ex7` folder create a Python program called `player2.py` to convert the Python JSON string below to a dictionary and print details from it:

    ```
    player = '{"name": "Pedri", "club": "FC Barcelona", "country": "Spain", "caps": 14, "goals": 0}'
    ```  
    Expected output:
    ```
    - Player dictionary - 
    {'name': 'Pedri', 'club': 'FC Barcelona', 'country': 'Spain', 'caps': 14, 'goals': 0}

    Pedri plays for FC Barcelona and Spain

    ```

    You must use the `json.load()` function    

3.  In your `Ex7` folder create a Python program called `writePlayer.py` to write the player dictionary for Pedri to a JSON file called `player.json`

    Expected contents in `player.json`:
    ```
    {"name": "Pedri", "club": "FC Barcelona", "country": "Spain", "caps": 14, "goals": 0}
    ```

4.  In your `Ex7` folder create a Python program called `updateGoals.py` to allow you to update the goals value in the `player.json` file.

    Expected Output:
    ```
    Input a new value for goals:1

    ```

    Expected contents in `player.json`:
    ```
    {"name": "Pedri", "club": "FC Barcelona", "country": "Spain", "caps": 14, "goals": 1}
    ```

5.  In your `Ex7` folder create a Python program called `updatePlayer.py` to allow you to update the both caps and goals values in the `player.json` file.

    Expected Output:
    ```
    Input a new value for caps (14):15
    Input a new value for goals (1):2

    ```

    > Notice how the current values are shown inside brackets.

    Expected contents in `player.json`:
    ```
    {"name": "Pedri", "club": "FC Barcelona", "country": "Spain", "caps": 15, "goals": 2}
    ```

# Lab #2

1.  In the project folder called `Ex7`  create a new ``movies.json`` file with this content:

```json
[
  {
    "title": "Gladiator",
    "year": 2000
  },
  {
    "title": "A Beautiful Mind",
    "year": 2001
  },
  {
    "title": "Chicago",
    "year": 2002
  },
  {
    "title": "The Lord of the Rings: The Return of the King",
    "year": 2003
  },
  {
    "title": "The Aviator",
    "year": 2004
  }
]
```

2.  Create and execute a Python program called `moviesPrint.py` with this code:

```python
import json

f = open("movies.json", "r")
movies = json.loads(f.read())
f.close()

for movie in movies:
    print(movie)    
```

3.  Create and execute a Python program called `moviesUpdate.py` with this code:

    ```python
    import json

    f = open("movies.json", "r")
    movies = json.loads(f.read())
    f.close()

    movie = {
        "title": "Slumdog Millionaire",
        "year": 2005
    }

    movies.append(movie)

    f = open('movies.json', "w")
    f.write(json.dumps(movies, indent=4))
    f.close()
    ```

    View the updated `movies.json` file.

4.  Create and execute a new Python program called `moviesByYear.py`.  When executed it should ask the user to input a year and then print movies from that year.

    Expected Output

    ```
    Input year:2005

    -Movies from 2005-
    Slumdog Millionaire

    ```

