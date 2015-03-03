from PIL import Image
from cStringIO import StringIO
from django.core.files.base import ContentFile

def handle_image(image_file):
    #img_path = MEDIA_URL+image.name
    # im = Image.open(image_file)
    # print(im.size)
    return image_file
    # (width, height) = im.size
    # (width, height) = (50,50)
    # new_im = im.resize((width, height))
    # new_im_file = StringIO()
    # new_im.save(new_im_file, 'jpeg', optimize = True)
    # new_im_file.seek(0)
    # return ContentFile(new_im_file)

def roll(image, delta):
    "Roll an image sideways"

    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))

    return image
