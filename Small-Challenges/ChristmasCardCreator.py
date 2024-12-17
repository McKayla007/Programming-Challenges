# Christmas Card Creator

# ----------------
# Constants
# ----------------

ASCII_SNOWMAN = """
                .-=====-.
                |_      |
                |=      |
              '=:=======:='
               /   * *   \\
        _ .    \  '.V.'  /    ,
         >-\_  /'----'--`\  _/-<
          /  `|     *     |`  \\
              \     *     /
              /'--'-'----'\\
             |      *      |
             |             |
             \            /
               '--'---'--`
"""

ASCII_SANTA = """
      .-"```"-.
     /_\ _ _ __\\
    | /{` ` `  `}
    {} {_,_,_,_,}
       )/ 0  0 \(
      _()_          __
     { | /_)(_\ | }       _/  \\
   /`{ \        / }`\   _| `  |
  /   { '.____.' }   \ {_`-._/
 /     {_,    ,_}     \/ `-._}
|        `{--}`    \  /    /
|    /    {  }     | `    /
;    |    {  }     |\    /
 \    \   {__}     | '..'
  \_.-'}==//\\====/
  {_.-'\==\\//====\\
   |   ,)  ``     |
    \__|          |
     |     __     |
     | _   /\   _ |
     |     ||     |
     \ _ _ || _ _ /
     {` ` `}{` ` `}
     {_,_,_}{_,_,_}
      |    ||    |
      /-. _||_ .-\\
     /    /  \    \\
    |___ /    \ ___|
"""

ASCII_TREE = """
             *
            /.\\
           /..'\\
           /'.'\\
          /.''.'\\
          /.'.'.\\
         /'.''.'.\\
         ^^^[_]^^^
"""

# ----------------
# Subprograms
# ----------------

def generate_card(art, recipient_name, sender_name, message):
  match art:
    case "snowman":
      ascii_to_display = ASCII_SNOWMAN
    case "santa":
      ascii_to_display = ASCII_SANTA
    case "tree":
      ascii_to_display = ASCII_TREE
    case _:
      ascii_to_display = ASCII_TREE
  print(f"""
  {ascii_to_display}

  Dear {recipient_name},
  
  {message}
  
  Best wishes,
  {sender_name}
  """)

# ----------------
# Main program
# ----------------

art = input("Which art would you like the card to display? (snowman/santa/tree): ")
recipient_name = input("Enter the recipient's name: ")
sender_name = input("Enter your name: ")
message = input("Enter your message to the recipient: ")

generate_card(art, recipient_name, sender_name, message)
