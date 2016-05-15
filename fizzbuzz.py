for each in range(0,101):
    if ((each % 3 == 0) and (each % 5 == 0)):
        print "fizzbuzz"
    elif (each % 3 == 0):
        print "fizz"
    elif (each % 5 == 0):
        print "buzz"
    else:
        print each
