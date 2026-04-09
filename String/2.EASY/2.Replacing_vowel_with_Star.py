st="My name is Tanmay.I live in  Bagula.I wanna be a game developer,But making games is very tough.For now I want be a backend developer."

newst=""
tch=0
for ch in st:
    if ch.lower() in 'aeiou':
        newst+='*'
        tch += 1 
    else:
        newst+=ch


print(newst)
print("Total * :",tch)