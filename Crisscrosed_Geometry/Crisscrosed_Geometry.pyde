################################################################################
# code and images by Maximilian Konrad
# https://github.com/MLK97
#
# released under the GPL license (https://www.gnu.org/licenses/gpl-3.0.de.html)
################################################################################

# Standard Python imports
import datetime
from random import shuffle, seed


################################################################################
# Global variables - knobs to turn
################################################################################

rand_seed = 1138
radius = 1

# Logic controls
record = True  # Save every frame?
animate = True  # Loop through draw()? 
seeded = True  # Set random seeds?




################################################################################
# Global variables
################################################################################


# The setup() function is part of Processing, it gets called one time when this file is run
def setup():
    # Sets size of canvas in pixels (must be first line)
    size(700, 700)
    
    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high
    
    # Set the number of frames per second to display
    frameRate(30)
    
    # Keeps text centered vertically and horizontally at (x,y) coords
    textMode(CENTER)
    textAlign(CENTER, CENTER)
    
    # Stops draw() from running in an infinite loop
    if not animate:
        noLoop()
        
    # Sets random seed value for both Python and Processing 
    if seeded:
        seed(rand_seed)       # Only applies to the random Python module
        randomSeed(rand_seed) # Only applies to the random() Processing function
        noiseSeed(rand_seed)  # Only applies to the noise() Processing function
    
    # Initializes colors for the first frame
    background(25, 25, 25)
    stroke(255, 255, 255)
    fill(114, 78, 78)

    
# The draw() function is part of Processing, it gets called in an infinite loop every frame
def draw():
    global radius
    x1 = abs(random(700))
    y1 = abs(random(700))
    x2 = abs(random(700))
    y2 = abs(random(700))
    x3 = abs(random(700))
    y3 = abs(random(700))
    x4 = abs(random(700))
    y4 = abs(random(700))
    
    noFill()
    
    beginShape()
    curveVertex(width/2, height/2)
    curveVertex(x1,y1)
    curveVertex(x2,y2)
    curveVertex(x3,y3)
    curveVertex(width/2, height/2)
    endShape()
    
    if (second() % 4) == 0 or (second() % 6) == 0 :
        stroke(25,25,25)
        strokeWeight(5)
        circle(width/2, height/2, radius)
        strokeWeight(1)
        radius = radius + 20
        stroke(255,255,255)
    elif (second() % 3) == 0 or (second() % 8) == 0 :
        stroke(25,25,25)
        strokeWeight(5)
        rect(width/2-radius, height/2-radius, 2*radius, 2*radius)
        strokeWeight(1)
        radius = radius + 20
        stroke(255,255,255)
    else:
        radius = 0
        
    saveFrame("pictures/crisscrossed-geometry-######.jpg")
    
    
