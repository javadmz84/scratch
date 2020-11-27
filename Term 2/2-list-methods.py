a = ['amirreza', 'javad', 'setayesh', 'artin', 'iliya']
print(a[4])
print(a[1:4])
print(a[-1])

a.append('sina')
a.append('iliya')
a.append('iliya')
a.append('iliya')
a.append('iliya')

print(a)

print(a.count('iliya'))

print(a.index('iliya'))


a.insert(3, 'Hazhir')
print(a)

print(a.pop())
print(a)

print(a.pop(3))
print(a)

a = [1, 5, 8, 97, 45, 12, 1, 51]
a.sort()
print(a)
b = ['c', 'a', 'A', 'Z', 'z']
b.sort()
print(b)
