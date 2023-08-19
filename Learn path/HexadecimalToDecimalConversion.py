def decimalToHecadecimal(decimal):
    conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
    decimal = int(decimal)
    hexadecimal = ''
    while(decimal>0):
        remainder = decimal%16
        hexadecimal = conversion_table[remainder]+ hexadecimal
        decimal = decimal//16
    print("Hexadecimal: ",hexadecimal)
    
def hexadecimalToDecimal(hexadecimal):
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hexadecimal = hexadecimal.strip().upper()
    decimal = 0
    power = len(hexadecimal) -1
    for digit in hexadecimal:
        decimal += conversion_table[digit]*16**power
        power -= 1
    print(decimal)

def main():
    type = input("Do you want to convert to decimal to hexadecimal? ")
    if type == "decimal":
        decimal = input("Enter the hexadecimal number: ")
        hexadecimalToDecimal(decimal)
    elif type == "hexadecimal":
        hexadecimal = input("Enter your decimal number: ")
        decimalToHecadecimal(hexadecimal)
    else:
        print("Invalid choice")

main()