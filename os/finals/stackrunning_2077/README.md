# Challenge Summary

Stack overflow, but take note of the stack layout and pass all if statement checks.

# Challenge Description

We have obtained basic access to super secret hackbash servers, but we don't know what to do from here on out. We managed to leak a copy of the source code, but it seems like they were smart. All the variable declarations have been redacted! A little birdie told me you were the best ~~netrunner~~ hacker in the area, could you figure out what to do next?

# Author

uhg

# Hints

Hint 1: What is the program execution flow like? Ensure everything is in order!

# Flag

`flag{b3st_st4ckrunn3r_0f_0ur_t1me_2077!}`

# Learning Objectives

Learn to read source code, understand the stack layout, and execute a slightly modified buffer overflow attack.

Buffer overflow vuln, but all if checks must be passed for program to reach `ret`. Basically a multi-canary ret2win stack overflow but the canaries are spoonfed through the source code.