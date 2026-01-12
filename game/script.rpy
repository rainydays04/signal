# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#character defintions
define o = Character("Octavia") #add colors!!
define a = Character("Alexie")
define c = Character("Cynthia", color="#ff69b4")
define l = Character("Lilith", color="#8a2be2")
define li = Character("Librarian", color="#deb887")
define w = Character("????", color="#ff0000")

image octavia = im.Scale("octavia-happy.png",1000,1000)
image octavia s = im.Scale("octavia-speaking.png",1000,1000)
image alexie = im.Scale("alexie-happy.png",1000,1000)
image alexie s= im.Scale("alexie-speaking.png",1000,1000)
image librarian= im.Scale("librarian.png",1000,1000)


#not important
define mom = Character("Mom",color="#808080", what_color="#000000")

#background defintions
image bg bedroom = im.Scale("bedroom.png",1920,1080)
image bg empty = im.Scale("empty.png",1920,1080)
image bg school-front = im.Scale("school-front.png",1920,1080)
image bg school = im.Scale("school.png",1920,1080)
image bg schoolyard = im.Scale("yard.png",1920,1080)
image bg library = im.Scale("library.png",1920,1080)
image bg sidewalk = im.Scale("sidewalk.png",1920,1080)
image bg movie = im.Scale("movies.png",1920,1080)
image bg chair = im.Scale("chairs.png",1920,1080)
image bg cafe = im.Scale("cafe.png",1920,1080)


#Variables
default alexie_relation=0
default gift="none"
default movie=False
default sus =False
default info_1=False
default cat_1=False
default genre="none"




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
                    $ gift= "note"
                    o"I think a welcome note would be nice to leave her"
                    narrator"Octavia quickly scribbles on a sticky note  and leaves it on the desk"

                "Snacks":
                    $ gift="snack"
                    o"Morning classes can be rough, perhaps a snack would be able to help her out"
                    narrator"Octavia grabs a granola bar from her bag and leave it on the desk"
                    narrator"Octavia looks up anxiously at the clock, metally timing for when the late bell will ring, and when the student will arrive"
        "Do not leave a gift":
            jump school_intro
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
    show octavia at right with moveinright
    o "Hope im not late for class-"
    narrator "Octavia collides into a person walking in the opposite direction"
    show alexie at left with moveinleft
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
    show bg school
    show octavia at right
    narrator "The school bell rang and Octavia took her seat, glancing anxiously at the empty desk beside her"
    narrator "A girl with short brown hair and glasses enter, looks around, and sees the empty desk"
    show alexie at left with moveinleft
    a "Hi, is this seat taken?"
    narrator "Octavia shakes her head and smiles warmly"
    if gift != "none":
        narrator "Alexie takes her seat and notices something on her desk"
        if gift=="note":
            narrator "She picks up the sticky note and read it, a small smile dawning on her face"
            narrator "She looked over at Octavia and mouthed a small thank you"
            $ alexie_relation +=10
        elif gift=="snack":
            narrator "Alexie sat at her desk and noticed a granola bar while Octavia watched from the corner of her eye"
            narrator "She looked at the snack and then at Octavia, nodding in appreciation"
            $ alexie_relation +=5
    else:
        a"Thank you for the warm welcome and showing me to class"
        o "Of course! If you need anything else feel free to ask me"
    hide octavia
    hide alexie
    jump lunch_day1
    return

label lunch_day1:
    show bg schoolyard
    show octavia at right
    narrator "During lunch break, Octavia sat with her friends in the schoolyard"
    narrator "She glanced over at Alexie, who was sitting alone at a nearby table"
    show alexie at left
    menu:
        "Why are you sitting alone?":
            narrator "Alexie looks over and smiles softly, shaking her head quietly and returns to her food"
        "You should come sit with us!": 
            narrator "Alexie looks over and smiles softly, shaking her head quietly and returns to her food"
   
    o"Oh...Maybe next time then"
    narrator "Octavia feels a bit disappointed, but decides to enjoy her lunch with her friends"
    hide octavia with moveoutleft
    hide alexie
    hide bg schoolyard
    jump afternoon_day1
    return

