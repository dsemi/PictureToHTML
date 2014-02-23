#!/usr/bin/python2

import random

def main():
    l = [(random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)) for i in range(10)]
    print('<html>%s</html>' % ('\n'.join(['<div class="outlined" style="position: absolute; left: %d; top: %d; width: %d; height: %d;">\n</div>' % box for box in l])))

    for i in range(3): print

    print('''.outlined {
    border: 1px solid black;
    }''')


if __name__ == '__main__':
    main()



