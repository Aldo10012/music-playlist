from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    if (self.__first_song == None) :
        print("adding first song")
        self.__first_song = Song(title)
        print(self.__first_song._Song__title)
        return
    
    print("adding new song")
    current = self.__first_song
    # while Current.next is not empty, make current = current.next
    while current._Song__next_song != None: 
        current = current._Song__next_song
    current._Song__next_song= Song(title)
    current = current._Song__next_song

    print(current.get_title())


  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index.
  # The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index. Otherwise, return -1.

  def find_song(self, title):
    pass


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    pass



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    if (self.__first_song == None) :
        print("you have 0 songs")
        return

    count = 0
    current = self.__first_song
    while current != None:
        count += 1
        current = current._Song__next_song
        
    print(f"you have {count} songs")


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    if (self.__first_song == None) :
        print("you don't have any songs")
        return
    
    current = self.__first_song
    count = 1
    while current != None:
      print(f"{count}. {current.get_title()}")
      current = current._Song__next_song
      count += 1


my_playlist = Playlist()

my_playlist.length()
my_playlist.print_songs()
print("")
my_playlist.add_song(Song("Believer"))
print("")

my_playlist.add_song(Song("Hotel California"))
print("")

my_playlist.add_song(Song("Let it Go"))
print("")
my_playlist.length()
my_playlist.print_songs()
