# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#character defintions
define o = Character("Octavia") #add colors!!
define a = Character("Alexie")

image octavia = im.Scale("octavia-happy.png",1000,1000)
image octavia s = im.Scale("octavia-speaking.png",1000,1000)
image alexie = im.Scale("alexie-happy.png",1000,1000)
image alexie s= im.Scale("alexie-speaking.png",1000,1000)



#not important
define mom = Character("Mom",color="#808080", what_color="#000000")

#background defintions
image bg bedroom = im.Scale("bedroom.png",1920,1080)
image bg empty = im.Scale("empty.png",1920,1080)



# The game starts here.

label start:
    #ok change of plans, dream setting
    show bg empty
    #alarm sounds if i figure it out
    show bg bedroom
    show octavia
    narrator "It's about 5 am and Octavia is at her desk writing on a...bookmark?"
    show octavia s
    o "Just a few more touches..."
    show octavia
    mom "Octavia wake up-{w}oh"
    show octavia s
    o "I'm up, just let me finish this"
    show octavia 
    mom "{i}Raises eyebrows{i} alright then, have fun at school {i}Leaves{i}"
    #i really hate the direction this is taking
    narrator "Octavia, productive as ever, takes another 30 minutes writing and erasing on this bookmark of hers"
    





    
    




    return
