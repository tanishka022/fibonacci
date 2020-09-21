total_terms = int(input("Total terms: "))

a = 0
b = 1
count = 0

if total_terms <= 0:
    print("Please enter a positive integer: ")

elif total_terms == 1:
    print("Series: ", total_terms, ":")
    print(a)

else:
    print("Series: ")
    while count < total_terms:
        print(a)
        sum = a + b
        a = b
        b = sum
        count = count + 1
