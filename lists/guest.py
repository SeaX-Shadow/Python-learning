#Guest list
guests = ['Leonora', 'Kliton', 'Jonis']
#Invitations
msg = f"{guests[0].title()} you are invited to my party!"
print(msg)

msg = f"{guests[1].title()} you are invited to my party!"
print(msg)

msg = f"{guests[2].title()} you are invited to my party!"
print(msg)

print("==========================")

#Leonora can't make it
print(f"{guests[0]} can't make it.")
#Removing Leonora from the list
del guests[0]
#Replacing Leonora with Denis
guests.insert(0, 'Denis')

print("==========================")
#New invitations
msg = f"{guests[0].title()} you are invited to my party!"
print(msg)

msg = f"{guests[1].title()} you are invited to my party!"
print(msg)

msg = f"{guests[2].title()} you are invited to my party!"
print(msg)
#More guests
print("I have found a bigger table so 3 more people can come.")
#Adding guests to the list

guests.insert(0, "Leonora")
guests.insert(3, "Esned")
guests.append("Amri")

print("===========================")
#New invitation letters
msg = f"{guests[0].title()} you are invited to my party!"
print(msg)

msg = f"{guests[1].title()} you are invited to my party!"
print(msg)

msg = f"{guests[2].title()} you are invited to my party!"
print(msg)
msg = f"{guests[3].title()} you are invited to my party!"
print(msg)

msg = f"{guests[4].title()} you are invited to my party!"
print(msg)

msg = f"{guests[5].title()} you are invited to my party!"
print(msg)
print("============================")
#Emergency
print("I can only invite 2 people to the party!!!")
#Removing guests from the list
guest_removed = guests.pop(5)
print(f"{guest_removed} I'm sorry!")
guest_removed = guests.pop(4)
print(f"{guest_removed} I'm sorry!")
guest_removed = guests.pop(3)
print(f"{guest_removed} I'm sorry!") 
guest_removed = guests.pop(2)
print(f"{guest_removed} I'm sorry!")

print(f"{guests[0].title()} you are still invited!")
print(f"{guests[1].title()} you are still invited!")
del guests[0]
del guests[0]
print(guests)


