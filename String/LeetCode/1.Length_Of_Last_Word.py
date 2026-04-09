st = input("Enter a string: ").strip()
words = st.split()

if not words:
    print("No words found")
else:
    lword = len(words[-1])
    print(f"Length of last word is: {lword}")