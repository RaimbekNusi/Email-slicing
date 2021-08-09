# Email slicing

## Description

Slicing is the act of selecting zero or more items of a sequence and forming them into a new sequence. Slicing is similar to indexing but it allows us to specify multiple offsets at once using a convenient syntax. The result of slicing is a new sequence consisting of the items at the specified offsets.

## Problem description

An email address is a sequence of characters with the following structure:
- it contains exactly one @ character
- there are 1 or more characters before the @. We call these characters the username
- There is at least one period (.) SOMEWHERE after the @
- IMMEDIATELY after the @ there are one or more characters that are NOT periods. We call all the characters in between the @ and the first-period-after-the-@ the domain

For this question, you will write a program that lets the user type in a valid email address, and reports the username and domain components of that address. Your program may assume that the user always types a correctly-formatted email address.

Here is one possible sample run. Green text was entered by the user, and the blue text is based on that
input.

![image](https://user-images.githubusercontent.com/86201781/128751677-96f718d6-e598-413a-8a1b-d82707285f27.png)

## How to use

Here are the steps for how to open, use and utilize the program:

- First, download all of the files listed above;
- Put all the files in one folder;
- Open the file Projec_pikachu_gengar.py;
- The program will open a command console which will ask you to input an e-mail address.
