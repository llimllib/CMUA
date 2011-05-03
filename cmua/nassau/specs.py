from imagekit.specs import ImageSpec 
from imagekit import processors 

# inline thumbnails
class ResizeThumb(processors.Resize): 
    width = 140
    height = 79
    crop = False

class ResizeEntry(processors.Resize):
    width = 620
    crop = False

# now lets create an adjustment processor to enhance the image at small sizes 
class EnchanceThumb(processors.Adjustment): 
    contrast = 1.2 
    sharpness = 1.1 

class EntryPic(ImageSpec):
    access_as = 'entry_image'
    pre_cache = True
    processors = [ResizeEntry]

# now we can define our thumbnail spec 
class Thumbnail(ImageSpec): 
    access_as = 'thumbnail_image' 
    pre_cache = False 
    processors = [ResizeThumb, EnchanceThumb] 
