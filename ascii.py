from PIL import Image
import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', help="path of the input file")   
    parser.add_argument('-o', '--output', help="path of the output file")  
    parser.add_argument('--width', type = int, default = 80, help="the width of the output painting,by default 80")
    parser.add_argument('--height', type = int, default = 80, help="the height of the output painting by default 80") 
    args = parser.parse_args()

    IMG = args.file
    WIDTH = args.width
    HEIGHT = args.height
    OUTPUT = args.output

    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    length = len(ascii_char)

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
    im = im.convert('L') 

    txt = ""

    # map 256 grayscale values to ASCII characters in the list
    for i in range(HEIGHT):
        for j in range(WIDTH):
            gray = im.getpixel((j,i))
            txt += ascii_char[int(gray/255*(length-1))]
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
   