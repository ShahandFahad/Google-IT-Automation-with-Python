#!/usr/bin/env python3
"""
Debugging Python Scripts

Introduction
Imagine one of your colleagues has written a Python script that's failing to run correctly. They're asking for your help to debug it. In this lab, you'll look into why the script is crashing and apply the problem-solving steps that we've already learned to get information, find the root cause, and remediate the problem

1. Reproduce the error
2. Find the root cause of the issue
3. Debug the issue


PROBLEM?
    Issue arised due to concatenating int with string in the print statemnet So, fixed it by converting it into string by calling str function.
"""
import random

def greeting():
  name = input("Hello!, What's your name?")
  number = random.randint(1,101)
  # The root casue was concating int with string so,
  # Converted number to string to git rid off the type error
  print("hello " + name + ", your random number is " + str(number))

greeting()