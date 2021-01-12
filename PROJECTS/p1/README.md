# CSC1100 Project 1 - Rock Paper Scissors

You will implement a text-based version of [Rock Paper Scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors#American_court_case).

Your program will run just one iteration (or game).

The program will ask for the user's choice of one of "Rock", "Paper" or "Scissors". If the user enters anything other than these three mutually exclusive choices, the program will print and error (and terminate).

If the user enters an allowable input, the program will compute and print the results of the game.

## Getting input

Please see zybooks chapter 1.3 for using the Python function `input()`.

## Choosing the computer's move

Please see zybooks chapter 5.3 for a discussion of `randint()`. As this chapter is deep inside the zybook, an explanation of choosing a random integer is provided below:

### `random` module

Python's random number generation functions are found in module `random`.

If you:

```python
import random
```

you can use:

```python
random.randint(minimum_value, maximum_value)
```

to get one random integer between `minimum_value` and `maximum_value` inclusive.

Or, if you:

```python
from random import randint
```

you can be slightly more concise:

```python
randint(minimum_value, maximum_value)
```

You can find the official documentation for the random number module [here](https://docs.python.org/3/library/random.html).

### Using a random number to select from allowable moves

If you create a `list` with the allowable moves of `Rock`, `Paper` and `Scissors`, the list's members are indexed by 0, 1 and 2. Use the random integer to fetch one of the values in the list.

Python lists are described in detail in zybooks chapter 3.2. However, this will get you started:

```python
lst = []                 # lst gets an empty list
lst = ["Foo", "Bar"]     # lst gets a list with two items indexed 0 and 1
a = lst[randint(0,1)]    # a gets "Foo" or "Bar"
```

## Short cut for vetting the user's input

You will already have a list containing the allowable moves. Rather than testing the user's input against each of the allowable moves individually, you can test against the whole list.

```python
choices = [ "Pears", "Apples"]
user_choice = "Butter"
if user_choice not in choices:
	print("Bad choice")
```

## Exiting a program prematurely

Use `exit()` to exit a program immediately. Note that `exit()` takes an optional integer argument. If your program is exiting with an error, the common value to give to `exit()` is 1. If your program is exiting without an error, the common value to give to `exit()` is 0.

## General hint

Develop your code incrementally - only a line or a couple of lines at a time. Test.

**Write a little, test a little.**

## Rules

| Player 1 | Player 2 | Outcome |
| -------- | -------- | ------- |
| Rock | Rock | Tie |
| Rock | Paper | Paper covers Rock |
| Rock | Scissors | Rock blunts Scissors | 
| Paper | Paper | Tie |
| Paper | Rock | Paper covers Rock |
| Paper | Scissors | Scissors cuts Paper |
| Scissors | Scissors | Tie |
| Scissors | Rock | Rock blunts Scissors |
| Scissors | Paper | Scissors cuts Paper |

## Outline

1. Import anything you'll need
2. Define any lists or other variables you'll need
3. Ask the user for their choice
4. Ensure the choice is a good one - if it isn't, say so and exit
5. Select a computer choice
6. Compute result and print

## Sample output

```text
perryk@Roci pk_rock_paper_scissors % python3 rps.py
Enter one of Rock, Paper or Scissors: Rock
The computer chose Scissors
Rock blunts Scissors
perryk@Roci pk_rock_paper_scissors % python3 rps.py
Enter one of Rock, Paper or Scissors: Paper 
The computer chose Rock
Paper covers Rock
perryk@Roci pk_rock_paper_scissors % python3 rps.py
Enter one of Rock, Paper or Scissors: Paper
The computer chose Paper
Tie
perryk@Roci pk_rock_paper_scissors % python3 rps.py
Enter one of Rock, Paper or Scissors: Paper
The computer chose Scissors
Scissors cut Paper
perryk@Roci pk_rock_paper_scissors % python3 rps.py       
Enter one of Rock, Paper or Scissors: Jar
Jar is not a valid move
perryk@Roci pk_rock_paper_scissors %
```

## Partner rules

Work must be done solo.

## What to turn in

Use schoology to turn in one Python file. Please ensure your name is embedded as a comment at the beginning of the file.

