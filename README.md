## Introduction
This is a python script for testing out the maths in the you tube video. "How Not to Be Wrong: The Power of Mathematical Thinking - with Jordan Ellenberg"

## Game
A ticket consists of 3 digits. A book consists of 7 of these tickets. A win means that either of the 2 conditions is true.
For both the conditions the order of digits is *NOT* important.
* All the 3 digits match in a ticket. Order is not important.
* There are 2 matches with 2 digits. A match with 2 digits is called a deuce. So there are 2 deuces.

Game conitnues till either we have a single book remaining or there is a stalemate. The logic for stalemate is not clear in code.

## Playing the Game

```
python3 play_game.py
```

This will report the number of times it took for the game to terminate.

## Unittests
To run the unittest do
```
python3 test_lottery.py
```
