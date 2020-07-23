################################################################################
# code and images by Maximilian Konrad
# https://github.com/MLK97
#
# released under the GPL license (https://www.gnu.org/licenses/gpl-3.0.de.html)
################################################################################

xoff = 0
start = 0
inc = 0.01
def setup():
    size(1100, 800)
    
def draw():    
    global xoff, start, inc
    background(50)
    stroke(255)
    noFill()
    beginShape(QUADS)
    xoff = start
    for y in range(25, height-25, 5):
        stroke(255)
        vertex(map(noise(xoff), 0, 1, width/2-100, width/2+100), y)
        vertex(100, height/2)
        vertex(width-100, height/2)
        xoff += inc
        
    endShape()  
    start += inc
    saveFrame("pictures/noisy-quads-######.jpg")
