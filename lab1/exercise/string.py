#there in no difference between "" and ''
print("hello")
print('hello')

a = """tototo kmlrkm serttyk ytkyf ytkygkf kyfjyf"""
print(a)

a = '''ytyty rihug jgkv kyutuy yk ygyg  y tky kyk'''
print(a)

#strings are arrays
u="hello, world"
print(u[1])

#looping
for x in "banana":
  print(x)

#length
a="fjrfgh"
print(len(a))

#Check
txt = "The best things in life are free!"
print("free" in txt)

#Check if not
txt = "The best things in life are free!"
print("free" not in txt)

#Slicing
d="kjdncdlksdck"
print(d[2:4])

#Slicingfromthestart
h="gsrggsgrtgrgrgsfv"
print(h[:6])

#Slicingtotheend
h="gsrggsgrtgrgrgsfv"
print(h[3:])

#NegativeIndexing
b = "hello world"
print(b[-5:-2])

#uppercase
a = "so i just dance"
print(a.upper())

#lowercase
a="PEANUTBUTTER"
print(a.lower())

#strip
a = " Hello, World! "
print(a.strip())

#replace

a = "Hello, World!"
print(a.replace("d", "r"))

#split
a = "Hello, World!"
print(a.split("W")) 

#Concatenation
a="mon "
b="amour"
c=a+b
print(c)

m="mon"
b="amour"
print(m+" "+b)

#format
a = "no"
txt = "yes {}"
print(txt.format(a))


q = 3
i = 567
p = 49.95
m = "kfgnf {3} kdjn {0} kjndv {1}"
print(m.format(q, i, p))

#Escape Character
q="lmrrf \"gfgfg\" dgmlg"

