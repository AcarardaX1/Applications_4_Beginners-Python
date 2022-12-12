course = 'Python for "Beginners"'
print(course)
print(course[0])
print(course[0:]) 
print(course[2:]) #Applications with elements of a string
print(course[:1])
print(course[0:3]) 
print(course[:]) #  = another = course[:] can also be written


xy = """

Hi John,

We reached out you through your email address.

We would like to inform you that you have been selected for the interview. 

Hope to see you soon

Thanks & Regards,

"""
print(xy)  #String with multiple lines


name = 'Jennifer'
print(name[1:-1]) #listing factors

first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(first,last)
print(message)
msg = f'{first} [{last}] is a coder'    #listing factors 2
print(msg)
print(msg[1])

coursename = 'Python for Beginners'
print(len(coursename))
print(coursename.upper())
print(coursename.lower())
print(coursename.title())  #listing factors 3
print(coursename.find('P'))
print(coursename.replace('Beginners', 'Absolute Beginners'))
print(coursename.replace("Beginners", "Professionals"))
print(type(print("Python" in coursename)))
print("PythoN" in coursename)
print("Python" not in coursename)
print("Python" in coursename)

print(float(10/3))
print(not bool(10/3)) #arirhmetic operations
print(bool(10/3))
print(int(10/3))

print(10//3) #floor division
print(10%3) #remainder     #arithmetic operations 2
print(10**3) #exponent

x=10
x = x+3 #Increment Operation
print(x)

y = 10
y -= 3 #Decrement Operation
print(y)

l = 10 + 3 * 2
print(l)    #Addition, Multiplication


g = 2.9
print(round(g)) #Rounding
print(abs(-2.9)) #Absolute Value

