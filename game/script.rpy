# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#character defintions
define o = Character("Octavia") #add colors!!
define a = Character("Alexie")
define c = Character("Cynthia", color="#ff69b4")
define l = Character("Lilith", color="#8a2be2")

image octavia = im.Scale("octavia-happy.png",1000,1000)
image octavia s = im.Scale("octavia-speaking.png",1000,1000)
image alexie = im.Scale("alexie-happy.png",1000,1000)
image alexie s= im.Scale("alexie-speaking.png",1000,1000)



#not important
define mom = Character("Mom",color="#808080", what_color="#000000")

#background defintions
image bg bedroom = im.Scale("bedroom.png",1920,1080)
image bg empty = im.Scale("empty.png",1920,1080)
image bg school-front = im.Scale("school-front.png",1920,1080)
image bg school = im.Scale("school.png",1920,1080)

#Variables
default alexie_relation=0
default gift="none"




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
            narrator "Octavia sets her alarm for another hour and goes back to sleep"
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
    c "Must be hard to transfer mid year huh?"
    c "Yeah, but I heard they finished the placement test early{w} without studying"
    show octavia with moveinright
    o "Hey, who are you talking about?"
    c"Our class is getting a new student today"
    l"Yeah, I heard she is from out of state, and she will be sitting next to you!"
    narrator "Octavia's eyes open excitedly at the prospect of meeting a new person"
    o"Really? I cannot wait to meet her!"
    #bell ringing
    narrator "Octavia scrambles to her seat and looks to the empty desk to her right"
    o"{i}Maybe i should leave something on her desk as a welcome gift{/i}"
    menu:
        "Leave a small gift on her desk":
            o"Yeah, maybe that would be nice, what should I give her?"
            menu:
                "Welcome note":
                    $ gift_given= "note"
                    o"I think a welcome note would be nice to leave her"
                    narrator"Octavia quickly scribbles on a sticky note  and leaves it on the desk"

                "Snacks":
                    $ gift="snack"
                    o"Morning classes can be rough, perhaps a snack would be able to help her out"
                    narrator"Octavia grabs a granola bar from her bag and leave it on the desk"
            narrator"Octavia looks up anxiously at the clock, metally timing for when the late bell will ring, and when the student will arrive"
    jump school_intro
    return

label regular_morning:
    show bg empty
    #alarm noise, ill be actually needing to find sound files later
    narrator "An hours later, Octavia's alarm goes off again"
    show bg bedroom
    show octavia
    o "I feel so well rested now"
    narrator "Octavia gets out of bed and prepares for the day"
    hide octavia
    show bg school-front
    #fix postioning with octavia and alexie 😅
    show octavia with moveinright
    o "Hope im not late for class-"
    narrator "Octavia collides into a person walking in the opposite direction"
    show alexie with moveinleft
    o"Oh my gosh, I am so sorry!"
    narrator"She leans down and helps pick up the books that fell"
    a "It's okay, no harm done"
    narrator "As Octavia looks up, she notices that the person is an unfamilar face"
    o "Wait, are you new here?"
    a "Yeah actually, I transferred today"
    o"Today? Wow, welcome to our school!"
    narrator"The girl laughs softly"
    a "Thanks, I'm Alexie by the way"
    narrator"Octavia smiles warmly back and holds out a hand"
    o"I'm Octavia, nice to meet you"
    #first bell rings
    a"Oh no, does that mean we're late?"
    o"No we still have a few minutes, I can show you to your class"
    narrator "Alexia nodded gratefully as Octavia led her into the school building"

    jump school_intro

label school_intro:
    if gift != "none":
        show octavia at right
        narrator "The school bell rang and Octavia took her seat, glancing anxiously at the empty desk beside her"
        narrator "A girl with short brown hair and glasses enter, looks around, and sees the empty desk"
        show alexie at with moveinleft
        a "Hi, is this seat taken?"
        narrator "Octavia shakes her head and smiles warmly"
        narrator "Alexie takes her seat and notices something on her desk"
        if gift=="note":
            narrator "She picks up the sticky note and read it, a small smile dawning on her face"
            narrator "She looked over at Octavia and mouthed a small thank you"
        elif gift=="snack":
            a"test2"
    else:
        a"test3"
    
