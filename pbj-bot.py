
step = 0

greetings = ["hi", "howdy", "hey", "hiya", "ciao", "aloha"]
assent = ["yes", "all right", "very well", "of course", "by all means", "ready", "sure", "certainly", "absolutely", "indeed", "right", "affirmative", "agreed", "roger", "aye aye",  "yeah", "yep", "yup", "ya", "uh-huh", "okay", "OK", "okey-dokey", "okey-doke", "yea", "aye"]
dissent = ["no", "absolutely not",
 "most certainly not",
  "of course not",
  "under no circumstances",
  "by no means",
  "not at all",
  "negative",
  "never",
  "not really",
  "nope",
  "uh-uh",
  "nah",
  "not on your life",
  "no way",
  "no way Jose",
  "ixnay",
  "nay"]

def script(user_input):
    done = False
    global step
    if(step == 0):
        print( """Lets start by gathering our ingeredients.To make the perfect PB&J sandwich you will need:
        -A clean, flat food production surface (I use a clean cutting board)
        -Peanut butter of your choice
        -Jelly, jam, or preserves of your choice
        -2 slices of sandwich bread
        -A clean butter knife
Have you got those?""")
        step += 1
    elif(step == 1 and user_input in assent):
        print """Excellent! Let's double check. Do you have a clean, flat food production surface?"""
        step += 1
    elif(step == 2 and user_input in assent):
        print """Perfect! Do you have a peanut butter?"""
        step += 1
    elif(step == 3 and user_input in assent):
        print """Perfect! Do you have some jelly, jam, or preserves to your liking?"""
        step += 1
    elif(step == 4 and user_input in assent):
        print """Perfect! Do you have two slices of bread staged?"""
        step += 1
    elif(step == 5 and user_input in assent):
        print """And finally, do you have a clean butter knife?"""
        step += 1
    elif(step == 6  and user_input in assent):
        print """Good, let's prepare the Bread.
Position the bread slices on the clean surface side-by-side, with one slice face up and the other face down.
This step is vital because it will allow the slices of bread to evenly match together when combining them in Step 5.
Are you ready for the next step?"""
    elif(step == 7) and user_input in assent:
        print """Let's apply the Peanut Butter
Using the knife, scoop a large dollop of peanut butter and spread it onto the top of each slice of bread.  Use as much peanut butter as desired.
Putting peanut butter on each side will prevent the bread from getting soggy from the jelly- this is especially important if preparing the sandwich ahead of time.
Are you ready for the next step?"""
    elif(step == 8) and user_input in assent:
        print """Let's apply Jelly
Using the same technique as with the peanut butter, scoop out the desired amount of jelly. Spread it on top of the peanut butter of one slice of bread.
Putting jelly on both sides will only lead to a mess, with jelly spewing out the sides of the sandwich.
Are you ready for the next step?"""
    elif(step == 9) and user_input in assent:
        print """Let's combine Both Slices of Bread
Take the slice of bread without jelly on it and flip it on top of the jelly of the other slice.  You should now have a layered PB&J sandwich with peanut butter on the top and bottom and jelly in the center.
Are you ready for the next step?"""
    elif(step == 10 and user_input in assent):
        print """Eat and Repeat
That's it!  Now you can satisfy your hunger with a delicious, non-soggy peanut butter and jelly sandwich. """
        if(raw_input("Enjoy, or would you like to make another?") in assent):
            print """Are you ready for another PBJ?"""
            step = 0
        else:
            done = True
    elif(user_input in dissent):
        print "I'm sorry I'm not equiped to do that right now. Thank you for working with me! I hope I'll see you again"
        done = True
    elif(user_input == ''):
        print """I'm sorry, you're so quiet, I didn't catch that."""
    else:
        print "I'm sorry, I didn't understand what you tried to say. Try rephrasing so that I have a better idea of what you mean, or double check your spelling. I'm still learning contextual comprehension!"
    return done

def main():
    print "Hello! I'm the peanut butter and jelly sandwich instruction chatbot! I'm only really equiped to respond to yes or no at the moment, please bear with me while I seek to improve myself. Are you ready to start making a PB&J?"
    while(1):
        if(script(raw_input())):
            exit(0)

if __name__ == "__main__": main()
