from PIL import Image
import argparse

# take care of the command line arguments
parser = argparse.ArgumentParser()

# define input file、output file and height and width of the output character painting
parser.add_argument('file',help="file path of the input image file")     # input file
parser.add_argument('-o', '--output', help="file path of the output character painting file")   # output file
parser.add_argument('--width', type = int, default = 80, help="the width of the output character painting") # output character painting width
parser.add_argument('--height', type = int, default = 80, help="the height of the output character painting") # output character painting height

# parse and get arguments
args = parser.parse_args()

# path of the input image file
IMG = args.file

# width of the output character painting
WIDTH = args.width

# height of the output character painting
HEIGHT = args.height

# path of the output file
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):

    # check alpha value
    if alpha == 0:
        return ' '

    # get length of the chacracter list (70)
    length = len(ascii_char)

    # convert RGB value into gray value which is in the range of 0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # the range of gray value is 0-255，while the length of character list is 70
    # map the gray value into the character list
    unit = (256.0 + 1)/length

    # return the mapped character
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':

    # open and adjust the width and height of the picture
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    # initilize the result string
    txt = ""

    # loop over every row
    for i in range(HEIGHT):
        # loop over every column
        for j in range(WIDTH):
            # convert the RGB value on pixel (j,i) to mapped character and append to the result string
            txt += get_char(*im.getpixel((j,i)))
        # append the new line character to the end of every row
        txt += '\n'
    # print out in terminal
    print(txt)

    # output the character painting into a file
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
            