from pyfiglet import Figlet
import sys

figlet = Figlet()

if len(sys.argv) !=1 and len(sys.argv) != 3 :
    sys.exit('Invalid usage')

if len(sys.argv) == 1:
    s = input('Input: ')
    print('Output:', figlet.renderText(s))

elif len(sys.argv) == 3:
    if sys.argv[1] != '-f' and sys.argv[1] != '--font':
        sys.exit('Invalid usage')

    if sys.argv[2] not in figlet.getFonts():
        sys.exit('Invalid usage')

    figlet.setFont(font = sys.argv[2])

    s = input('Input: ')

    print('Output:', figlet.renderText(s))

