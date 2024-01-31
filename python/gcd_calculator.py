# S-MATH100 (Number Theory)
# Otanes, De Los Reyes, Gabot, Tuazon

def find_gcd_of_array(numbers):
    current_gcd = find_gcd(numbers[0], numbers[1]) #find the gcd of the first two elements = gcd(index0, index1)

    for num in numbers[2:]: #find the gcd of current_gcd and the next element until last = gcd(current_gcd, index2) and so on
        current_gcd = find_gcd(current_gcd, num)

    return current_gcd

def find_gcd(a, b): #euclidean algorithm to find gcd
    while b != 0: 
        a, b = b, a % b

    return a

def input_formatter(input): #clean the user input, turn into array, parse str to int
    try:
        array = [int(x) for x in input.replace(" ", "").split(',')]
    except ValueError: #end program when invalid characters are entered or blank input
        print("\nInvalid Input\n")
        exit()

    if len(array) < 2: #end program when there are less than two integers entered
        print("\nAt least two numbers are required to find the GCD.\n")
        exit()

    return array


numbers = input("\nEnter integers to find their GCD: ")

array = input_formatter(numbers)
gcd = abs(find_gcd_of_array(array))

print(f"\nInput: {array}\nGCD = {gcd}\n")
