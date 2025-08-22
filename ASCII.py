#ASCII Conversion 

def asciiConversion(strParam):
    
    result = []
    for i in strParam:
        ascii_value = ord(i)
        result.append(ascii_value)
     #Convert the list of ASCII values to a single integer
    result = int("".join(str(num) for num in result)) 
   """Optional: Convert list of ASCII values to a space-separated string
      Example: "AB" -> [65, 66] -> "65 66"
      space_separated_result = " ".join(str(num) for num in result)"""
    print(result)
    
asciiConversion(input("Enter a String/Character:"))
