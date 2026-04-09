st="My name is Tanmay.I live in  Bagula.I wanna be a game developer,But making games is very tough.For now I want be a backend developer."

v=c=0

for ch in st:
    if ch.lower() in 'aeiou':
        v+=1
    elif ch.isalpha() :
        c+=1

print(f"Total vowel: {v}")
print(f"Total consonant: {c}")
