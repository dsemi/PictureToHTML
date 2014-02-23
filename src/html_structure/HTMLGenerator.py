#!/usr/bin/python2

PAGE_TEMPLATE = '''
<DOCTYPE !html>
<html>
<style>
body {
    position: relative;
    text-align: center;
    z-index: -9999999;
}
div.outlined {
border: 1px solid black;
}
</style>
%s
</html>'''

DIV_TEMPLATE = '''
<{tag} class="outlined" style="position: absolute;
left: {x}%%; top: {y}%%; width: {width}%%; height: {height}%%;
%s z-index:{depth}">{text}
</{tag}>'''


# As of right now this is very barebones, when more features of html are added, make class and have generators for different objects
# Then also move outer html out to another function

def divs_from_boxes(box_list):
    return PAGE_TEMPLATE % ('\n'.join([(DIV_TEMPLATE % ("background:rgb({color[2]}, {color[1]}, {color[0]}); " if box['tag'] != 'button' else "")).format(**box) for box in box_list]))
    
def main():
    pass

if __name__ == '__main__':
    main()



