from control_info_element import control_info_element

class road_sign(control_info_element):
    ''' A general road_sign class '''
    def __init__ (self, i, x, y, r, v):
        '''Intializes the road sign'''
        self.locationX = x
        self.locationY = y
        self.belongstoRoad = r
        self.value = v
        control_info_element.__init__(self, i)

    def changeValue (self):
        '''This function is responsible for changing the shown value on the digital road sign'''
        return None
