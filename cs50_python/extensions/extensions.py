def main():
    fileType = input("File name: ").lower().strip()
    pFileType(fileType)

def pFileType(f):
    if (f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".gif") or f.endswith(".png")):
        if(f.endswith(".jpg") or f.endswith(".jpeg")):
            print("image/jpeg")
        else:
            print("image/" + f[f.rfind(".")+1:])
    elif(f.endswith(".pdf") or f.endswith(".zip")):
        print("application/" + f[f.rfind(".")+1:])
    elif(f.endswith(".txt")):
        print("text/plain")
    else:
        print("application/octet-stream")

main()