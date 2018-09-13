class Song:
    def __init__(self, title="", artist="", duration=0.0):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return "{}, {} {}m".format(self.title, self.artist, self.duration)
