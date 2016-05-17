import sys
''' sys kezeli ha fájl név után beírsz valamit '''

def main(argv):
    if (len(argv)>0):
        print("Hello "+' '.join(argv)+"!")
    else:
        print("Hello Wolrd!")
main(sys.argv[1:])
