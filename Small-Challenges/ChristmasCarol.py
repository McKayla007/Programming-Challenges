# This program will generate lyrics for a personalised Jingle Bells carol.

# ----------------
# Constants
# ----------------

BELL_ASCII_ART = """			   			  		
				   _,--._
                                 ,'  _.._`.
                            ,^.,' ,-" _," ;
                   _,----.._\\|( _/,--"  ,<
                 ,'     ____(_))< ___..".  `.
                :  _,-"__,-" (_)-.      ,\\.  \
                :,'..-"  _,-")|(\\ `._.-"_,\\  \
                 `.__ ,-"    '-`'   \\.-"   Y  :
                 /  /:-...______...-:      |  |
                (  ( |-...______...-'      ;  ;_
                 \\ ,\\|              |     /,^/  ;._
                  `  .              .        _,'   ;
                     :              :    _,-'    ,"
                     '              ` ,-'     _,"
                    '                '    _,-"`.
                   ;`--...______,,,--":.-"     ;
                  :                    :  `..."
                  '---....______,,,,---'
                           :     ;
                            `.,."          
"""

# ----------------
# Subprograms
# ----------------

def generate_lyrics(noun, animal, place, verb):
  print(f"""
  Jingle bells, jingle bells, jingle all the way!
  Dashing through the {noun}
  On a one-{animal}-open-sleigh
  O'er the {place} we go
  {verb} all the way.
  """)


# ----------------
# Main program
# ----------------

print(BELL_ASCII_ART)
print("Welcome to the Jingle Bell project! This program will generate your very own version of 'Jingle Bells' for you!")

noun = input("Enter a noun: ")
animal = input("Enter an animal: ")
place = input("Enter a place: ")
verb = input("Enter a verb: ")

print("Here's your very own version of Jingle bells!")

song_lyrics = generate_lyrics(noun, animal, place, verb)
