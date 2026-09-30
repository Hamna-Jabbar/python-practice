#Basic input
name=input("Enter your name:")
print(name)

#input+message
name=input("what is your name?")
print("hello",name)

age=int(input("Enter your age"))
print(age)

#take two number input
a=int(input("Enter first number"))
b=int(input("Enter second number"))
print(a+b)

#mini task 
a=input("Enter your name")
b=int(input("Enter your age"))
print("my name is",a,"i am",b,"years old")

#calculator
h=int(input("Enter your first number"))
j=int(input("Enter your second number"))
print("addition=",h+j)
print("subtraction=",h-j)
print("multiplication=",h*j)
print("division=",h/j)
print("remainder=",h%j)
print(" floor division=",h//j)
print("power=",h**j)

#comparison operrator

#| Operator | Meaning        |
#| -------- | -------------- |
#| `>`      | bara           |
#| `<`      | chota          |
#| `>=`     | bara ya equal  |
#| `<=`     | chota ya equal |
#| `==`     | equal          |
#| `!=`     | not equal      |

#let use it
age=int(input("Enter your age:"))
print(age>=20) 

#if
age=int(input("Enter your age:")) 
if age>=20:
  print("you are an adult")

marks=int(input("Enter your marks:"))
if marks>=50:
  print("PASSED")

  #if else
age=int(input("Enter your age:")) 
if age>=20:
  print("you are an adult")
else:
  print("you are under 20")

marks=int(input("Enter your marks:"))
if marks>=50:
  print("PASSED")
else:
  print("FAILED")

#elif (Jab humein 2 se zyada possibilities check karni hon, elif use karte hain.)
age=int(input("Enter your age"))
if age>=18:
  print("your are adult")
elif age>=13:
  print("you are teenager")
else:
  print("child")
  