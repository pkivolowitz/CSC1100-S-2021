# Times Table

This is an in-class exercise. The end-product is a 1 to 10 times table.

In this short program, you'll see:

* range-based `for` loop
* nested `for` loops
* formatting printing

## `for` loop

The `for` loop is one kind of looping construct in Python. In plain language, the general form reads something like this:

```text
for some_variable in some_enumerable_collection:
    code repeated once for each member of the collection 
```

`for` loops are described in Zybooks chapter 5.5.

## `range`

An easy way to make a collection of integers is with a Python `range()`. `range()` is described in Zybooks chapter 5.6.

The short story is:

```python
range(starting_value, one_beyond_last_desired_value)
```

or

```python
range(starting_value, one_beyond_last_desired_value, increment)
```

To enumerate from 1 to 10:

```python
for i in range(1, 11):
    print(i)
```

To enumerate from 1 to **9** skipping every other value:

```python
for i in range(1, 11, 2):
    print(i)
```

To enumerate from 10 to 1:

```python
for i in range(10, 0, -1):
    print(i)
```

## Nested loops

Loops may be found inside loops. When this happens, it is called *nested* loops.

You have experienced nested loops in your daily living: counting.

When you count, from 0 to 100 for example, you are implementing a nested loop. Counting in the 1's place is a loop from 0 to 9 nested inside a loop counting from 0 to 9 in the 10's place.

In code:

```python
print('beginning outer loop')
for outer_loop_counter in range(0, 10):
    print('beginning inner loop')
    for inner_loop_counter in range(0, 10):
        print('[{}] [{}]'.format(outer_loop_counter, inner_loop_counter))
    print('end of inner loop')
print('end of outer loop')
```

This produces (in part):

```text
beginning outer loop
beginning inner loop
[0] [0]
[0] [1]
[0] [2]
[0] [3]
[0] [4]
[0] [5]
[0] [6]
[0] [7]
[0] [8]
[0] [9]
end of inner loop
beginning inner loop
[1] [0]
[1] [1]
[1] [2]
[1] [3]
[1] [4]
(and so on)
```

A times table is an example of a nested loop. The outer loop is each line. The inner loop is each column.

## Formatting strings

String formatting is found in Zybooks chapter 3.8 and 7.2.

In printing the times table, it is critical that you control the number of spaces in which each value is printed. This can be done via string formatting.

```python
>>> print('{}{}{}'.format(1, 1, 1))
111
>>> print('{:1}{:1}{:1}'.format(1, 1, 1))
111
>>> print('{:1}{:2}{:3}'.format(1, 1, 1))
1 1  1
>>>
```

## Printing with and without a trailing new line

```python
>>> print('hello', end='')
hello>>> 
>>> print('hello')
hello
>>> 
```

## Desired output

```text
perryk@Roci times_table % python3 main.py 
       1   2   3   4   5   6   7   8   9  10
   1   1   2   3   4   5   6   7   8   9  10
   2   2   4   6   8  10  12  14  16  18  20
   3   3   6   9  12  15  18  21  24  27  30
   4   4   8  12  16  20  24  28  32  36  40
   5   5  10  15  20  25  30  35  40  45  50
   6   6  12  18  24  30  36  42  48  54  60
   7   7  14  21  28  35  42  49  56  63  70
   8   8  16  24  32  40  48  56  64  72  80
   9   9  18  27  36  45  54  63  72  81  90
  10  10  20  30  40  50  60  70  80  90 100

perryk@Roci times_table % 
```
