def setup():
    size(800, 600)
    noStroke()
    img = loadImage("download.jpg")
    x = 0
    
    while x < 800:
        y = 0
        while y < 600:
            image(img,x, y, 100, 100)
            # if y % 100 == 0:
            y= y + 100   
            # if x % 100 == 0:
        x = x + 100
           
