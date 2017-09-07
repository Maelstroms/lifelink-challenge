
step = 0

greetings = ["hi", "howdy", "hey", "hiya", "ciao", "aloha"]
assent = ["all right", "very well", "of course", "by all means", "sure", "certainly", "absolutely", "indeed", "right", "affirmative", "agreed", "roger", "aye aye",  "yeah", "yep", "yup", "ya", "uh-huh", "okay", "OK", "okey-dokey", "okey-doke", "yea", "aye"]

def script(user_input):
    done = False
    if(step == 0):
        print( """Lets start by gathering our ingeredients.To make the perfect PB&J sandwich you will need:
        -A clean, flat food production surface (I use a clean cutting board)
        -Peanut butter of your choice
        -Jelly, jam, or preserves of your choice
        -2 slices of sandwich bread
        -A clean butter knife
Have you got those?""")
        step += 0.1
    elif(step == 0.1 && user_input in assent):
        print """Excellent! Let's double check. Do you have a clean, flat food production surface?"""
        step += .1
    elif(step == 0.2 && user_input in assent):
        print """Perfect! Do you have a peanut butter?"""
        step += .1
    elif(step == 0.3 && user_input in assent):
        print """Perfect! Do you have some jelly, jam, or preserves to your liking?"""
        step += .1
    elif(step == 0.4 && user_input in assent):
        print """Perfect! Do you have two slices of bread staged?"""
        step += .1
    elif(step == 0.5 && user_input in assent):
        print """And finally, do you have a clean butter knife?"""
        step = 1
    elif(step == 1):
        print """Let's prepare the Bread
Position the bread slices on the clean surface side-by-side, with one slice face up and the other face down.
This step is vital because it will allow the slices of bread to evenly match together when combining them in Step 5."""
    elif(step == 2):
        print """Let's apply the Peanut Butter
Using the knife, scoop a large dollop of peanut butter and spread it onto the top of each slice of bread.  Use as much peanut butter as desired.
Putting peanut butter on each side will prevent the bread from getting soggy from the jelly- this is especially important if preparing the sandwich ahead of time."""
    elif(step == 3):
        print """Let's apply Jelly
Using the same technique as with the peanut butter, scoop out the desired amount of jelly. Spread it on top of the peanut butter of one slice of bread.
Putting jelly on both sides will only lead to a mess, with jelly spewing out the sides of the sandwich."""
    elif(step == 4):
        print """Let's combine Both Slices of Bread
Take the slice of bread without jelly on it and flip it on top of the jelly of the other slice.  You should now have a layered PB&J sandwich with peanut butter on the top and bottom and jelly in the center."""
    elif(step == 5):
        print """Eat and Repeat
That's it!  Now you can satisfy your hunger with a delicious, non-soggy peanut butter and jelly sandwich. Enjoy!"""
    elif(step == 6):
        print """Are you ready for another PBJ?"""
        step = 0
    elif(user_input == ''):
        print """I'm sorry, you're so quiet, I didn't catch that."""
    else:
        print "I'm sorry, I didn't understand what you tried to say. Try rephrasing so that I have a better idea of what you mean."
    return done

def main():
    print "Hello! I'm the peanut butter and jelly sandwich instruction chatbot! Are you ready to start making a PB&J?"
    while(1):
        if(script(raw_input())):
            exit(0)

if __name__ == "__main__": main()
