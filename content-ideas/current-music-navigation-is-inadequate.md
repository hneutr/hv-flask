What applications am I talking about?
- applications that let you have a static library
     - online or offline

---

How is it inadequate?
Music has much more information that you can currently see. Things relate in many more ways than you can show. information is kept too separate in some ways. How very abstract? Yep, this is an abstract issue: I’m talking about the relationships between the ‘things’ in a music browser. 

What information can a song have? Let’s look at an ‘dense’ example: the song ‘Don’t Let Me Down’ by the Beatles. This particular version is found on Mono Masters.

What information do we normally get when we look at this song?
iTunes:

General Information:
- Name: Don’t Let Me Down
     - Sort Name As: --
- Artist: The Beatles
     - Sort Artist As: --
- Album Artist: --
     - Sort Album Artist As: --
- Album: Mono Masters
     - Sort Album As: --
- Composer: John Lennon & Paul McCartney
     - Sort Composer As: --
- Year: 1969
- Track: 32
- Disc Number: 2
- Rating: --
- Genre: Rock
- Album is a Compilation by multiple artists: No

Misc:
- Play Count: --
- Artwork
- Lyrics

Playback Options:
- Media Kind: Music
- Start: 0:00
- Stop: 0:00
- Remember Playback Position: --
- Skip When Shuffling: --
- Volume Adjust: None
- Equalizer: None

File: 
- Kind: MPEG audio file
- duration: 3:33
- size: 8.2 MB
- bit rate: 320 kbps
- sample rate: 44.100 kHz
- channels: Joint Stereo
- id3 tag: v2.4
- encoded with: LAME3.98
- format: MPEG-1, Layer 3
- Date Modified: 0/00/00, 0:00 PM
- Location: /path/to/file

This is a lot of information. Most of it is pretty uninteresting for my gripes: things under File and Misc are pretty unarguably presented. 

But the stuff in General Information has the meat. It tells you what the key method of sorting is in iTunes. 
In iTunes a song is much more than an audio file, and an artist is much less. The only true objects that exist in the music sphere of iTunes are songs and playlists. 

What do I mean by ‘true’?
Songs and playlists are ‘true’ objects in iTunes because they actually exist in iTunes database file - a file usually located at /‘User’/Music/iTunes/iTunes Music Library.xml

I’m not saying there’s nothing else going on in iTunes, but the only two things that have their own place in the datafile are playlists and songs. 

What does this tell us?
It tells us that, apart from playlists, every other kind of ’sort’ in iTunes is based off on information in its songs. 

What does this mean?
- Sorting by Artist… or anything means:
     - going through each song in the database and looking up its field

This is certainly a valid way to store your data. But it also inhibits certain kinds of connections between data. Songs can have relations at each level: artist, album, composer, etc. But songs (and everything else) cannot relate to each other in this scheme. 

I think the only way to truly represent the diversity of connections between musical objects is to have more ‘true’ objects, and more ways of drawing connections between them.

---

This means objects are a lot more complicated. What kind of objects do I image this system having?
- songs
- artists
- sets
- tags

tags contain:
- descriptor
     - adjective: ie genre
     - artist
- unordered songs, sets

Songs contain:
- path
- duration
     - tag timestamps
- rating
- play count
- artwork
- start/stop

Nothing else. Keep it simple, stupid proof it. 
The only thing that needs explaining is tag timestamps. These can be used for indicating subtracks, i.e. in a mix, or any other kind of tag.

Now… sets. There’s a lot hiding under the covers here.
Sets can be:
- creators
- adjectives

---

What information does this song have that we might want to ‘have’?

Let’s start with the connective tissue:
Support versions of songs: a song could be a cover or remix, a live version, an acoustic version. All of these are legitimate, and can’t really be closely associated. I imagine a toggle button to show/hide ‘versions’ of a song, and each version would also continue to appear in its usual position in the sort. For two songs that otherwise sort in the same place you can either ‘always show versions’ or select a default version.


Support versions of albums: similar to songs. 

Songs and Albums:
- Version Type:
     - Version: 
          - Adjective
     - Live
          - Venue
          - Year
     - Remix/Cover
          - Original
          - Remixer (Creator)



- artists
- albums

---

why?
- it is hard to convey this information adequately

---

What already exists?
- iTunes
- Spotify
- Soundcloud
- Grooveshark

---

what are some relations I would like?
