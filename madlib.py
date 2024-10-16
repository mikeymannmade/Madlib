import random

START = 1
ADD_WORD = 2
STOP = 3

def main():

    adjectives = []
    nouns = []
    verbs = []
    names = []
    places = []
    silly_items = []
    num = 3

    print("\n\nWelcome to mikeys madlibs!\n\n")

    while num > 0:
        adjectives.append(input(f"\nEnter an adjective ({num} remaining): \n:::"))
        nouns.append(input(f"\nEnter a noun ({num} remaining): \n:::"))
        verbs.append(input(f"\nEnter a verb ({num} remaining): \n:::"))
        names.append(input(f"\nEnter an name ({num} remaining): \n:::"))
        places.append(input(f"\nEnter an place ({num} remaining): \n:::"))
        silly_items.append(input(f"\nEnter a silly item ({num} remaining): \n:::"))
        num -= 1

    random.shuffle(adjectives)
    random.shuffle(nouns)
    random.shuffle(verbs)
    random.shuffle(names)
    random.shuffle(places)
    random.shuffle(silly_items)
    stories = [
                f"\nOne day, {names[0]} was feeling very {adjectives[0]}. They decided to head\n"
                f"to the {places[0]}, where they accidentally {verbs[0]} over a {nouns[0]}.\n"
                f"To their surprise, a {silly_items[0]} appeared out of nowhere!\n\n"
                f"Meanwhile, {names[1]} was at the {places[1]}, dealing with a {adjectives[1]}\n"
                f"situation. They had just {verbs[1]} when they saw a {nouns[1]} rolling\n"
                f"towards them, followed by a {silly_items[1]}. It was a strange sight!\n\n"
                f"Finally, {names[2]} found themselves in the {places[2]}, feeling\n"
                f"particularly {adjectives[2]}. While they {verbs[2]} around, they came across\n"
                f"a {nouns[2]} sitting next to a {silly_items[2]}. Who would have guessed\n"
                f"the day would turn out so bizarre!\n\n\n\n\n",
                
                f"\nAt the {places[0]}, {names[1]} was {verbs[1]} around when suddenly, a {nouns[0]}\n"
                f"flew out of nowhere! It was all too {adjectives[1]}, and before they\n"
                f"knew it, {silly_items[0]} filled the room.\n\n"
                f"Not too far away, {names[0]} was trying to fix their {nouns[2]} when the\n"
                f"entire {places[2]} started shaking. It wasn't just a typical day anymore.\n"
                f"{names[2]} would have laughed if it weren't so {adjectives[0]}.\n\n\n\n\n",
                
                f"\nEarly in the morning, {names[2]} found themselves at the {places[2]},\n"
                f"working on a project that required a lot of {adjectives[1]} focus.\n"
                f"Suddenly, {names[1]} ran by holding a {nouns[0]}, yelling about a {silly_items[1]}.\n"
                f"It was the last thing anyone expected to see before {verbs[2]}.\n\n"
                f"Later that day, things only got stranger as {names[0]} came sprinting\n"
                f"into the {places[1]}, holding onto a {nouns[1]}, shouting about how they\n"
                f"needed help before things got too {adjectives[2]}.\n\n\n\n\n",
                
                f"\nThe adventure began when {names[0]} tripped over a {nouns[1]} at the {places[0]}.\n"
                f"This led them straight into a bizarre encounter with a {silly_items[2]}.\n"
                f"{names[1]} was nearby, watching from a distance, wondering how {names[0]}\n"
                f"was managing to stay so {adjectives[2]} through it all. Things became\n"
                f"even more {adjectives[1]} when {verbs[0]} happened unexpectedly.\n\n\n\n\n",
                
                f"\nIt was a regular day in the {places[1]} when {names[2]} stumbled across a\n"
                f"hidden room filled with {nouns[0]} and a giant {silly_items[0]}.\n"
                f"They called {names[1]}, who hurried over, {verbs[2]} in excitement. Together,\n"
                f"they tried to figure out what this {adjectives[0]} discovery meant,\n"
                f"but {names[0]} just shrugged and went back to the {places[2]} to deal\n"
                f"with their {nouns[2]}, which had been causing {adjectives[2]} problems all day.\n\n\n\n\n"
                ]
    random_story = random.choice(stories)


    print("Generating Story...")
    print("\nStory Finished.\n")
    input("Press ENTER to read story: ")
    print(random_story)

main()