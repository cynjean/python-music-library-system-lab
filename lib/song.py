class Song:
    """Represent a song and maintain aggregate statistics across all songs."""

    # These collections belong to the class so every song contributes to one library.
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}
    # Keep the singular spelling as an alias for the original lab tests/API.
    artist_count = artists_count

    def __init__(self, name, artist, genre):
        """Store a song's details and update the library-wide statistics."""
        self.name = name
        self.artist = artist
        self.genre = genre

        # Run each update through a class method to keep the bookkeeping in one place.
        type(self).add_song_to_count()
        type(self).add_to_genres(genre)
        type(self).add_to_artists(artist)
        type(self).add_to_genre_count(genre)
        type(self).add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the number of Song instances created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre once, preserving the order in which genres appeared."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist once, preserving the order in which artists appeared."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Count one more song for its genre."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Count one more song for its artist and keep both attribute names in sync."""
        # Existing starter tests reset `artist_count` directly, while the assignment
        # specifies `artists_count`; honor a reset of either spelling.
        if cls.artist_count is not cls.artists_count:
            if not cls.artist_count and cls.artists_count:
                counts = cls.artist_count
            elif not cls.artists_count and cls.artist_count:
                counts = cls.artists_count
            else:
                counts = cls.artists_count
        else:
            counts = cls.artists_count

        counts[artist] = counts.get(artist, 0) + 1
        cls.artists_count = counts
        cls.artist_count = counts
