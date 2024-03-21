# Challenge Summary

Memory dump analysis using Volatility. 1st stage is preliminary analysis to find username and process list which unlocks 3 remaining challenges

1. Extracting info from notepad process
2. Accessing Google Chrome history to get a Google Drive image and carve out `flag.zip` using `foremost`
3. Reassembling image from Microsoft Paint

# Challenge Description

### Walk Down Memory Lane

You managed to access the memory dump of someone's Windows laptop. Find out whose it is and what they were doing!

The flag contains 3 parts and should be formatted as follows - `flag{<username>_<process_name_1>_<process_name_2>}`

`username` - What is the name of the account used?<br>
`process_name_1` - Name the user process started at 8:33 (without .exe) <br>
`process_name_2` - Name the user process at decimal virtual offset 168292184921408 (without .exe)

[memdump.7z](https://drive.google.com/file/d/1uQsIZh7g1739cKYLynM-jY4de_q6jDFL/view?usp=sharing)

7z password: `do_you_rmb_when`

### Walk Down Memory Lane - 1

greycat wrote some important confidential data in his notes. Find out what was so secret about it

Use the same memory dump from "Walk Down Memory Lane"

### Walk Down Memory Lane - 2

It was found that greycat used some suspicious websites to disseminate some top secret data. The only thing we know is that everyone's favorite browser is Chrome

Use the same memory dump from "Walk Down Memory Lane"

### Walk Down Memory Lane - 3

greycat was bored waiting for his volatility to find the profile of a memory dump so he resorted to drawing some sketches. Maybe he left some suspicious information there too?

Use the same memory dump from "Walk Down Memory Lane"

# Author

jloh02

# Hints

### Walk Down Memory Lane

1. Windows stores files in user directories. Maybe you can find out the user's username using the file path?
2. Try listing the processes using Volatility
3. Convert the decimal number to hexadecimal and find the corresponding virtual offset in the process list

### Walk Down Memory Lane - 2

You can use Volatility 2's `chromehistory` plugin with the profile `Win10x64_17134`

### Walk Down Memory Lane - 3

Try to see what greycat was drawing in Microsoft Paint! The canvas size had a width of approximately 1000-2000px

# Flag

0. flag{greycat_mspaint_notepad}
1. flag{n0w_l_rmb_n0T3p4d_5tr1ngs_4re_l1ttle_eNdI4n}
2. flag{n0w_w3_kn0w_wh4t_y0u_w3re_s34rChlng}
3. flag{greYc4t_4rtworK_r3coveRy}

# Learning Objectives

Volatility memory dump forensics

- Basic process list enumeration
- Process dump analysis Notepad + Microsoft Paint canvas recovery
- Chrome history recovery

- File carving from image
