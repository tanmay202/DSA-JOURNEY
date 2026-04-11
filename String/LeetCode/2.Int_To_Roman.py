while(True):    
    num = int(input("Enter number: "))

    def convert(digit, one, five, ten):
        if digit < 4:
            return one * digit
        elif digit == 4:
            return one + five
        elif digit < 9:
            return five + one * (digit - 5)
        elif digit == 9:
            return one + ten

    output = ""

    # thousands
    output += "M" * (num // 1000)

    # hundreds
    output += convert((num % 1000) // 100, "C", "D", "M")

    # tens
    output += convert((num % 100) // 10, "X", "L", "C")

    # ones
    output += convert(num % 10, "I", "V", "X")

    print(output)