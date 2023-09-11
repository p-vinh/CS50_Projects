def main():

    while True:
        height = input("Height: ")

        if (height.isnumeric()):
            height = int(height)
            if (height >= 1 and height <= 8):
                break

    for i in range(0, height):
        for space in range(1, height - i):
            print(" ", end="")

        for j in range(0, i+1):
            print("#", end="")

        print("  ", end="")

        for right in range(0, i+1):
            print("#", end="")
        print("")


main()
