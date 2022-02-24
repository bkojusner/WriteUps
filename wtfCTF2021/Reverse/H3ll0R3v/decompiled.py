import sys

def main(input):
    j = -4
    for c in input:
        if j == 1:
            if c != 'Z':
                exit(43)
            else:
                if j == -7:
                    if c != 'w':
                        exit(133)
                    else:
                        if j == -5:
                            if c != 'f':
                                exit(42069)
                            else:
                                if j == -4:
                                    if c != 'C':
                                        exit(11037)
                                else:
                                    if j == 7:
                                        if c != 'R':
                                            exit(9001)
                                        else:
                                            if j == -2:
                                                if c != 'F':
                                                    exit(11037)
                                            if j == -1 and c != '{':
                                                exit(11037)
                                    if j == 4 and c != '3':
                                        exit(11037)
                        elif j == 0 and c != '3':
                            exit(11037)
                else:
                    if j == -3:
                        if c != 'T':
                            exit(82)
                        if j == 2:
                            if c != '_':
                                exit(11037)
                        if j == -6:
                            if c != 't':
                                exit(133)
                        if j == 6:
                            if c != 'E':
                                exit(133)
                    elif j == 9 and c != '3':
                        exit(7223)
        else:
            if j == 3:
                if c != 'R':
                    exit(133)
                if j == 5:
                    if c != 'V':
                        exit(133)
                if j == 8:
                    if c != '5':
                        exit(6738)
            elif j == 10:
                if c != '}':
                    exit(1111)
            j += 1
    else:
        print('Hello World')

main(sys.argv)
