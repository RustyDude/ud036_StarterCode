import fresh_tomatoes
import media


# Creation of movie instances and defining attributes for each movie instance

old_boy = media.Movie("Old Boy",
                      ("After being kidnapped and imprisoned for fifteen "
                       "years, Oh Dae-Su is released, only to find that "
                       "he must find his captor in five days."),
                      "http://bit.ly/2qJPcsv",
                      "https://www.youtube.com/watch?v=iM19DAN_Ui8")

i_am_number_four = media.Movie("I Am Number Four",
                               ("Aliens and their Guardians are hiding on "
                                "Earth from intergalactic bounty hunters. "
                                "They can only be killed in numerical order, "
                                "and Number Four is next on the list. "
                                "This is his story."),
                               "http://bit.ly/2pOSxsg",
                               "https://www.youtube.com/watch?v=CfMMosvPHfQ")

life_is_beautiful = media.Movie("Life is Beautiful",
                                ("When an open-minded Jewish librarian and "
                                 "his son become victims of the Holocaust, "
                                 "he uses a perfect mixture of will, humor "
                                 "and imagination to protect his son from the "
                                 "dangers around their camp."),
                                "http://bit.ly/2pJGQ5O",
                                "https://www.youtube.com/watch?v=pAYEQP8gx3w")

shawnshank_redemption = media.Movie("The Shawnshank Redemption",
                                    ("Two imprisoned men bond over a "
                                     "number of years, finding solace "
                                     "and eventual redemption through "
                                     "acts of common decency."),
                                    "http://bit.ly/2e2Yn28",
                                    "http://bit.ly/1kIAhVe")

three_idiots = media.Movie("3 idiots",
                           ("Two friends are searching for their "
                            "long lost companion. They revisit their "
                            "college days and recall the memories of "
                            "their friend who inspired them to think "
                            "differently, even as the rest of the "
                            "world called them ""idiots""."),
                           "http://bit.ly/2pPhp10",
                           "https://www.youtube.com/watch?v=K0eDlFX9GMc")

ip_man = media.Movie("Ip Man",
                     ("During the Japanese invasion of 1937, when a wealthy "
                      "martial artist is forced to leave his home and work "
                      "to support his family, he reluctantly agrees to train "
                      "others in the art of Wing Chun for self-defense."),
                     "http://bit.ly/2pJK0WR",
                     "https://www.youtube.com/watch?v=SZtSwjk4aD8")

# List of the movie instances
movies = [old_boy, i_am_number_four, life_is_beautiful,
          shawnshank_redemption, three_idiots, ip_man]

# Creating html movies page
fresh_tomatoes.open_movies_page(movies)
