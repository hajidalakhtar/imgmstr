from fastapi import FastAPI
import uvicorn
import requests
from PIL import Image,ImageFilter
from io import BytesIO
from starlette.responses import StreamingResponse


app = FastAPI()

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return StreamingResponse(img_io, media_type="image/png")
  


  
@app.get("/")
def read_root():
    return {"Hello": "Wofdsfsdfrld"}



@app.get('/img')
def image(url:str = None,rotate:str = None,flip:str = None,w:str = None,blur:str = None):
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
      return "https://magicimage.hajidalakhtar.repl.co/img?url=https://images.ctfassets.net/23aumh6u8s0i/1T1ohGJuh0B6wqNSwUuXy8/60206973f801267676b9b7f98c34eaea/04_solid_pixels&w=1800&blur=10"

# uvicorn.run(app,host="0.0.0.0",port="8080")

#https://github.com/tiangolo/fastapi
#https://tryolabs.com/blog/2019/12/10/top-10-python-libraries-of-2019/