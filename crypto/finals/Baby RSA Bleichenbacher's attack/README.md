# Challenge Summary

Easier Bleichenbacher's attack as padding starts with "00" and not "0002". 

# Challenge Description

RSA padding oracle go brrrr

# Author

Jules (JuliaPoo)

# Hints

Let $m$ be the message (flag), $n$ be the public modulus and $c$ be the `encrypted_flag`. We are going to perform a Binary Search to compute the value of $t = \frac{n}{m}$ to sufficient precision to recover $m$. 

First, let's define a function `is_error(x:int)->bool`. `is_error(x)` will ask the server to decrypt $c x^e \text{ mod } n$, and return `True` if the server encounters an invalid padding. Recall that in RSA, using $c x^e \text{ mod } n$ as the ciphertext will decrypt into the plaintext $m x \text{ mod } n$. Note that the padding check only checks if the first byte of the plaintext is `\x00`. I.e., if the plaintext is smaller than some fixed threshold, then it passes the padding check.

The hint to this challenge will be the answers to the following questions:

- What do you expect `is_error(1)` to return?
- What do you expect `is_error(x)` to return when `x` is a small integer close to `1`?
- As you continue to increase the value of `x`, you'd expect `is_error(x)` to start returning `True`. Eventually, as `x` continues to increase, it will start returning `False` again! (Why?) Let $x_0$ be the value of `x` where this transition occurs, i.e., `is_error(x0) == True` and `is_error(x0 + 1) == False`. What can you infer about $t$ from $x_0$? (Answer: $t \in [x_0, x_0 + 1]$)
- Now let's make the hypothesis that $t \in [x_0, x_0 + 0.5)$. What would you expect `is_error(2*x0 + 1)` to return? What if $t \in [x_0 + 0.5, x_0 + 1]$? Once you've answered this question, you've half-ed the possibilities $t$ can be. This is the start of the Binary Search.
- Suppose from the above question, you've inferred that $t \in [x_0, x_0 + 0.5)$. How would you continue the binary search? I.e., how would you tell if $t \in [x_0, x_0 + 0.25)$ or if $t \in [x_0 + 0.25, x_0 + 0.5]$?
- When do you stop the binary search?

If you're stuck on these questions, no joke, model drawing from primary school can help you visualise the size of each variable.

# Flag

`flag{omg_pwease_dowt_do_twis_to_mwe_pwease}`

# Learning Objectives

A taste of what Bleichenbacher's attack entails.