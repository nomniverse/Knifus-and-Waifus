# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("Me")

# Love Interests
define miki   = Character("Miki", image="miki") # Childhood friend
define hana   = Character("Hana", image="hana") # Klutz
define aiko   = Character("Aiko", image="aiko") # Yandere

# Side Characters
define sora   = Character("Sora", image="sora") # ???
define miho   = Character("Miho", image="miho") # Bully

# Defaults
default player_name = "John Smith"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg mc_bedroom

    "Another day... just another average day."

    "Honestly, it's a bit of a relief that nothing exciting happens like in fiction. But still..."

    "It would be nice to at least have something a bit different happen for once."

# Player and Miki walk to school together
label w1d3_to_school:

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene bg street

    "Like always, my best friend since basically birth is waiting for me so we can walk to school together."

    player "Yo! How's it going?"
    
    show miki winteruni sidetail smile

    # These display lines of dialogue.

    miki "Hey there, stranger, what's your name?"

    $ player_name = renpy.input("Weird of your friend to ask your name, but go ahead and tell her anyways:")
    $ player_name = player_name.strip()

    player "Did someone steal your memories or something? You should know it's [player_name]..."

    miki "Who??? Just kidding, [player_name], I could never forget my best friend."

    player "Of course you couldn't. I'm the only person at school that would put up with how weird you are sometimes."

    miki winteruni sidetail frown blush "Hey! Shut up. It's not like I chose you to be my friend anyways. We just happen to live next door..."

label w1d3_school_arrival:
        
    scene bg school_exterior
    
    "By the time we were done arguing with each other about who was the more misfortunate friend, we had already made it school."

    player "Whatever, just remember that you're always the one that texts me saying you're bored and want to hang out."

    show miki angry
    
    miki "Well yeah, it's not like any of my friends from class live anywhere close to us."

    player "What friends?"

    "Almost as if on cue, a girl from our class that I only vaguely recognised walked up to us."

    show hana neutral
    
    hana "Hi Miki... Hi [player_name]... Sorry if I'm interrupting, but can I ask you two a favour?"

    "Wonder what this was about?"

    show hana neutral at left
    show miki happy at right
    
    miki "What's up Hana, my friend?"

    "I could feel the spite towards me as Miki emphasised 'my friend'."
    
    hana conerned "Could I get a bit of your lunches later? I forgot mine at home..."

    miki concerned "Did you forget it at home, or did Miho dump your bento box again?"

    "Hana and Miho went to middle school together and both decided to go the our high school. According to some of their middle school classmates, Miho always was bullying Hana."

    player "You really should tell the teacher if Miho's giving you a hard time."

    hana "I've tried... The teachers never believe me, saying a nice girl with such upstanding parents could never be so rotten."

    miki "That's a load of crap! You should show them all the posts on MyBook that Miho makes about you."

    miki "Give them proof that she's been antagonising you since middle school."

    hana "I tried... Miho claimed that some jealous girls hacked her account."

    miki "Obviously, we need to find proof that the teachers can't deny! [player_name], don't you agree?"

    menu:

        "Oh no... Miki is probably going make this a whole dramatic ordeal... Should I agree with her?"

        "Yeah, Hana needs our help!":

            miki "I knew you couldn't resist helping a poor soul, [player_name]!"

            hana "Thank you both, but you really shouldn't bother."

            player "Like Miki said, there's no way we can let you continue getting pushed around by Miho."

            hana "I appreciate it..."

        "No, it's none of our business.":

            miki "You can't be serious! Hana is going to keep getting bullied if no one helps her."

            hana "Miki, it's fine... really."

            miki "[player_name], I'm not going to let you turn your back on someone in need like this. You're helping Hana, that's final."

            player "I guess I don't get a say... sure."
            
label w1d3_getting_background_info:

    miki "Anyways, now that we're helping you, we need to know as much as possible about the situation."

    player "Yeah, makes sense. So Miki, what are you even planning to do?"

    miki "Oh, don't you worry. I have a brilliant plan! Meet me at the library after school, I'm gonna skip class to get some stuff."

    player "Wait, you can't just leave!"

    miki "You'll just make up an excuse to our teacher for me, right [player_name]?"

    hide miki

    show hana at center

    player "Dang it... What am I gonna tell our teacher next period?"

    hana "Shouldn't she not skip school?"

    player "Miki will do whatever she wants, you'll get used to it..."

    player "Anyways, so about you and Miho..."

    hana "Yeah..."

    "Looks like she might not be comfortable just telling me everything..."
    
default w1d3_hana_interrogation = set()

label w1d3_hana_interrogation:
    
    menu:

        set w1d3_hana_interrogation

        "What should I try getting Hana to tell me about?"

        "How do you know Miho?":

            hana "Well, her and I happened to be in the same class all through middle school."

            player "I see."

            jump w1d3_hana_interrogation

        "Where does she normally bully you?":

            hana "Well, she bullies me wherever she gets a chance to honestly..."

            player "Oh? Well does she bully you anywhere more often?"

            hana "I guess... she likes to steal things out of my locker or trash it."

            jump w1d3_hana_interrogation

        "Any idea why she bullies you so much?":

            hana "Hm..."

            hana "Hm...."

            hana "Hm....."

            hana "I really don't know. She's been awful to me ever since we've met."

            jump w1d3_hana_interrogation

        "I think that's enough information." if len(w1d3_hana_interrogation) >= 3:

            jump w1d3_library

label w1d3_library:

    "As expected, Hana and I found Miki at the library."

    show miki happy
    
    miki "C'mon [player_name], it's rude to keep a lady waiting."

    player "You're a lady? Could have fooled me."

    show miki frown
    
    miki "Hey shut up, smart ass. That's 10 de-merits!"

    player "You've watched too many high school anime..."

    show hana neutral at left

    show miki neutral at right
    
    hana "So Miki, what did you have to go get?"
    
    miki "This!"

    "Miki pulled out a camera from her bag."

    miki "I went home to grab this. I figured if we take pictures of you getting bullied, the teachers will have to believe you."

    player "You know your phone takes pictures right?"

    miki "See you'd think that, but then Miho could just say they're photoshopped or something. With this Polaroid camera, it'll be a lot harder to say the pictures were doctored."

    player "You just wanted to justify spending your paycheck last summer on that thing."

    show miki frown blush at right
    
    miki "Shut up!"

label demo_end:

    "This is just the demo version for NaNoRenO 2020. Hopefully it gets more content in the future!"
        
    # This ends the game.
    return
