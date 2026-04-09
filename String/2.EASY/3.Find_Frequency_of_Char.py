st = input("Enter a string: ")

freq = {}

for ch in st:
    freq[ch] = freq.get(ch, 0) + 1

for ch in st:
    if freq[ch] == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character")