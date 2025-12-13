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
image bg empty = im.Scale("school-front.png",1920,1080)image bg empty = im.Scale("school-front.png",1920,1080)




# The game starts here.

label start:
    #ok change of plans, dream setting
    show bg empty
    show bg bedroom
    show octavia
    #alarm noise
    o"Ughh.... What time is it"
    narrator "Octavia turns to see her clock, of which reades 4:30 AM."
    o"Oh this is way to early, but to be fair I did sleep early last night"
    o"I could sleep a few more hours or I can get ready now"
    menu:
        "Sleep for a few more hours":
            o"I think I'll sleep a bit longer, let me just fix my alarm"
            show bg empty
            hide octavia
            jump regular_morning


        "Get ready now":
            o"I have enough sleep, might as well take this time to get ready"
            narrator "Octavia gets out of bed and prepares for the day ahead of her"
            jump early_morning

    return

label early_morning:
    hide octavia
    show bg school

