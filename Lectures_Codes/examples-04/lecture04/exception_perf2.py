import timeit

statements=[
"""\
chars = dict()

for ch in data:
    try:
        chars[ch] = chars[ch] + 1
    except:
        chars[ch] = 1
""",
"""\
chars = dict()

for ch in data:
    if ch in chars:
        chars[ch] = chars[ch] + 1
    else:
        chars[ch] = 1
"""
]

for data in ("abcdefgh", "aaaaaaaa"):
    for s in statements:
        t = timeit.Timer(stmt=s, setup='data="{}"'.format(data))
        print("--------------------------------------------------------------------")
        print("data = {}\n{}".format(data, s))
        print("%.2f usec/pass\n" % (1000000 * t.timeit(number=1000000)/1000000))