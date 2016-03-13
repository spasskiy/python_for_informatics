largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    try:
        number = int(num)
        if largest is None:
            largest = number
        if smallest is None:
            smallest = number
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    except:
        if num == "done":
            break
        print "Invalid input"

print "Maximum is", largest
print "Minimum is", smallest