from control_info_element import control_info_element

class road_sign(control_info_element):
    ''' A general road_sign class '''
    def __init__ (self, i, x, y, r, v):
        self.locationX = x
        self.locationY = y
        self.belongstoRoad = r
        self.value = v
        control_info_element.__init__(self, i)

    def changeValue (self):
        return None
