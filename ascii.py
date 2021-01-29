from PIL import Image
import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('file')     # path of the input file
    parser.add_argument('-o', '--output')   # path of the output file
    parser.add_argument('--width', type = int, default = 80) # the width of the output painting
    parser.add_argument('--height', type = int, default = 80) # the height of the output painting

    args = parser.parse_args()

    IMG = args.file
    WIDTH = args.width
    HEIGHT = args.height
    OUTPUT = args.output

    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

    # map 256 grayscale values to 70 ASCII characters
    def get_char(r,g,b,alpha = 256):
        if alpha == 0:
            return ' '
        length = len(ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

        unit = (256.0 + 1)/length
        return ascii_char[int(gray/unit)]

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
    im = im.convert('RGB') # ensure the value of each pixel is a tuple

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    # save the ASCII art style painting into the file
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("result.txt",'w') as f:
            f.write(txt)

if __name__ == '__main__':
    main()
   