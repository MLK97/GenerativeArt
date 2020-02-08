################################################################################
# 8 Dots
#
# Playing around with various configurations of 8 Dot generations
# 
# PRogrammed and Animated by Maximilian Konrad
# 2020-02-08
# https://github.com/MLK97
#
################################################################################
# Define globals here
rand_seed = 1138
w = 1200  # width
h = 1200  # height
frame_rate = 1



        
        
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
    
    background(15, 14, 14)
    stroke(15, 14, 14)
    strokeWeight(2)
    
    # Stops draw() from running in an infinite loop (should be last line)
    noLoop()


def draw():
    s = 0
    for k in range(4):
        t = 0
        for l in range(4):
            fill(41,37,37)
            square(80+s, 80+t, 200)
            fill(255,40,40)
            random_dots(180+s, 180+t)
            t += 280
        s += 280
    
    saveFrame("images/gif-######.jpg")
 
 
    
def random_dots(x, y):
 for m in range(8):
    x0 = x+random(-80,80)
    y0 = y+random(-80,80)
    circle(x0, y0, 30)
 
    
