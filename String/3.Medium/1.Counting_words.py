st = input("Enter a sentence: ").strip()

if st == "":
    print("No words found")
else:
    words = st.split()
    print("Total words:", len(words))