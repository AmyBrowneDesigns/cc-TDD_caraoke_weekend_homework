class Room:

    def __init__(self, room_name, till):
        self.room_name = room_name
        self.till = till
        self.song = []
        self.guest = []
    
    def add_song(self, song):
        self.song.append(song)

    def check_song_list(self):
        return len(self.song)
    
    

