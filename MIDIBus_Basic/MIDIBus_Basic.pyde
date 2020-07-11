add_library('themidibus')


def setup():
    size(400, 400)
    background(0)
    
    global myBus
    myBus = MidiBus(this, "Keystation 88", "Microsoft MIDI Mapper")
    myBus.list()
    

    
def draw():
    channel = 0
    pitch = 64
    velocity = 127
    
    myBus.sendNoteOn(channel, pitch, velocity) # Send a Midi noteOn
    delay(200)
    myBus.sendNoteOff(channel, pitch, velocity)
    
    number = 0
    value = 90
    
    myBus.sendControllerChange(channel, number, value)
    delay(2000)
    
def noteOn(channel, pitch, velocity):
    # Receive a noteOn
    print()
    print("Note On:")
    print("--------")
    print("Channel: ", channel)
    print("Pitch: ", pitch)
    print("Velocity; ", velocity)
    
def controllerChange(channel, number, value):
    # Receive a controllerChange
    print()
    print("Controller Change:")
    print("--------")
    print("Channel:", channel)
    print("Number:", number)
    println("Value:", value)
