def test(file1, file2):
    myfile = open(file1,"r")
    lines = myfile.readlines()
    lines.reverse()
    myfile.close()
    filetwo = open(file2, "w")
    for line in lines:
        filetwo.write(line)
    filetwo.close()
def main():
    filename = "C:/Users/Lilyj/AppData/Local/Programs/Python/Python312/test.txt"
    filename2 = "C:/Users/Lilyj/AppData/Local/Programs/Python/Python312/mesa.txt"
    test(filename, filename2)

if __name__ == "__main__":
    main()
