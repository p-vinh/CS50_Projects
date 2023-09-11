def main():
    i = input()
    convert(i)

def convert(s=str):
    print(s.replace(":)","🙂").replace(":(","🙁"))

main()