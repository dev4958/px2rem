import sys

args = sys.argv
if len(sys.argv) != 3:
    print()
    print('px2rem.py')
    print('Converts a file with px values (ex: 1px) to rem values (ex: 1rem) based on a specified root font size.')
    print('Requires two arguments, [file path] and [root font size] to convert.')
    print()
    print('Example: $python3 px2em.py [file path] [root font size (float || integer)]')
    print('Clarification: If [root font size] = 16 and line n of [file path] contains the value "16px" -> line n of [file path] converts to contain the value "1.000rem".')
    print()
else:
    if sys.argv[2].find('px') != -1:
        sys.argv[2] = sys.argv[2][0 : len(sys.argv[2]) - 2]
    with open(sys.argv[1]) as file, open('output.txt', 'w') as output:
        for _ in file:
            position = _.find('px')
            if position != -1 and _.find('@media') == -1:
                backStep = 0
                while _[position - backStep] != ' ' and _[position - backStep] != ':':
                    backStep += 1
                else:
                    rem = '{0:.3f}'.format(float(_[position - (backStep - 1) : position]) / float(sys.argv[2])) + 'rem'
                    convertedLine = _.replace(_[position - (backStep - 1) : position + 2], rem)
                    output.write(convertedLine)
            else:
                output.write(_)
