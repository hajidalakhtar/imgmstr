from fastapi import APIRouter
import requests
from PIL import Image,ImageFilter
from io import BytesIO
from starlette.responses import StreamingResponse

#APIRouter creates path operations for user module
router = APIRouter()



def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return StreamingResponse(img_io, media_type="image/png")
  

@router.get('/')
def read_root(url:str = None,rotate:str = None,flip:str = None,w:str = None,blur:str = None):
    img_url = url
    rotate = rotate
    flip = flip
    thumbnail_width = w
    blur = blur
    # return "asd"

    if img_url != None:
      img_url_open = requests.get(img_url)
      return_img = Image.open(BytesIO(img_url_open.content))
      if rotate != None:
        return_img = return_img.rotate(int(rotate))
      if flip != None and flip == "true":
        return_img = return_img.transpose(Image.FLIP_LEFT_RIGHT)
        
      if thumbnail_width != None:
        return_img.thumbnail((int(thumbnail_width),int(thumbnail_width)))
      if blur != None:
        return_img = return_img.filter(ImageFilter.BoxBlur(int(blur)))
    
      return serve_pil_image(return_img)
    else:
      return "https://imgmstr.vercel.app/?url=https://cdnb.artstation.com/p/assets/images/images/024/538/889/large/pixel-jeff-rog-demo1.jpg&w=1800&flip=true&blur=10"
