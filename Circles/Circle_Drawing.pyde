################################################################################
# Concentric animation
#
# Playing around with concentric circles
# 
# Based on the talented Paul Rickards: 
# https://twitter.com/paulrickards/status/1028651749555560448
#
# Based on Aaron Penne 
# 2018-08-21
# https://github.com/aaronpenne
#
# Modulated and Animated by Maximilian Konrad
# 2020-01-06
# https://github.com/MLK97
#
################################################################################

# Define globals here
rand_seed = 1138
frame_rate = 30
x = 777
w = 900  # width
h = 900  # height
pad = h/2
pad_pct = 0.07
k = 0
inc = True


        
        
def setup():
    # Sets size of canvas in pixels (must be first line)
    size(w, h) # (width, height)
    
    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high
    
    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)
        
    # Set the number of frames per second to display
    frameRate(frame_rate)
        
    # Set the psuedorandom seed
    randomSeed(rand_seed)
    
    # Set (x, y) for circles to center
    ellipseMode(CENTER)
    
    
    background(50, 0, 30)
    
    # Stops draw() from running in an infinite loop (should be last line)


def draw():
    
    global k
    global inc
    #Check if Circle Amount reached 15:
    #If it hasn't increase until 15
    #If it has decrease until -1
    if inc and k < 15:
        k = k + 1
    elif k == 15 and inc:
        inc = False
    elif inc == False and k >= 0:
        k = k - 1
    elif k == -1:
        inc = True
        
    #Draws the Circle    
    strokeWeight(1)
    concentric_circles(k, 200)
    
    saveFrame("circles-######.jpg")
    
#Draws Circles with inner Circles in them
def concentric_circles(num_circles, outer_radius):
    x = 0
    y = 50
    step = outer_radius/(num_circles+2)
    next_circle = outer_radius
    while(y < height):
        x = 0
        while(x < width+1):
            radius = outer_radius
            for i in range(num_circles):
                ellipse(x, y, radius, radius)
                radius -= step
            x += (next_circle/2)
        y += (next_circle/2)
            
