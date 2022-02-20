# IMGMSTR

A simple URL to handle any image for your app

## Overview

* Rotate 
* Resizes 
* Blur 
* Watermark   


## Getting Started

**Resizes** [Try It](https://imgmstr.vercel.app/?url=https://cdnb.artstation.com/p/assets/images/images/024/538/889/large/pixel-jeff-rog-demo1.jpg&w=750).

```
https://imgmstr.vercel.app/?url=IMG_URL&w=IMG_SIZE
```

**Rotate** [Try It](https://imgmstr.vercel.app/?url=https://cdnb.artstation.com/p/assets/images/images/024/538/889/large/pixel-jeff-rog-demo1.jpg&rotate=20).

```
https://imgmstr.vercel.app/?url=IMG_URL&rotate=ANGLE
```

**Blur** [Try It](https://imgmstr.vercel.app/?url=https://cdnb.artstation.com/p/assets/images/images/024/538/889/large/pixel-jeff-rog-demo1.jpg&blur=5).

```
https://imgmstr.vercel.app/?url=IMG_URL&blur=BLUR_LEVEL
```

**Watermark** [Try It](https://imgmstr.vercel.app/?url=https://cdnb.artstation.com/p/assets/images/images/024/538/889/large/pixel-jeff-rog-demo1.jpg&wm_text=IMAGE%20MASTER&wm_text_color=ffffff&wm_text_size=40).

```
https://imgmstr.vercel.app/?url=IMG_URL&wm_text=WATERMARK TEXT&wm_text_color=HEXACOLOR (optional)&wm_text_size=PIXEL (optional)
```
## Using with html
```
<!DOCTYPE html>
<html>
<head>
<title>Image Master</title>
</head>
<body>

<h2>Resizes </h2>
<img src="https://imgmstr.vercel.app/?url=https://cdnb.artstation.com/p/assets/images/images/024/538/889/large/pixel-jeff-rog-demo1.jpg&w=750"/>

<h2>Blur </h2>
<img src="https://imgmstr.vercel.app/?url=https://cdnb.artstation.com/p/assets/images/images/024/538/889/large/pixel-jeff-rog-demo1.jpg&w=750&blur=5"/>
<h2>Flip  </h2>
<img src="https://imgmstr.vercel.app/?url=https://cdnb.artstation.com/p/assets/images/images/024/538/889/large/pixel-jeff-rog-demo1.jpg&w=750&flip=true"/>
<h2>Rotate  </h2>
<img src="https://imgmstr.vercel.app/?url=https://cdnb.artstation.com/p/assets/images/images/024/538/889/large/pixel-jeff-rog-demo1.jpg&w=750&rotate=180"/>
<h2>Watermark  </h2>
<img src="https://imgmstr.vercel.app/?url=https://cdnb.artstation.com/p/assets/images/images/024/538/889/large/pixel-jeff-rog-demo1.jpg&w=750&wm_text=By IMAGE MASTER&wm_text_color=ffffff"/>

</body>
</html>
```html



## License
Released under the [MIT License](https://github.com/go-gorm/gorm/blob/master/License)

