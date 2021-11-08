import sys
import container
import time


start = time.time()
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Incorrect command line! You must write: python main -f <inputFileName>\n"
              "[<outputFileName1>] [<outputFileName2>] or python main -r <number of elements>\n"
              "[<outputFileName1>] [<outputFileName2>]")
    elif str(sys.argv[1]) == "-f":
        if len(sys.argv) == 5:
            inputFileName = sys.argv[2]
            outputFileName1 = sys.argv[3]
            outputFileName2 = sys.argv[4]
        elif len(sys.argv) == 4:
            inputFileName = sys.argv[2]
            outputFileName1 = sys.argv[3]
            outputFileName2 = "Outputs\output2.txt"
        elif len(sys.argv) == 3:
            inputFileName = sys.argv[2]
            outputFileName1 = "Outputs\output1.txt"
            outputFileName2 = "Outputs\output2.txt"
        else:
            print("Incorrect command line! You must write: python main -f <inputFileName>"
                  "[<outputFileName1>] [<outputFileName2>]")
            exit()
    elif sys.argv[1] == "-r":
        if len(sys.argv) == 5:
            elementsCount = int(sys.argv[2])
            outputFileName1 = sys.argv[3]
            outputFileName2 = sys.argv[4]
        elif len(sys.argv) == 4:
            elementsCount = int(sys.argv[2])
            outputFileName1 = sys.argv[3]
            outputFileName2 = "Outputs\output2.txt"
        elif len(sys.argv) == 3:
            elementsCount = int(sys.argv[2])
            outputFileName1 = "Outputs\output1.txt"
            outputFileName2 = "Outputs\output2.txt"
        else:
            print("Incorrect command line! You must write: python main -r <number of elements>"
                  "[<outputFileName1>] [<outputFileName2>]")
            exit()
    else:
        print("Incorrect command line!")
        exit()

    print("----------Start program----------")
    cont = []
    if sys.argv[1] == "-f":
        ifile = open(inputFileName)
        str = ifile.read()
        ifile.close()

        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        strArray = str.replace("\n", " ").split(" ")
        container.Read(cont, strArray)
    else:
        container.Random(cont, elementsCount)

    container.Print(cont)
    ofile1 = open(outputFileName1, 'w')
    container.Write(cont, ofile1)
    ofile1.close()

    print("********** After the function has worked **********")
    container.SpecialFunction(cont)
    container.Print(cont)
    ofile2 = open(outputFileName2, 'w')
    container.Write(cont, ofile2)
    ofile2.close()

    print("----------Finish program----------")
print("time of work", time.time() - start)
