################################################################################
# Concentric animation
#
# Playing around with concentric circles
# 
# PRogrammed and Animated by Maximilian Konrad
# 2020-01-06
# https://github.com/MLK97
#
################################################################################

# Define globals here
rand_seed = 1138
frame_rate = 60
w = 900  # width
h = 900  # height
offset = 0
iteration = 1


        
        
def setup():
    # Sets size of canvas in pixels (must be first line)
    size(w, h) # (width, height)
    
    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high
    
    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(RGB, 100)
        
    # Set the number of frames per second to display
    frameRate(frame_rate)
        
    # Set the psuedorandom seed
    randomSeed(rand_seed)
    
    # Set (x, y) for circles to center
    ellipseMode(CENTER)
    
    global pg
    pg = createGraphics(w,h)    
    
    background(0, 0, 0)
    stroke(255, 255, 255)
    
    # Stops draw() from running in an infinite loop (should be last line)
    #noLoop()


def draw():
    concentric_circle((width/2), (height/2), 250, 25)
    image(pg, 0, 0)
    saveFrame("images/circles-######.jpg")
    

def concentric_circle(x, y, radius, amount_inner_circles):
    global offset, iteration
    step = radius/amount_inner_circles
    pg.beginDraw()
    pg.background(0,0,0)
    pg.noFill()
    pg.stroke(255,255,255)
    for i in range(amount_inner_circles+1):
        if iteration == 1:
            pg.ellipse(x-offset, y, radius, radius)
            pg.ellipse(x+offset, y, radius, radius)
        if iteration == 2:
            pg.ellipse(x-offset, y, radius, radius)
            pg.ellipse(x+offset, y, radius, radius)
            pg.ellipse(x, y-offset, radius, radius)
            pg.ellipse(x, y+offset, radius, radius)
        if iteration == 3:
            pg.ellipse(x-offset, y, radius, radius)
            pg.ellipse(x+offset, y, radius, radius)
            pg.ellipse(x, y-offset, radius, radius)
            pg.ellipse(x, y+offset, radius, radius)
            pg.ellipse(x-offset, y-offset, radius, radius)
            pg.ellipse(x-offset, y+offset, radius, radius)
            pg.ellipse(x+offset, y-offset, radius, radius)
            pg.ellipse(x+offset, y+offset, radius, radius)
        radius = radius - step
    pg.line(0,0,w,h)
    pg.line(w,0,0,h)
    pg.endDraw()
    offset = offset + 4
    if width/2 < offset and iteration < 3:
        offset = 0
        iteration = iteration + 1
    else:
        offset = 0
        iteration = 1
    
    
