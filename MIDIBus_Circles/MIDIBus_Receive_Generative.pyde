################################################################################
# Code and Images by Maximilian Konrad
# https://github.com/MLK97
#
# released under the GPL license (https://www.gnu.org/licenses/gpl-3.0.de.html)
################################################################################

add_library('themidibus')

channel = 0
pitch = 0
velocity = 0
w = 900
h = 900 

def setup():
    size(w, h)
    frameRate(30)

    global myBus
    myBus = MidiBus(this, "Keystation 88", "Microsoft MIDI Mapper")
    myBus.list()

    
def draw():
    background(50)
    circle(pitch, pitch, velocity)
    
    saveFrame("pictures/MIDIBus-Circles-######.jpg")
    
def noteOn(channelI, pitchI, velocityI):
    # Receive a noteOn
    global channel, pitch, velocity, myBus, w, h
    if velocityI != 0:
        channel = channelI
        pitch = int(pitchI *random(2,17))
        if pitch > h:
            pitch = h
        velocity = int(velocityI*random(1,5))
    
    
def noteOff(channelO, pitchO, velocityO):
    # Receive a noteOff
    # Some Midi-Controllers don't send a noteOff
    # Instead they send a noteOn with velocity = 0
    # (Keystation 88 behaves like this)
    # You can test this with MidiOX for example
    print("Note Off")
    
    
    
    
