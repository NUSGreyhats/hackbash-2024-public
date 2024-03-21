from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime

message = b"XXXXXXXXXXXXXXXXXXXX" # I replaced each character with an `X` HAHAHAHAHA
flag = "flag{" + message.decode() + "}"
m = bytes_to_long(message)
nbits = 632
p,q = getPrime(nbits), getPrime(nbits)
n = p*q
e = 8
c = pow(m, e, n)

print("c =", c)
print("n =", n)
# c = 23965790658009916031696292154239687991326434808126937936323279539527574371744576958848321183942689578488108708090204264281234425279645871337130565890080553808286438515223159187176347615720948597941926154290059517927271273443279014021993150936914996059185621898372665540262508940585954336627247149084360680096370504712966571457587699331961735094863336202844831343021213343719068703
# n = 189837407291613686919566769420272986448887534101748508070907335184348859008673016485968480064813107452336510716209913153290507313137443655096566113288817486410790226639142211212337576873005124899472566893871237221782815126355733037194994994186981409359274410396627201503295100149056825213695727311814873644431153627454770965400706379939864430240987135360486090463455805641835098883
