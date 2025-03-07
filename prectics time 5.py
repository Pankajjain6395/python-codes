words = {"madad": "help", 
         "kushi": "happy", "kurshi":"chair", 
         "kithab":"book"}


word = input("Enter the words you want meaning of:")


print(words[word])


# problem 2

s = set()

n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))




# problem 3

s = set()
s.add(18)
s.add("18")


print(s)      #yes


#problem 4

p= set() 
p.add(20) 
p.add(20.0) 
p.add('20') # length of s after these operations? 


print(p)
 

print(len(p))

#problem 5

s= {}
print(type(s))   # this is set dictionary not set


#problem 6

d = {}


name = input("Enter the name:")
lang = input("Enter the lang:")

d.update({name:lang})

name = input("Enter the name:")
lang = input("Enter the lang:")

d.update({name:lang})

name = input("Enter the name:")
lang = input("Enter the lang:")

d.update({name:lang})

name = input("Enter the name:")
lang = input("Enter the lang:")

d.update({name:lang})

print(d)