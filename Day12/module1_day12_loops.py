"""
    Author:         Daniel-TheProgrammer
    Description:    Learn about loops in python.
"""

# The for loop is used for iterating over a sequence. If want to repeat a task 10 times, you can use a for loop to
# quickly and easily automate the job. Similar to if/then statements, for loops also use a colon (:) for the end of the
# declaration line. Additionally, the action is indented from the declaration line. As the action is completed, the
# iterator is automatically updated by one and the loop ends when the iterator is greater than the terminating value.
for i in range(1, 11):
    print("i equals {}".format(i))

# The step value of the range can also be used in conjunction with a for loop.
for i in range(1, 110, 10):
    print("i equals {}".format(i))

# A for loop can also be used with strings.
bridge = "Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see."
for letter in bridge:
    print("{}".format(letter))

# A for loop can be used in conjunction with an if statement to complete an action based on the iterator.
bridge = "Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see."
x = 0
for letter in bridge:
    if letter in 'aeiou':
        x += 1
print("There are {} vowels in the quote.".format(x))

# A for loop can also be used to loop through a list.
questions = ["What is your name?", "What is your quest?", "What is the airspeed velocity of an unladen swallow?"]
for question in questions:
    print(question)
    print(input())

# Loops can also be nested for additional functionality.
print("=" * 26)
for i in range(1, 13):
    for j in range(1, 13):
        print("| {:2} times {:2} equals {:3} |".format(i, j, i * j))
    print("=" * 26)

# Unlike a for loop, a while loop will continue to execute while the condition is True. Just like for loops and
# conditional statements, a while loop also use a colon (:) for the end of the declaration line. Additionally, the
# action is indented from the declaration line. However, while loops do not iterate automatically, so an action must be
# completed in order to avoid an infinite loop.
i = 0
while i < 10:
    print(i)
    i += 1

# A while loop can be used in conjunction with user defined input to create a simple text adventure game.
print("You're on a holy quest to seek the Holy Grail. Where do you look?")
choice = ""
while choice != 'quit':
    print("Select an option within quotes")
    choice = input("You can choose to go into the 'forest', head back to 'camelot', go make some 'rabbit' stew, try to "
                   "recruit the 'french' to join your quest, or celebrate at a 'wedding'. If you get tired, you can "
                   "just 'quit' and go home.")
    if choice.lower() == "forest":
        print("As you traverse this dense forest, you are stopped by the Knights of Ni. You appease the Knights of Ni "
              "by spending your money on shrubberies courtesy of Roger the Shrubber. At least you didn't need to chop "
              "down the largest tree in the forest with a herring.")
        print("")
    elif choice.lower() == "camelot":
        print("You've done it. You've reached Camelot. This great castle (while it's only a model), is the most "
              "well-respected court in the land. You think you hear the faint sound of singing coming from the castle. "
              "As you begin to ride to the castle, King Arthur tells the group, 'Well, on second thought, let's not go "
              "to Camelot. It is a silly place.' Your party agrees, and you ride off.")
        print("")
    elif choice.lower() == "rabbit":
        print("You reach the cave of Caerbannog ready to face the beast. Not frightened by the sight of the rabbit, "
              "Bors goes to make some rabbit stew. Unfortunately, the rabbit has great, big, pointy teeth, and he "
              "kills Bors. You charge in response, but the rabbit makes quick work of your party and you also lose "
              "Gawain and Ector. Luckily, Brother Maynard is there with the Holy Hand Grenade of Antioch. Thanks to "
              "the instructions in the Book of Armaments, you count to five...three sir...three and blow the rabbit to "
              "tiny bits.")
        print("")
    elif choice.lower() == "french":
        print("You come to a castle in search of knights to join you on your quest for the Holy Grail. Unfortunately, "
              "there is an incredibly rude French guard who continues to taunt you. All the sudden, the castle is "
              "catapulting cattle onto your party. You devise an ingenious plan to build a large, wooden badger to "
              "sneak into the castle. However, you forget to hide in the badger and the Frenchmen catapult it back "
              "anyway. You leave dejected and defeated.")
        print("")
    elif choice.lower() == "wedding":
        print("Your trusty companion was struck by an arrow carrying a note of a person in distress. Even though your "
              "companion is getting much better, you run off to save the day. The source of the note came from a "
              "castle in the distance. As you burst through the gates and fight your way through the guards and "
              "bystanders, you come to find out the source of the note was not what you expected. You just ruined a "
              "wedding. But don't fret, you apologize, and the surviving guests break out in song.")
        print("")
    elif choice.lower() == "quit":
        print("You have failed in your quest to find the Holy Grail. Try again next time.")
        print("")
    else:
        print("That was not an acceptable entry. Try again.")
        print("")
