# string literals
print("The {} {} {}".format("car", "yellow", "fast"))  # empty braces
# The car yellow fast
print("The {2} {1} {0}".format("car", "yellow", "fast"))  # index
# The fast yellow car
print("The {f} {y} {c}".format(c="car", y="yellow", f="fast"))
# The fast yellow car

name = "Peter"
print(f"Nice to meet you, {name}")


#####################################################
# text wrapping:
s_var = "pepe"

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" + s_var + "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"


print(s)


#####################################################


m = (
    "https://ja.wikipedia.org/wiki/"
    "%E3%83%97%E3%83%AD%E3%82%B0%E3%83"
    "%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E"
)


print(m)


#####################################################


r = (
    "https://ja.wikipedia.org/wiki/"
    "%E3%83%97%E3%83%AD%E3%82%B0%E3%83"
    "%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E"
)


print(r)
