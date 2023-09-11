import sys


def main():
    while True:
        credit = input("Number: ")

        if (credit.isnumeric()):
            break

    length = len(credit)

    if (length != 13 and length != 15 and length != 16):
        print("INVALID")
        sys.exit(0)

    checkSum(credit, length)

    firstDigits = int(credit[0] + credit[1])

    if (int(credit[0]) == 4):
        print("VISA")
    elif (firstDigits >= 51 and firstDigits <= 55):
        print("MASTERCARD")
    elif (firstDigits == 34 or firstDigits == 37):
        print("AMEX")
    else:
        print("INVALID")


def checkSum(credit, length):
    credit = int(credit)
    total = False
    digit1 = 0
    digit2 = 0
    sumEvens = 0
    sumOdds = 0
    count = 0

    while credit > 0:
    	digit2 = digit1
    	digit1 = credit % 10

    	if (count % 2 == 0):
            sumEvens += digit1
    	else:
            multiple = 2 * digit1
            sumOdds += (multiple // 10) + (multiple % 10)

    	credit //= 10
    	count += 1

    total = (sumEvens + sumOdds) % 10 == 0
    if (total == False):
        print("INVALID")
        sys.exit(0)


if __name__ == "__main__":
    main()
