class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  def get_title(self):
    # print(self.__title)
    return self.__title
  
  def set_title(self, title):
    self.__title = title
     
  def get_next_song(self):
    # print(self.__next_song)
    return self.__next_song

  def set_next_song(self, next_title):
    self.__next_song = next_title
    
  def __str__(self):
    # print(f"You are listening to {self.__title}")
    return f"Current Song: {self.__title}\nNext Song:    {self.__next_song}"

  def __repr__(self):
    # print(f"{self.__title} -> {self.__next_song}")
    return f"{self.__title} -> {self.__next_song}"


# song = Song("Can't Touch This")

# print("SONG TITLE METHODS")
# song.get_title() 
# song.set_title("Believer")
# song.get_title() 

# print("\nNEXT SONG METHODS")
# song.get_next_song()
# song.set_next_song("Change")
# song.get_next_song()

# print("\nDUNDER METHODS")
# song.__str__()
# song.__repr__()