label afternoon_day1:
    show bg school
    show octavia at center
    c "Octavia, did you finish the math homework from yesterday?"
    narrator "Octavia was looking wistfully at her silent and distant deskmate"
    c "Helllo? Earth to Octavia!"
    o "Oh! Sorry Cynthia. What were you saying?"
    narrator "Cynthia raised an eyebrow"
    c "Something on your mind?"
    o "Yeah kinda. I was just wondering about the new student, you know, Alexie?"
    c "Ohhhhh, yeah. You didn't hear? She is hella smart, but has difficulty talking to others"
    narrator "Octavia cocked her head"
    o"Really? She seemed rather sociable to me earlier"
    narrator "Cynthia shrugged"
    c "I can't speak on her behalf, but you seem rather interested in her"
    o "I just wanna get to know her better, she seems nice"
    narrator "Cynthia went back to her work as Alexie came into the classroom"
    hide octavia
    hide bg school
    show bg empty
    jump library_day1
    return

label library_day1:
    show bg library
    show octavia at left
    narrator "After school, Octavia went to fullfill her weekly library duties"
    narrator "As she was organizing books, the librarrian approached her, Alexie trailing behind"
    show librarian at right with moveinright
    li "Octavia, just who I was looking for"
    li "I'm sure you met Alexie earlier today. She said she was interested in the library program"
    narrator "The librarian left Alexie and Octavia alone to work"
    hide librarian with moveoutright
    show alexie at right with moveinright
    menu:
        "offer help":
            narrator"Octavia explained the process of checking out books and offered to help Alexie find some books that she might like"
        "ask about interests":
            narrator"Octavia asked Alexie about her interests and suggested some books she might like"
            a"I really like horror and mystery novels"
            a"I was actually going to see the next showing of 'The Conjuring 2' this weekend"
            menu:
                "recommend a similar book":
                    o"The book 'The Hauting of Ninth Avenue' has a similar plot, you might like it!"
                    $alexie_relation +=5
                "Ask about the movie":
                    o"Oh? I love 'The Conjuring' series. I didn't know they were bringing it back in theaters"
                    a"Yeah, I got two tickets, but my friend bailed since she hard it was scary"
                    menu:
                        "Offer to go together":
                            $ movie=True
                            o"I'd be willing to go with you if you'd like. I'll bring some snacks too"
                            a"Really? That'd be great! Here is my number, I'll send the plans later this afternoon"
        "stay silent":
            narrator"Octavia, too nervous to speak, simply nodded and continued her work"
            narrator "Alexie, already comfortable in the silence, joined her in organizing the books"
    hide octavia
    hide alexie
    jump end_day1

label end_day1:
    show bg bedroom
    show octavia
    narrator "Octavia returned to her home for the day"
    if movie==True:
        narrator"she gets a text from Alexie with the movie plans"
        a"Hey Octavia. This is Alexie. The movie starts at 7pm on Saturday at the Grand Cinema. See you then!"
    else:
        narrator"She reflects on the day and wonders how she can get to know Alexie better"
    jump day2_start


label day2_start:
    hide octavia
    show bg empty
    narrator "The next day, Octavia is walking towards the school when she saw Alexie"
    show bg sidewalk
    show octavia at right
    show alexie at left with moveinleft
    narrator "As Octavia was trying to approch her, she realized Alexie was mumbling something to herself"
    narrator "She saw that Alexie was...talking to herself about..."
    a"You said you wouldn't follow me today..."
    w"I just need to make sure you're safe. The organization can't let anything happen to you"
    o"{i}Organization? What is she talking about?{/i}"
    menu:
        "Confront her about it":
            o"Alexie, whoa re you talking to?"
            narrator"Alexie jumps slightly, startles by Octavia's sudden presence"
            a"Oh,nobody. Nobody, just talkig to myself"
            narrator "From behind her a black cat darts away"
            a"Are you headed to school too?"
            o"Yeah, wanna walk together?"
            a "Sure"
            jump day2_walk
        "Stay silent and see what happens":
            $ sus =True
            a "They promised me I would be safe and could just go to school"
            w"You know we still need to monitor you. Just in case anything happens"
            a "I don't need monitoring, I can take care of myself"
            if movie==True:
                w"What about that girl you invited to the movies? How are you sure she is trustworthy?"
                a "She's fine...strangely sociable, but fine"
            else:
                w"What about the people you interact with at school? How are you sure they are trustworthy?"
                a "They're fine...People leave me alone for the most part, so I'm fine"
            narrator "As Alexie spoke, Octavia noticed a black cat sitting in front of Alexie, seeming to be the one talking"
            narrator"The cat darts away as it notcies Octavia causing Alexie to turn behind her"
            menu:
                "Approach Alexie":
                    o"Alexie, whoa re you talking to?"
                    narrator"Alexie jumps slightly, startles by Octavia's sudden presence"
                    a"Oh,nobody. Nobody, just talkig to myself"
                    narrator "From behind her a black cat darts away"
                    a"Are you headed to school too?"
                    o"Yeah, wanna walk together?"
                    a "Sure"
                    jump day2_walk
                "Run away":
                    narrator"Before Alexie could notice her, Octavia quickly hurried away from towards the school"
                    hide octavie with moveoutright
                    jump day2_school
