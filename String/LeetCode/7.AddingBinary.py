def AddBinary(a,b):
    for ch in a + b:
        if ch not in '01':
            return "Invalid binary number"
        