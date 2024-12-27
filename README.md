# Deliver

Deliver is a programming language that simulate deliver package and put them on piles.

## Before trying
It's my first esolang, so it probably is a little(a LOT) bad

## Main Concept

Deliver runs on a tape of stacks.

Each **Pile** is a stack, there's at least 2560 piles. Each stack at least can contain 256 numbers.

Your **Position** is a number, automatically mod by the number of piles.

Your **Package** is a number, which you can use as a register

A **Routine** is a function i, though you cannot pass value to it or get a return value from it

A **Circuit** is a library.

## Syntax
`Move d` to move by d, d is either a number, TOP, PACKAGE, or a string

`Take the top package from the pile` to take the top value from current pile

`Throw the top package from the pile away` to throw the top package away from the current pile

`Put the package onto the pile` to put your package onto the current pile (i.e. push it into the stack)

`Add the package to the pile` to add your package number to the current pile's top number

`Merge the package to the pile` to multiply your package number to the current pile's top number

`Divide the package to the pile` to divide your package number from the current pile's top number

`Takeaway the package from the pile` to minus your package number from the current pile's top number

`Let the package to be x` to set your package to x, x is either a number or TOP or PACKAGE or a string

`If the pile has no package` to start a if, check if the current pile has no package

`If the pile has packages` to start a if, check if the current pile has packages

`If the pile's top package is x` to start a if, check if the current pile's top number is x, x is either a number or TOP or PACKAGE or a string

`If the pile's top package is not x` to start a if, check if the current pile's top number is not x, x is either a number or TOP or PACKAGE or a string

`End` to end a if or a routine

`Report package id` to output a number which equals to the package

`Report package name` to output a string which value equals to the package number

`Require package id` to input a number which then be assign to the package

`Require package name` to input a string which then be assigned (in integer) to the package

`Routine x:` to record a routine, named with x

`Follow the routine x` to follow a routine recordeded earlier named x

`Follow the circuit` to follow a circuit (i.e. import a library)

`Record routine x as y` to record a routine named with x as a number y, where y is either a number, TOP, PACKAGE or a string

`Follow the record x` to follow a routine numbered x, where x is either a number, TOP, PACKAGE or a string

## How string was treated as number
First of all, Deliver support UTF-8.

Each string is treated as a $256^4$-based number, the least significant bit is the last character.

## Computational Class
Deliver is turing complete if infinite memory is provided, because you can simulate BF in it.

A BF interpreter will soon be implemented

## Example(s)
See examples in the example folder, note that some of them is coded before string-as-number is implemented, so maybe a bit old fashioned.

## STC
STC stands for standard circuit

Now it only includes `PrintLetter.📦`, which has issue(it'll empty the package except for `PrintNewLine`, which is updated)
