classmates = ['Alex', 'Gjon', 'Arbjon', 'Flamur', 'Arbri', 'Arlind', 'Tahir']
classmates.append('Kejdi')
print(classmates)
classmates.insert(0, 'Erald')
print(classmates)
del classmates[2]
print(classmates)
removed = classmates.pop(2)
print(classmates)
print(removed)
classmates.remove('Arbri')
print(classmates)
classmates.sort()
print(classmates)
classmates.sort(reverse=True)
print(classmates)
print(sorted(classmates))
print(sorted(classmates, reverse=True))
print(classmates)
classmates.reverse()
print(classmates)
print(len(classmates))