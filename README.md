# Cuttle

# TODO
- Define how to change pulsewidth and wave size by command
- Shift out the array changes (optimise for forward movement?)
- In trackDriver, parse the command and set the daisy loop
- Move daisy last-bit loop in trackDriver from daisychain


'''
  Accepted messages to the trackManager:
  - SFxxx - Starboard forward with thrust value between 000-100
  - SRxxx - Starboard reverse
  - SOxxx - Starboard override
  - PFxxx
  - PRxxx
  - POxxx

'''
