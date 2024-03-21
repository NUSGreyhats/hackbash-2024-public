# Challenge Summary

Menu program:
- Option 1 leaks canary if check is met (overflow to pass the check!)
- Option 2 does nothing
- Option 3 is for simple buffer overflowing and executing final payload

# Challenge Description

A canary has been used in history as an early warning for poisonous gases. In the same way, it is also an early warning for stack overflowing.

But, it is not enough! Are you able to bypass the canary?

# Author

uhg

# Hints

Hint 1: Read the functions carefully, would you be able to obtain the canary somehow?

Hint 2: If you knew what the canary's value was, what if you just put it back in place as part of your payload?

# Flag

`flag{i5_1t_4_51n_t0_k1ll_4_c4n4ry???!}`

# Learning Objectives

Learn to read source code and identify the correct vulnerabilities to exploit.

Call 1, overflow from input to password to pass the `strncmp(input, password)`. Basic buffer overflow.

Call 3, buffer overflow, place canary back in place, ret2win. Buffer overflow with canary!
