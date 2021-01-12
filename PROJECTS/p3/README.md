# CSC1100 Project 3 - Counting words with a dictionary

In this project, you'll read the entirety of Mary Shelley's Frankenstein into a Python dictionary.

A dictionary is a mapping of keys to values. In this program, the book's words will serve as keys. The value associated with each key will be the number of times that key is found in the book.

This project will give you practice using:

* text files - see Zybooks chapter 12.1
* slicing - see Zybooks chapter 7.1
* string functions such as `lower()` - see Zybooks chapter 7.3
* dictionaries - see Zybooks chapter 3.4
* `while` loop - see Zybooks chapter 5.2
* `break` - see Zybooks chapter 5.10

## The file

You are given `words.txt`. This file contains the text of Frankstein where each word is given on a line by itself. Here are the first few lines:

```text
Frankenstein
by
Mary
Wollstonecraft
Godwin
Shelley
```

Chapter 12.1 in Zybooks shows the basics of opening a text file for reading using `open()` and `close()` like so:

```python
f = open('file')
# use the file
f.close()
```

You can use this method. You can also use this way:

```python
with open('file') as f:
	# use the file
```

## Reading the file

For simplicity, rather than read the file line by line, let's take advantage of having lots of memory and loading the entire file into memory in one go.

```python
all_words = f.readlines()
```

`all_words` will be a Python `list`. This makes it really easy to enumerate.

## Line endings

`all_words` will contain all the words in the book in order. When reading text, one must be aware of incompatibilities between different operating systems. In this case, in how a line of text is ended. On Linux and Mac OS, text lines are terminated with `\n` - the new line character. On Windows, text lines are terminated with `\r\n` - the return character then the new line character.

Fortunately, Python takes care of this and converts all text lines to end with `\n` no matter what system you're on. Great!

But, there is something special we have to do as the `\n` character will be read into `all_words` at the end of each word like so: `all\n`.

## Slicing

Slicing is discussed in Zybooks chapter 7.1. Slicing works on lists and also on strings. We can use slicing to rid us of the trailing `\n` characters.

```python
w = 'all\n'
w[:-1]
'all'
```

This works and is convenient because the new line is always the last character in each word.

## Smashing to lower case

For the purposes of this project, we'll treat all the words in Frankenstein as case-insensitive. Strings in Python offer a `.lower()` method. A method is a function that is attached to an object. In this case, the object is the string.

```python
w = 'WaLLE'
w
'WaLLE'
w.lower()
'walle'
w
'WaLLE'
```

Notice that using `.lower()` doesn't change the string. If you want to change the string, you need to assign the smashed result.

## Dictionary

You've worked with lists - you know they're lists because Python surrounds them with `[` and `]`. Dictionaries are denoted by `{` and `}`. Here is an empty dictionary:

```python
d = {}
```

Dictionaries, discussed in Zybooks in chapter 3.4, map keys to values.

Here are examples showing use of a dictionary.

```python
>>> d = { 'somekey' : 'some value', 19 : 'another value', 'Somekey' : True }
>>> d
{'somekey': 'some value', 19: 'another value', 'Somekey': True}
>>> d[19]
'another value'
>>> d[19] = 'a changed value'
>>> d[19]
'a changed value'
>>> del(d[19])
>>> d[19]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 19
>>> d['this key does not exist']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'this key does not exist'
>>> 'this key does not exist' in d
False
>>> 'somekey' in d
True
>>> 
```

Notice:

* keys do not have to be all of the same type.
* values do not have to be all of the same type.
* you can modify the value mapped to a key.
* it is an error to refer to a key that is not present
* you can test for the presence or absence of a key
* you can remove a key

## Outline

This program can be divided into two phases:

1. Gather input (read file and build dictionary)
2. Process user input (report results)

### Gather input

Using the open file, read all the lines at once using `.readlines()`. Having done so, use a `for` loop to enumerate the words building the dictionary as you go. In this case, the dictionary will map keys (words) to integers (the count of each word).

Remember it is an error to refer to a key that does not exist. The first time you encounter a word, certainly it does not exist in the dictionary. Consequently, you must test for the presence of a word before simply attempting to increment its value.

Remember to strip new lines and to smash all words to lower case.

### Process user input

In this phase, your program must loop over and over until the user enters "QUIT". The looping construct to use is the `while` loop. Here is a *similar* loop:

```python
while True:
	user_input = int(input('Enter a number [0 quits]: '))
	if user_input == 0:
		break
```

Notice that the loop "will go on forever". At least, until the user enters 0.

Again, this is a *similar* loop - you won't be looking for numbers, for example.

Remember to smash the user's input down to lower case so that it will match the keys in the dictionary.

## Sample output

```text
perryk@Roci pk_count_words_with_dictionary % python3 wc.py 
Enter word to find (QUIT exits): the
the is found 4371 times
Enter word to find (QUIT exits): brown
brown is not found in the book
Enter word to find (QUIT exits): dog
dog is found 2 times
Enter word to find (QUIT exits): jumped
jumped is found 1 time
Enter word to find (QUIT exits): over
over is found 58 times
Enter word to find (QUIT exits): QUIT
perryk@Roci pk_count_words_with_dictionary % 
```

## Work rules

All work is to be done solo.

## What to hand in

Submit to Schoology just your Python source code.
