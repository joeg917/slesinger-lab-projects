import math
import pyabf
def valvePlotter(abf):
    # Variables
    bitDictionary = {} # This will store all the sweeps for a given valve
    sweepInterval = 2
    tagEvents = [] # lets us track when the valves change
    # Dictionary Initialization
    for i in range(8):
        bitDictionary[i] = []
    #Finding Valve Switch Points    
    for i in range(len(abf.tagComments)): #loop through the bit comments to see where the digital outputs turn on
       binary_tag =  abf.tagComments[i].split("=>")[1] 
       bit_index = binary_tag[::-1].find('1')# translate the "1" position to a particular valve number
       tag_sweep = (math.ceil(abf.tagTimesSec[i] / sweepInterval)) # divide the tag time by the time in between sweeps and round up to find the sweep
       tagEvents.append((tag_sweep, bit_index))
    # Fill Loop: Build bitDictionary by looping through the recording's sweeps and checking where the valves are on
    currentValve = 0
    for sweep in range(abf.sweepCount):
        for event_sweep, event_bit in reversed(tagEvents):
            if sweep >= event_sweep:
                currentValve = event_bit
                break
            else:
                currentValve = 0    
        bitDictionary[currentValve].append(sweep)
    return bitDictionary