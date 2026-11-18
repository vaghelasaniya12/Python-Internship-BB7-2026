usernames = ["Ayman", "Ayesha", "Riya", "Sarah", "Aamena", "Saniya"]

result = list(filter(lambda name: len(name) >= 6, usernames))

print("Original Usernames:", usernames)

print("Filtered Usernames:", result)