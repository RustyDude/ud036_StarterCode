import webbrowser


class Movie():
    """Creates a movie object.

    Initialize neccesary contents of movie object.
    Provide a function to show movie's trailer.

    Attributes:
        title (str): Name/Title of the movie.
        storyline (str): A short summary of the movie's story.
        movie_poster (str): A poster image of movie.
        trailer_youtube_url(str): A trailer video of the movie.

    Functions:
        show_trailer : Opens a pop-up window for showing a movie's trailer.
    """

    # Movie initailization
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # Movie contents
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Opens pop-up movie trailer
        webbrowser.open(self.trailer_youtube_url)
