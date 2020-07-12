add_library('themidibus')

channel = 0
pitch = 0
velocity = 0

def setup():
    size(1820, 980)
    frameRate(30)

    global myBus
    myBus = MidiBus(this, "Keystation 88", "Microsoft MIDI Mapper")
    myBus.list()

    
def draw():
    background(50)
    circle(pitch, pitch, velocity)
    
def noteOn(channelI, pitchI, velocityI):
    # Receive a noteOn
    global channel, pitch, velocity, myBus
    if velocityI != 0:
        channel = channelI
        pitch = int(pitchI *random(2,20))
        velocity = int(velocityI*random(1,5))
    
    
def noteOff(channelO, pitchO, velocityO):
    # Receive a noteOff
    # Some Midi-Controllers don't send a noteOff
    # Instead they send a noteOn with velocity = 0
    # (Keystation 88 behaves like this)
    # You can test this with MidiOX for example
    print("Note Off")
    
    
    
    
