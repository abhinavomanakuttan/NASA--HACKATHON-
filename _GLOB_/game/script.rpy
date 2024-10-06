﻿# Declare characters used by this game.
define s = Character(_("Sylvie"), color="#c8ffc8")
define m = Character(_("Me"), color="#c8c8ff")
define q = Character(_("Nyla"))
define g = Character(_("GAME"))

image pic_1 =im.Scale("pic1.jpg",1920,1080)
image pic_2 =im.Scale("df.jpg",1920,1080)
image pic_3 =im.Scale("df2.jpg",1920,1080)
image pic_4 =im.Scale("for.jpg",1920,1080)
image boy =im.Scale("boy2.jpg",1920,1080)
image girl =im.Scale("girl3.jpg",1920,1080)
image girl2 =im.Scale("girl2.jpg",1920,1080)
image ph =im.Scale("ph.jpg",1920,1080)
image river =im.Scale("river.jpg",1920,1080)
image river2 =im.Scale("river2.jpg",1920,1080)

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False

# The game starts here.
label start:

    # Start by playing some music.
    play music "illurock.opus"

    scene bg lecturehall
    with fade
    
    show pic_1

    "A group of students are gathered around to reasearch on the GLOBE program with a focus on environmental conservation."

    s "Hey let us introduce ourself,Lets start with me, Am Sylvie a research student "
    
    show girl
    
    q " and am Nyla also a research student,then lets begin our journey.."
    
    show girl2
    
    s "Okay, so we're in a coastal city. We've been hearing reports of pollution in the local river. What should we do?."
    
    show girl

    q " Let's test the water quality. We can check for things like pH, temperature, and dissolved oxygen."
    
    show girl2
    
    m " Good idea! I'll get the water testing kit"
    
    show boy
    
    g " tests the water quality and notes the data."
    
    g "Water quality analysis complete. The river has elevated levels of pollutants, including nitrates and phosphates."
    
    s "(angry): This isn't good. These pollutants can harm aquatic life. What can we do to help?"
    
    q "(Serious): We could try to identify the source of the pollution. Maybe it's coming from a nearby factory or landfill."
    
    show girl2
    
    m " That's a great idea! Let's investigate."
    
    show boy
    
    

    scene bg uni
    with fade

    s "Okay, so we're in a coastal city. We've been hearing reports of pollution in the local river. What should we do?"

    show sylvie green normal
    with dissolve

    m "Good idea! I'll get the water testing kit."

    g "tests the water quality and notes the data."

    g " Water quality analysis complete. The river has elevated levels of pollutants, including nitrates and phosphates."
    
    g "The students investigate the area and find a nearby factory discharging wastewater into the river."
    
    show river
    
    g " Pollution source identified. The factory is discharging untreated wastewater into the river"
    
    s " We need to report this to the local authorities. They can take steps to stop the pollution."
    
    q " Great plan! Let's contact the environmental protection agency."
    
    m " I have informed the local authorities they will take necessary actions."
    
    g "Mission accomplished! You've successfully identified and reported a source of water pollution."
    
    show river2
    
    s "(happy): I'm glad we could help protect the environment."
    
    q " Me too. Let's move on to our next mission."

    menu:

        "Do you want to continue? Yes/No"

        "YES.":

            jump rightaway

        "NO":

            jump later


label rightaway:

    show sylvie green smile

    m " Sounds good! Where are we going next?"
    
    show pic_2

    g " Your next mission is to investigate deforestation in a tropical rainforest. Prepare for your journey!"

    s " What should we focus on in the rainforest?"

    q " We could measure the tree canopy cover and biodiversity."

    q "Or we could investigate the impact of deforestation on local communities."
    
    

    scene bg meadow
    with fade
    
    show pic_3

    "After a short while, we reach the meadows just outside the neighborhood where we both live."

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    m "Hey... Umm..."

    show sylvie green smile
    with dissolve

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    m "Ummm... Will you..."

    m "Will you be my artist for a visual novel?"

    show sylvie green surprised

    "Silence."

    "She looks so shocked that I begin to fear the worst. But then..."

    show sylvie green smile

    menu:

        g "Choose your focus: "

        "Measure tree canopy cover and biodiversity":
            jump game

        "Investigate the impact of deforestation on local communities.":
            jump book


label game:
    
    show pic_4

    m "It's a kind of videogame you can play on your computer or a console."

    m "Visual novels tell a story with pictures and music."

    m "Sometimes, you also get to make choices that affect the outcome of the story."

    s "So it's like those choose-your-adventure books?"

    m "Exactly! I've got lots of different ideas that I think would work."

    m "And I thought maybe you could help me...since I know how you like to draw."

    m "It'd be hard for me to make a visual novel alone."

    show sylvie green normal

    s "Well, sure! I can try. I just hope I don't disappoint you."

    m "You know you could never disappoint me, Sylvie."

    jump marry


label book:

    $ book = True

    m "It's like an interactive book that you can read on a computer or a console."

    show sylvie green surprised

    s "Interactive?"

    m "You can make choices that lead to different events and endings in the story."

    s "So where does the \"visual\" part come in?"

    m "Visual novels have pictures and even music, sound effects, and sometimes voice acting to go along with the text."

    show sylvie green smile

    s "I see! That certainly sounds like fun. I actually used to make webcomics way back when, so I've got lots of story ideas."

    m "That's great! So...would you be interested in working with me as an artist?"

    s "I'd love to!"

    jump marry

label marry:

    scene black
    with dissolve

    "And so, we become a visual novel creating duo."

    scene bg club
    with dissolve

    "Over the years, we make lots of games and have a lot of fun making them."

    if book:

        "Our first game is based on one of Sylvie's ideas, but afterwards I get to come up with stories of my own, too."

    "We take turns coming up with stories and characters and support each other to make some great games!"

    "And one day..."

    show sylvie blue normal
    with dissolve

    s "Hey..."

    m "Yes?"

    show sylvie blue giggle

    s "Will you marry me?"

    m "What? Where did this come from?"

    show sylvie blue surprised

    s "Come on, how long have we been dating?"

    m "A while..."

    show sylvie blue smile

    s "These last few years we've been making visual novels together, spending time together, helping each other..."

    s "I've gotten to know you and care about you better than anyone else. And I think the same goes for you, right?"

    m "Sylvie..."

    show sylvie blue giggle

    s "But I know you're the indecisive type. If I held back, who knows when you'd propose?"

    show sylvie blue normal

    s "So will you marry me?"

    m "Of course I will! I've actually been meaning to propose, honest!"

    s "I know, I know."

    m "I guess... I was too worried about timing. I wanted to ask the right question at the right time."

    show sylvie blue giggle

    s "You worry too much. If only this were a visual novel and I could pick an option to give you more courage!"

    scene black
    with dissolve

    "We get married shortly after that."

    "Our visual novel duo lives on even after we're married...and I try my best to be more decisive."

    "Together, we live happily ever after even now."

    "{b}Good Ending{/b}."

    return

label later:

    "I can't get up the nerve to ask right now. With a gulp, I decide to ask her later."

    scene black
    with dissolve

    "But I'm an indecisive person."

    "I couldn't ask her that day and I end up never being able to ask her."

    "I guess I'll never know the answer to my question now..."

    "{b}Bad Ending{/b}."

    return