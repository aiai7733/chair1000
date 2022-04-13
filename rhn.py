import csv
# from PIL import ImageFont

# def add_text_to_image(img, text, font_path, font_size, font_color, height, width, max_length=4):
#     position = (width, height)
#     font = ImageFont.truetype(font_path, font_size)
#     draw = ImageDraw.Draw(img)
#     if draw.textsize(text, font=font)[0] > max_length:
#         while draw.textsize(text + '…', font=font)[0] > max_length:
#             text = text[:-1]
#         text = text + '…'

#     draw.text(position, text, font_color, font=font)

#     return img

rhn = []
with open('/Users/hasegawaai/Desktop/ADL/pinch/rhn.csv') as f:
    reader = csv.reader(f)
    rhn = [row for row in reader]

print(rhn)

# imagePath = '/Users/hasegawaai/Desktop/ADL/pinch/image/image0.png'
# r = rhn[0][0]
# h = rhn[0][1]
# n = rhn[0][2]
# text = "r: %s\nh: %s\nnum_legs" % (r, h, n)
# fontPath = "/System/Library/Fonts/ArialHB.ttc"
# fontSize = 10
# color = (0, 0, 0)

# image = Image.open(imagePath)
# font = ImageFont.truetype(fontPath,fontSize)#フォントの指定
# draw = ImageDraw.Draw(image)
# draw.text((110,20),text,font=font,fill=color)
# image.save(image_path)