# Deliver
Deliver is a programming language that let you experience delivery

## Main Concept

Deliver runs on a tape of stacks.

Each **Pile** is a stack, there's at least 2560 piless. Each stack at least can contain 256 numbers.

Your **Position** is a number, automatically mod by the number of piles.

Your **Package** is a number, which you can use as a register

A **Routine** is a function i, though you cannot pass value to it or get a return value from it

A **Circuit** is a library.

## Syntax
`Move d` to move by d, d is either a number, TOP, or PACKAGE

`Take the top package from the pile` to take the top value from current pile

`Throw the top package from the pile away` to throw the top package away from the current pile

`Put the package onto the pile` to put your package onto the current pile (i.e. push it into the stack)

`Add the package to the pile` to add your package number to the current pile's top number

`Merge the package to the pile` to multiply your package number to the current pile's top number

`Divide the package to the pile` to divide your package number from the current pile's top number

`Takeaway the package from the pile` to minus your package number from the current pile's top number

`Let the package to be x` to set your package to x, x is either a number or TOP or PACKAGE

`If the pile has no package` to start a if, check if the current pile has no package

`If the pile has packages` to start a if, check if the current pile has packages

`If the pile's top package is x` to start a if, check if the current pile's top number is x, x is either a number or TOP or PACKAGE

`If the pile's top package is not x` to start a if, check if the current pile's top number is not x, x is either a number or TOP or PACKAGE

`End` to end a if or a note

`Report package id` to output a number which equals to the package

`Report package name` to output a character which Unicode value equals to the package number

`Routine x:` to record a routine, named with x

`Follow the routine x` to follow a routine recordeded earlier named x

`Follow the circuit x` to follow a circuit (i.e. import a library)

## Computational Class
Deliver is turing complete, because you can simulate BF in it.

## Example(s)
a + b:
```
Require package id
Put the package onto the pile
Require package id
Add the package to the pile
Take the top package from the pile
Report package id 
```
