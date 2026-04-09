st = input("Enter a string: ").strip()

words = st.split()

if not words:
    print("No words found")
else:
    largest_word = words[0]

    for word in words:
        if len(word) > len(largest_word):
            largest_word = word

    print("Words:", words)
    print("Largest word:", largest_word)