# CSC1100 Project 2 - Frequency Distribution from a Pair of Dice

In this project you'll simulate throwing two six-sided dice. You'll record the outcome into a data structure, repeating the experiement some user specified number of times. With every tenth simulation, you'll present the accumulating results showing the chance of throwing 2 through 12.

This project will feature:

- use of a list of integers, each member counting the number of times a particular outcome was rolled
- use of the random number generator (already seen in project 1)
- sophisticated use of string formatting
- use of a function
- use of a `for` loop
- some extremely old-school screen formatting

## The data structure

You will accumulate the results of the simulation in a list of integers. We'll take some liberties with the list's construction so as to make the program a bit more straight forward to write.

Specifically, you'll note that two six sided die summed together create 11 potential outcomes that do **not** start numbering from 0. Rather, the potential outcomes are 2 through 12 inclusive. It would be nice if we could use the sum of the two dice directly as the index into the list. But we cannot because indicies start at 0 but the sum of two six sided die starts at 2.

The liberty we'll take is to create the list with 13 members leaving cells 0 and 1 alone so that we can directly use indexes 2 through 12.

See Zybooks chapter 3.2 for an introduction to lists. Here is some helpful additional information.

### Creating a list of length *n*

You need a list 13 members long. Rather than creating the list like this:

```python
histogram = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
```

you can use a shorthand:

```python
histogram = [ 0 ] * 13
```

This says, make 13 cells each containing the initial value of 0.

## `randint()` review

To get random integers, you must import first:

```python
import random
```

or

```python
from random import randint
```

```randint()``` requires two parameters, the first being the minimum value desired and the second being the maximum value desired.

## String formatting

Here is a sample of the final output of an invocation of the program:

```text
100000 trials
[ 2]  2.82%
[ 3]  5.58%
[ 4]  8.32%
[ 5] 11.00%
[ 6] 13.76%
[ 7] 16.80%
[ 8] 13.89%
[ 9] 11.16%
[10]  8.33%
[11]  5.51%
[12]  2.82%
```

For each of the lines of computed output, there are two spaces set aside inside the brackets even though some of the numbers only require one space. Then, each of the percentages are printed within five spaces and each has specifically two places after the decimal point.

There are many ways of performing this kind of formatting within Python. We're learning the style described in Zybooks chapter 3.8.

## Use of a `for` loop with a `range`

You'll ask the user how many simulations they would like to run. Then, use a `for` loop enumerating over the appropriate `range`. This is described in Zybooks chapter 5.6.

## Writing your own function

Functions are a critical part of the Python language. They allow logically related code to be bundled up into a reusuable and customizable box. The entire chapter 6 of the Zybook is related to functions, but all you'll need to know for this project is contained in 6.1.

The function you will write is called `PrintHistogram()`. It will take two parameters, a similation number and the histogram list. It is declared in this way:

```python
def PrintHistogram(t, histogram):
```

It makes sense to make this a function because you'll need to print the histogram from two locations in your program. Once will be inside the loop that enumerates all the simulations. The `PrintHistogram()` function should be called for every tenth simulation. Second, you'll need to call `PrintHistogram()` just prior to exiting the program, after the loop.

The reason you'll need to call this function in two places is this: Suppose the user asks for a number of simulations which is not a multiple of ten? Inside the loop, you'll call the function every tenth simulation - what about the leftover?

## Some *really old school* tech

Every tenth simulation, you'll print more than ten lines of output. So, if the user wanted a big number of simulations, you'd get a LOT of output. Instead of scrolling and scrolling, what we'll do is use from really old school tech (from the late 1970's) to reposition the curses to the top left of a console window, erase the screen, and then finally print the data.

See [here](https://youtu.be/b9WdDyUsI9Q).

You'll make use of [ANSI ESCAPE SEQUENCES](https://en.wikipedia.org/wiki/ANSI_escape_code).

Specifically:

```python
print('\033[1;1H', end='')
print('\033[2J', end='')
```

The first print statement moves the cursor to row 1 column 1. The second erases the screen.

These work on Linux consoles and other systems derived from Unix such as MacOS. This will not work on Windows consoles because Microsoft. Repl.it uses a Linux console, so it works on Repl.it.

## Example of output

See above for a video.

## Work rules

All work is to be done solo.

## What to hand in

Just the Python program, using Schoology. Make sure your name is embedded as a comment at the top of the file.
