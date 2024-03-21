## Challenge README Template

PLEASE UPDATE THE LIST OF CHALLENGES BELOW BEFORE YOU PUSH!

Use the template file that is provided in this repository.

1. Challenge Summary _(what the challenge is about)_
2. Challenge Description _(description to put on CTFd)_
3. Author _(the name that will be credited in CTFd)_
4. Hints _(if any, else nil)_
5. Flag
6. Learning Objectives _(key concepts tested, to be learnt)_

## Points to note

- All challenges should come with a solve script (if applicable) for testing, otherwise a very brief overview of the solution.
- For all service challenges, keep the files in two folders `dist` and `deploy`. `dist` will contain the files that will be given to the participants on CTFd. `deploy` will contain the files that will be used to run the challenge on the challenge server.
- Keep in mind that the target audience are mostly participants who are new to CTFs. The CTF challenges shouldn't test way beyond what was covered -- it's fine for the harder challenges to test slightly more (given enough time, participants can google and figure out a way to solve it.)

Look at the slides beforehand if you are unsure about the level of difficulty

List of usable ports: 55000-58000

## List of Challenges for Finals

**Linux & Privilege Escalation**

| Challenge Name | Challenge Summary | Difficulty (1-5) | Port number |
| --- | --- | --- | --- |
| Sanity Check | connect and cat flag.txt | 1 | 57512 |
| kage bunshin no jutsu | many folders, flag appears one character at a time | 2 | 57513 |
| snek | SUID, python library injection | 2 | 57514 - 57533 |


**Pwn / Binary Exploitation**

| Challenge Name | Challenge Summary | Difficulty (1-5) | Port number |
| --- | --- | --- | --- |
| Full Buffer Developer | simple x86\_64 ret2win | 2 | 55432 |
| Give it your all | send more than 0x1000 bytes to SIGSEGV and get flag | 2 | 55433 |
| Stackrunning 2077 | ret2win but correct elements must be placed on the stack | 3 | 55436 |
| Home Run | ret2win with PIE leak (bit shifting/masking) | 4 | 55434 |
| To not kill a canary | buffer overflow + ret2win with canary | 5 | 55435 |

**Crypto**

| Challenge Name | Challenge Summary | Difficulty (1-5) | Port number |
| --- | --- | --- | --- |
| Mahjong Cipher | simple caesar cipher, but using mahjong tiles  | 1 | - |
| My First Encryption | hash lookup and xor (with known flag format) | 2 | - |
| Xor Key | fixed-length xor key | 2 | - |
| Easy Padding Oracle | padding oracle but texts with valid padding are provided | 3 | - |
| Anti-Fermat | Modifying fermat decryption | 4 | - |
| AES-CBC | leak suffix of data by changing prefix | 4 | 55001 |
| Baby RSA Bleichenbacher's attack | Bleichenbacher's attack but padding is easier, allowing a binary search | 5 | 55002 |

**Networking & Forensics**

| Challenge Name | Challenge Summary | Difficulty (1-5) | Port number |
| --- | --- | --- | --- |
| Agent Shadow | ICMP Exfiltration | 3 or 4 | |
| File Extensions | Powerpoint as ZIP file | 1 | |
| a fugacious flag | flag is shown for 0.1 seconds, then deleted from screen. solve by using wireshark to capture, or linux pipes | 2 | 57812 |
| Significant Bits | Hidden file in LSB | 2 | |
| Walk Down Memory Lane | 3-part volatility challenge, enumerating processes, chrome, mspaint | 4 | - |

**Web Exploitation**

| Challenge Name | Challenge Summary | Difficulty (1-5) | Port number |
| --- | --- | --- | --- |
| uno dos tres | html css javascript in CTFd website | 1 | - |
| Secure Login | SQLi in headers | 2 | 55600 |
| Notes App | Command injection | 4 | 55601 |
| Secure Login Secure Flag | UNION SQLi | 3 | 55602 |
| 0xff x slash | Directory Traversal to read flag in .git | 2 | 55603 |
| My Ping Script | command injection blaclist bypass | 1 | 55655 |
| Rotate Picture | file upload vuln to RCE with exif tag | 3 | 55677 |