label day2_walk:
    $ info_1=True
    hide alexie
    hide octavia
    show bg school
    narrator "Octavia and Alexie walked to school together, the earlier incident left Octavia feeling curious about Alexie"
    show octavia at right with moveinright
    show alexie at left with moveinright
    a "So how much did you hear?"
    o "Honestly, not much. Just you talking to someone and a cat"
    if sus==True:
        o"And something about an organization?"
        a"..."
        narrator "Alexie hesitated for a moment, looking around if anyone was listening"
        narrator "She pulled Octavia to the side and whispered"
        a "Look, I don't know how much you heard, bu I cannot tell you much about it"
        a "Just do not mention it to anyone else, okay? Especially the cat"
        narrator "Octavia nodded, feeling more confused than before"
    else:
        narrator"Alexie raised her eyebrows"
        a "I see.. well, it's a long story I'll share with you another time"
        o "Alright, sure, no rush"
    jump day2_lunch



label day2_school:
    hide alexie
    hide octavia
    show bg school
    narrator "Octavia entered the school building, heading towards her desk"
    narrator "She watched as Alexie entered the classroom and took her seat"
    jump day2_after

label day2_lunch:
    hide octavia
    hide alexie
    show bg schoolyard

    narrator "The rest of the day passed by uneventfully until lunch break"
    show octavia at right
    narrator "Octavia was writing in her notebook when she looked up and noticed a black cat sitting on a nearby bench"
    o"{i}Isn't that the cat from this morning?{/i}"
    narrator "The cat seemed to star at her, unblinking, as it approached her"
    w "You shouldn't talk to her"
    o"{i}What the...did that cat just talk?{/i}"
    narrator "She stared down at the cat, unsure how to respond"
    w"She is dangerous you know. You shouldn't trust her"
    o"Who are you?"
    narrator "The cat simply smiled up at her"
    w "I'm just looking out for the both of you"
    narrator "Before Octavia could respond, Alexie approached just as the cat darted away once more"
    show alexie at left with moveinleft
    a "Hey, is everything okay? You're not sitting with youre usual friends"
    o "Yeah, everything's fine. Just saw a cat I recognized"
    narrator"At the mention of a cat, Alexie's expression darkened slightly"
    a "A cat you say?"
    narrator"Octavia nodded as Alexie looked at her, waiting for more information"
    menu:
        "Tell her about the cat":
            o"Yeah it was a black cat, seemed to be trying to warn me about something"
            narrator"Alexie mumbled under her breath"
            a"I can't even catch a break..."
            o"What do you mean by that?"
            narrator "Alexie shook her head"
            a "It's nothing"
            narrator"Octavia felt that Alexie was hiding something, but decided not to press the issue"
        "Stay silent":
            o"Yeah it just reminded me of something from a tv show I watched"
            narrator "Alexie nodded, accepting the explantion, but it still seemed slightly bothered"
    o "Do you want to sit with me? I don't mind the company. I usuall eat alone on Fridays since my friends have a club meeting at this time"
    a "Sure, thanks"
    jump day2_after

