#ASCII Conversion 

def asciiConversion(strParam):
    
    result = []
    for i in strParam:
        ascii_value = ord(i)
        result.append(ascii_value)
    result = int("".join(str(num) for num in result))
    print(result)
    
asciiConversion(input("Enter a String/Character:"))
