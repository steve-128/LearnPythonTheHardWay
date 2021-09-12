class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

never_gonna_give_you_up = Song(["Never gonna give you up","Never gonna let you down",
"Never gonna run around and desert you"])
never_gonna_give_you_up.sing_me_a_song()

line1= "Never gonna make you cry"
line2 = "Never gonna say goodbye"
line3 = "Never gonna tell a lie and hurt you"
never_gonna_give_you_up_2 = Song([line1,line2,line3])
never_gonna_give_you_up_2.sing_me_a_song()