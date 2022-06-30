from PIL import Image

width_height_Red =  (120, 300) 
width_height_Amber =  (30, 300) 
width_height_Green =  (150, 300) 

img1 = Image.new(mode = "RGB", size = width_height_Red, color = (252, 228, 214)) 
img2 = Image.new(mode = "RGB", size = width_height_Amber, color = (255, 242, 204))
img3 = Image.new(mode = "RGB", size = width_height_Green, color = (226, 239, 218))


def get_concat_h(img1, img2, img3):
    dst = Image.new('RGB', (img1.width + img2.width + img3.width, img1.height))
    dst.paste(img1, (0, 0))
    dst.paste(img2, (img1.width, 0))
    dst.paste(img3, (img1.width + img2.width, 0))
    return dst


get_concat_h(img1, img2, img3)
