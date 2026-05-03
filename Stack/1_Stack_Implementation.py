class Stack:
    def __init__(self, max_size=100):
        self.stack = []
        self.max_size = max_size

    # Push operation
    def push(self, item):
        if len(self.stack) >= self.max_size:
            print("Stack Overflow")
        else:
            self.stack.append(item)
            print(f"{item} pushed into stack")

    # Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            removed = self.stack.pop()
            print(f"{removed} popped from stack")

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    # Check if empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display stack
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements:", self.stack)


# 🔹 Main Program (Menu Driven)
s = Stack(5)

while True:
    print("\n--- Stack Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        s.push(val)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")