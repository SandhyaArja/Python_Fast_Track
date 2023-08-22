class LightSwitch:
    def __init__(self):
        self._is_on=False 
    @ property 
    def is_on(self):
        return self._is_on
    def turn_on(self):
        self._is_on=True 
    def turn_off(self):
        self._is_on=False 
switch=LightSwitch ()
print(switch._is_on)
switch.turn_on()
print(switch._is_on)
switch.turn_off()
print(switch._is_on)
