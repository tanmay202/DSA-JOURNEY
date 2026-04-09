# st = input("Enter a string: ").strip()
st='Mr. Ding'
words = st.split()

for word in words:
    print(word[::-1], end=" ")
    