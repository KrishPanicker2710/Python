class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
    def add(self, s):
        self.songs.append(s)
    def remove(self, s):
        if s in self.songs:
            self.songs.remove(s)
    def display(self):
        print(self.songs)
    def __del__(self):
        print("Deleted")
p = Playlist("Road Trip", "Pop")
while True:
    ch = input("1. Add 2. Remove 3. View 4. Exit: ")
    if ch == "1":
        p.add(input("Song: "))
    elif ch == "2":
        p.remove(input("Song: "))
    elif ch == "3":
        p.display()
    elif ch == "4":
        del p 
        break