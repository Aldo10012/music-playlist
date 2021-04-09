from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None



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


  def find_song(self, title):
    if (self.__first_song == None) :
        print("you don't have any songs :(")
        return

    index = 0
    current = self.__first_song

    while current != None:      
      if f"{current.get_title()}" == f"{title}":
        print(f"'{title}' is at index {index}")
        return

      index += 1
      current = current._Song__next_song

    print("cound not find your song") 
      

  def remove_song(self, title):
    current = self.__first_song

    if f"{current.get_title()}" == title:
      print("remove")   
      print(f"next song: {current.get_next_song()}")
      current = current.get_next_song()

    while current != None:
      if f"{current.get_next_song()}" == title:
        print("removed!")
        current.set_next_song(current.get_next_song().get_next_song()) 
        return
      
      current = current._Song__next_song
    pass


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
    return f"you have {count} songs"



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
my_playlist.find_song('Believer')
print("")
my_playlist.add_song(Song("Believer"))
print("")

my_playlist.add_song(Song("Hotel California"))
print("")

my_playlist.add_song(Song("Let it Go"))
print("")

my_playlist.length()
my_playlist.print_songs()

print("\nFIND SONG")
my_playlist.find_song("Believer")

print("\nREMOVE SONG")
my_playlist.remove_song("Let it Go")
my_playlist.print_songs()



"""
BUGS:

1. find_song() isn't working anymore, fix it
2. remove_song() isn't removing 1st song in list.
"""