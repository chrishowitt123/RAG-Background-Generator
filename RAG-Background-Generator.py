from PIL import Image

"""
A program that builds RAG backgrounds for charts.

"""

# define dimensions 
width_height_Red =  (120, 300) 
width_height_Amber =  (30, 300) 
width_height_Green =  (150, 300) 


img1 = Image.new(mode = "RGB", size = width_height_Red, color = (252, 228, 214)) 
img2 = Image.new(mode = "RGB", size = width_height_Amber, color = (255, 242, 204))
img3 = Image.new(mode = "RGB", size = width_height_Green, color = (226, 239, 218))


# join RAGs togeather
def get_concat_h(img1, img2, img3):
    # define canvas size
    cvs = Image.new('RGB', (img1.width + img2.width + img3.width, img1.height))
    # paste images side-by-side
    cvs.paste(img1, (0, 0))
    cvs.paste(img2, (img1.width, 0))
    cvs.paste(img3, (img1.width + img2.width, 0))
    return cvs

get_concat_h(img1, img2, img3)
