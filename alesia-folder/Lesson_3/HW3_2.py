
a = "do"
b = "ing"
print("Verb + ing", "\nFor example: do + ing = ", a + b)
# print("do + ing = ", a + b)

v = input("\nType a verb: ")
d = len(v)
if v == "be":
    (print("Gerund of '", v, "' is ", "'being'", sep="")
     & exit(code=None))
if v.endswith("ee"):
    (print("Gerund of '", v, "' is '",  v, "ing'", sep="")
     & exit(code=None))
if v.endswith("ie"):
    (print("Gerund of '", v, "' is '", v.replace("ie", "ying'"), sep="")
     & exit(code=None))
if v.endswith("y"):
    (print("Gerund of '", v, "' is '",  v, "ing'", sep="")
    & exit(code=None))
if v.endswith("e"):
    (print("Gerund of '", v, "' is '", v.replace(v[d - 1], "ing'"), sep=""))
else: (print("Gerund of '", v, "' is '",  v, "ing'", sep=""))

# TODO cases with -r, -l, -m
# print(c + "ing")

