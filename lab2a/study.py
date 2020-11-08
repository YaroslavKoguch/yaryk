print("this is True:", True)
print("this is False:", False)
print("-12.5 є рівним {}".format(int(-12.5)))
a = 'dds'
if type(a) == int:
    print("this is int")
else:
    print("this is str")
for i in range(2,10,2):
    print(i)

d = 'str'
try:
    print("Що буде якщо", d*2 - d, "?")
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")
with open("readme.md", "w") as ar:
    ar.write("це не той readme.md, спробуйте з Caps Lock")

ar = lambda x: hex(x)
print(ar(33))