label day2_after:
    hide octavia
    hide alexie
    show bg empty
    narrator "The rest of the day passed uneventfully"
    show bg bedroom
    show octavia
    narrator "Octavia prepared to study at her desk"
    if info_1==True:
        narrator"As Octavia worked on her schoolwork, she wondered about Alexie and what the cat had warned her"
        o"{i}Be careful around her? What harm could possibly come of a high schooler could do? {/i}"
        narrator"Octavia leaned back in her chair and thought about it more"
        o"Back to think about it, why and how was the cat talking to me. I was so in shock that I never questioned it"
        narrator "Distracted from her work, she began to research into Alexie, but before she could finish up she got a tect"
        if movie==True:
            narrator"Alexie: Still on for the movie tomorrow?"
            narrator"Octavia: Sure yeah"
            narrator"Alexie: Yeah I was just curious after the whole cat thing"
            narrator"Octavia: You wanna talk more about that cat thing? It seems rather important to you, Sailor Moon"
            narrator"Alexie: I'll talk about it at the movies"
        else:
            $ movie=True
            narrator "Alexie: Hey you want to talk, You seemed kinda distracted at lunch"
            narrator"Octavia: Nothing, it's probably just that my friends were out and I was kinda tired"
            narrator"Alexie: How about you come to the movie I'm going to tomorrow? It's a horror"
            o"{i}Didn't the cat tell me not to...{/i}"
            menu:
                "Accept her request":
                    narrator"Octavia: Sure, I'm not during anything"
                    narrator"Alexie: Great, here is the address"
                "Decline her request":
                    narrator"Octavia: I'm not a fan of horror. Bet if I pass up on this"
                    narrator"Alexie: You should come. Here are the details"
                    narrator"Octavia laid back in her desk"
                    o"I guess it's a date"


    else:
        #expand meow
        narrator"After Octavia had finished her school work, she saw that there was a sale on movie tickets online"
        o"{i}Oh that'll be nice for a little break. What movie should I watch?{/i}"
        menu:
            "The Conjuring":
                $ genre="horror"
                o"I don't really like scary movies, but it's always nice to get out their comfort zone"
            "10 Things I Hate About You":
                $ genre="romance"
                o"I love a good romance movie and this is a classic"
    jump movie_day
    

label movie_day:
    show bg empty
    hide octavia
    narrator"The showing for the movie was at 8:30 am. The theatre was only a few blocks away, so octavia got there relatively early to prepare her "
    show bg movies
    show octavia with moveinright
    narrator"Upon entering she sees Alexie in line for popcorn"
    if movie==True:
        narrator "Octavia runs over to her excitedly"
        show alexie with moveinleft
        a"Oh hey, you made it"
        o"Yeah, I am so excited for this movie. Scared. But im excited I am seeing it with you."
        narrator"They both walk into the theater for the movie"
    else:
        narrator"Not having anticipated Alexie's presence, she walks over to talk to her, curious about what movie she is seeing"
        show alexie with moveinleft
        o"Alexie?"
        narrator"Alexie turns around in a bit of a shock, calming down when she sees it is Octavia"
        a"Octavia? I didn't expect to see you here, what movie are you watching?"
        if genre ="horror":
            o"I am going to see The Conjuring"
            a"Me too! How about we see it together"
            o"Alright"
        else:
            o"I am seeing 10 Things I Hate About You"
            a"Oh it's that one romance movie right?"
            o"Yeah, what movie are you seeing?"
            a"The Conjuring"
            o"Oh I have been wanting to see that movie for a while now, but I'm too scared to see it alone"
            a"Well I have an extra ticket anyway sooo"
            narrator "Octavia's eyes lit up when she heard that"
            o"Yeah, I didn't buy my tickets yet"
            narrator"Alexie took out her extra ticket and they walked into the theater together"
    hide alexie with moveoutright
    hide octavia with moveoutright
    show bg chairs
    show alexie with moveinright
    show octavia with moveinright
    narrator"They both settled into their chairs as the movie started"
    hide alexie
    hide octavia
    show bg empty
    narrator"At the end of the movie, the two went out to a cafe to talk"
    show bg cafe
    show alexie
    show octavia
    o"This is a nice cafe, thanks for bringing me here"
    a"Of course, um, there is something I need to talk to you about something"
    narrator"Octavia leans in with intruige"
    o"Yeah, what is it?"
    a"So you know the cat from lunch?"
    a"I NEED you to tell me what she told "
    narrator"Octavia leaned back, suprised by Alexie's insistance"
    o"She just told me to be careful...of you"
    narrator"Alexie leaned back in frustration"
    a"Sorry you had to go through that, I know a talking cat is very...strange"
    o"What's stranger is this whole interaction, you clearly have something to tell me"
    narrator"Alexie takes a long exasperated breathe"
    a"You know like, magical girls in those boooks and stories?"
    o"Yeah"
    


        
    
