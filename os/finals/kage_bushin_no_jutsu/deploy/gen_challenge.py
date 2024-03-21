import os
import random
import shutil

flag = "flag{well_i_hoped_you_didnt_do_this_manually_because_its_a_really_long_flag_hehe_hope_you_enjoyed_xd_see_you_around_this_is_the_end}"

# def make_dirs(cur, depth, final):
#
#     if depth == final:
#         return
#
#     for i in range(10):
#         os.mkdir(f"{cur}/{i}")
#         make_dirs(f"{cur}/{i}", depth+1, final)




os.chdir("./chall")

for i in range(50):
    os.mkdir(f"./{i}")

for i in range(len(flag)):

    x = random.randint(0, 49)
    while (y:=random.randint(0,49)) == x:
        y = random.randint(0, 49)

    os.rmdir(f"{x}")
    with open(f"{x}", "w") as f:
        f.write(flag[i])
    os.chdir(f"{y}")
    for i in range(50):
        os.mkdir(f"./{i}")

