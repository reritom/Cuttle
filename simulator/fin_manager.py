from fin_model import FinModel

class FinManager():
    '''
        This class handles the creation, updating, and logging of all the fins in each track
    '''
    def __init__(self, number):
        self.number_of_registers = number
        self.tracks = {"Starboard": [], "Portside": []}

        self.initialiseTracks()

    def initialiseTracks(self):
        '''
            This method propagates each of the fins
        '''
        for track in self.tracks:
            for i in range(self.number_of_registers * 8):
                self.tracks[track].append(FinModel())

    def runRound(self, starboard_track, portside_track, delta):
        return self.updateFins(starboard_track, portside_track, delta)

    def updateFins(self, starboard_track, portside_track, delta):
        '''
            This method receives the starboard and portside daisychain arrays, and the time delta, to
            update the fin position calculations, and then returns an array of fin positions for each
        '''
        starboard_fin_positions = []
        for index, bit in enumerate(starboard_track):
            starboard_fin_positions.append(self.tracks['Starboard'][index].runRound(bit, delta))

        portside_fin_positions = []
        for index, bit in enumerate(portside_track):
            portside_fin_positions.append(self.tracks['Portside'][index].runRound(bit, delta))

        return starboard_fin_positions, portside_fin_positions
