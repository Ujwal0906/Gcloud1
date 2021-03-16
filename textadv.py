print(
    "==================================================================================================================")
print("Press any key to start the game")
a = input(">>")
print(
    "Type rules if you want to the rules of the game before you start (recommended if this is your first time playing)\n"
    "Type start if you want to start the game (In case you've already read the rules of the game)")
ans = input(">>").lower().strip()
if ans == "rules":
    print(
        "==================================================================================================================")
    print("The Rules:")
    print("1) You will be given many choices to make. Some may lead to the completion of the game and some may not!")
    print("   So pick wisely!")
    print("2) You will receive options to pick from in this format:")
    print("         1) Pick me!")
    print("         2) No pick me!")
    print(
        "You will have to pick either 1 or 2 by typing in the option's number")
    print("3) This game has multiple endings. Try and find them all!")
    print("Hope you have fun! Good luck!")
    pass
elif ans == "start":
    pass
else:
    pass
print(
    "==================================================================================================================")
print("Enter the your name")
name = input(">>").strip()


def start():
    print(
        "==================================================================================================================")
    print(
        name + " is driving down a beaten path with tall menacing trees on either side of the path and you're sure you")
    print("took the wrong left and ended up here. Your car is running on it's last few drops of fuel. It's ")
    print("lurching and sputtering as it struggles to move forward, but suddenly the line of trees clear and you ")
    print("spot a very pristine building with these giant letters on it: HOTEL.")
    print("Do you:")
    print("1) Stop at the hotel to refuel and stay the night.")
    print("2) Keep driving and risk the possibility of getting stuck in the middle of nowhere at night.")
    ans = input(">>").strip()
    if ans == '1':
        hotel()
    if ans == "2":
        drive()
    else:
        print("Invalid input. Please try again")
        start()


def drive():
    print("==================================================================================================================")
    print("You continue to drive in the hopes of finding a place to refuel your car and continue on your journey. Eventually\n"
          "as the night goes on and the light gets darker, your car breaks down. You get out and inspect the engine. Suddenly\n"
          "you feel a hand grasp your shoulder. You turn around in shock to see a man with a long beard and an axe in his hand\n"
          "as well as a lamp in the other. He asks you to stay over at his hut and fix your car the next day.")
    print("Do you: ")
    print("1) Stay at the hut.")
    print("2) Reject his offer and continue to try to fix your car.")
    ans = input(">>").strip()
    if ans == "1":
        hut()
    if ans == "2":
        game_over("You reject his offer and continue to try fixing your car. The mysterious man walks away. You try fixing\n"
                  "the car but you don't really know anything about cars so you decide to continue to walk in search of\n"
                  "something that looks more safe. You keep walking and walking for what seems like an eternity. Until\n"
                  "you see something in the distance; A building with big red letters on it: HOTEL... ")
    else:
        print("Invalid Input. Please try again")
        drive()


def hut():
    print("==================================================================================================================")
    print("You decide to accept his offer and walk towards his house with him. You have to walk to rows and rows of trees\n"
          "to get to his house. You hear so many sounds on the way there. Hoots, growls and something that sounds like\n"
          "screams. Eventually, you reach the house. He gives you a room upstairs and says that you can stay there for\n"
          "the night.He warns you saying that you should not leave the house till he fixes your car as there are scary\n"
          "things in these woods. When you go upstairs, there are two rooms. One that says guest and the other that says\n"
          "DO NOT ENTER. The man must be used to having guests then, you think to yourself. You don't think much of it \n"
          "and go to sleep. The next morning, you wake up and go downstairs for breakfast and on the way you see the axe\n"
          "that the man was carrying yesterday. It was covered it something dark. Mud? No. Something darker... blood?\n"
          "You try not to scream out in fear.")
    print("Do you: ")
    print("1) Confront the man about it.")
    print("2) Leave it and try to figure it out by yourself.")
    ans = input(">>").strip()
    if ans == "1":
        game_over("You decide to confront him about it. Immediately after you bring up the blood on the axe, he runs towards\n"
                  "the axe. He frustratedly screams out, cursing that he forgot to clean his axe. He picks it up and \n"
                  "slashes you down multiple times. ")
    if ans == "2":
        print("You decide on not confronting him. Instead you plan to look around the house for clues as to who he is.\n")
        central_room()
    else:
        print("Invalid Input. Please try again")
        hut()


def central_room():
    print("==================================================================================================================")
    print("Do you: ")
    print("1) Go to the backyard.")
    print("2) Go back upstairs.")
    print("3) Go to the front-yard.")
    ans = input(">>").strip()
    if ans == "1":
        backyard()
    if ans == "2":
        upstairs()
    if ans == "3":
        front_yard(weapon="")
    else:
        print("Invalid Input. Please try again")
        central_room()


def backyard():
    print("==================================================================================================================")
    print("You decide to go to the backyard. You look around and see a bunch of normal things in the backyard. Nice grass,\n"
          "large fence, a small table, a couple of chairs and a really large and odd tool shed.")
    print("Do you: ")
    print("1) Inspect the tool shed.")
    print("2) Go back to the central room.")
    ans = input(">>").strip()
    if ans == "1":
        tool_shed()
        print("Tool-Shed here.")
    if ans == "2":
        central_room()
    else:
        print("Invalid Input. Please try again")
        backyard()


def tool_shed():
    print("==================================================================================================================")
    print("You go to the tool shed and creak open the door. The smell of stale-air gushes out. You look around and find\n"
          "normal stuff, gardening tools, buckets, fertilizer and a trap-door... wait, a trapdoor?")
    print("Do you: ")
    print("1) Go back to the central-room.")
    print("2) Go down the trap door.")
    ans = input(">>").strip()
    if ans == "1":
        central_room()
    if ans == "2":
        trap_door()
        print("Trap door here.")
    else:
        print("Invalid Input. Please try again")
        tool_shed()


def trap_door():
    print("==================================================================================================================")
    print("You push open the trap door and jump in. It's a completely dark room except for one spotlight in the middle \n"
          "of the room. You walk over to it and see a large red button.")
    print("Do you: ")
    print("1) Push the button.")
    print("2) Go back to the central room.")
    ans = input(">>").strip()
    if ans == "1":
        button()
    if ans == "2":
        central_room()
    else:
        print("Invalid Input. Please try again")
        trap_door()


def button():
    print("==================================================================================================================")
    print("You push the button a screen comes down from the ceiling. It's the hotel! The one you passed by at the start.\n"
          "Then you hear the following words in a robotic voice: You have 10 seconds to abort demolition.")
    print("Do you: ")
    print("1) Let the 10 seconds run out.")
    print("2) Abort the demolition.")
    ans = input(">>").strip()
    if ans == "1":
        print("You let the timer run out and watch the hotel blow up. On the screen you can see a man running towards\n"
              "the hotel. It's the bearded man! Now's your chance to escape. You run out of the shed. Jump the fence and\n"
              "run as fast as you can. You find a tar road and a sign that says Bangalore ahead.")
        print(
            "==================================================================================================================")
        print(
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CONGRATULATIONS YOU WIN!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        play_again()
    if ans == "2":
        game_over("The voice says that it's deactivated. It then says relaying message to owner. You start to panic.\n"
                  "In a few seconds you hear large footsteps coming towards you. You try to get out of the shed to run\n"
                  "for you life but it's too late. He's here and you're dead. ")
    else:
        print("Invalid Input. Please try again")
        button()


def upstairs():
    print("==================================================================================================================")
    print("You decide to go upstairs. You seem your guest room as well as the Do Not Enter room. Maybe there are clues\n"
          "the Do Not Enter room?")
    print("Do you: ")
    print("1) Go into the room.")
    print("2) Go back to the central room.")
    ans = input(">>").strip()
    if ans == "1":
        dne_room()
        print("dne_room here.")
    if ans == "2":
        central_room()
    else:
        print("Invalid Input. Please try again")
        upstairs()


def dne_room():
    print("==================================================================================================================")
    print("You decide to open the door to the room. It's a clean room with a bunch of paperwork organised well in a cabinet..\n"
          "You walk up to a desk with drawers in it. On further inspection you find a folder that says previous prisoners.\n"
          "You open the file and to your horror you find out everything. The file you're reading contains notes written by\n"
          "previous prisoners about the owner. It turns out he's an employee of the hotel. They hired him to catch people\n"
          "who don't stay at the hotel, imprison them while giving them a false sense of security and then killing them.\n"
          "It also says that his only weakness is his own axe. There is also a button in the backyard that will save you.\n"
          "with this new information, you decide to head back to the central room. You find his axe lying there.")
    print("Do you: ")
    print("1) Take his heavy axe and slow yourself down.")
    print("2) Leave it and press on.")
    ans = input(">>").strip()
    if ans == "1":
        weapon = "axe"
        print("==================================================================================================================")
        print("Do you:")
        print("1) Go to the front yard.")
        print("2) Go the backyard.")
        ans = input(">>").strip()
        if ans == "1":
            front_yard(weapon)
            print("front yard here.")
        if ans == "2":
            backyard()
    if ans == "2":
        weapon = "None"
        print("==================================================================================================================")
        print("Do you:")
        print("1) Go to the front yard.")
        print("2) Go the backyard.")
        ans = input(">>").strip()
        if ans == "1":
            front_yard(weapon)
            print("front yard here.")
        if ans == "2":
            backyard()
    else:
        print("Invalid Input. Please try again")
        dne_room()


def front_yard(weapon):
    print("==================================================================================================================")
    print("You walk out the front door and into the front yard. The man sees you and runs towards you screaming at you\n"
          "saying that he told you not leave the house.")
    if weapon == "axe":
        print("As he gets closer, you grip the axe tighter. You swing the axe at him as hard as you can. It connects!\n"
              "you run as fast as you can. As you're running further and further away, you see a sign that says,\n"
              "Bangalore ahead!")
        print(
            "==================================================================================================================")
        print(
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CONGRATULATIONS YOU WIN!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        play_again()
    else:
        game_over("You stand there shocked with nothing to fight him with. He grabs you by your neck and suffocates you\n"
                  "to your death. ")





def game_over(reason):
    print("==================================================================================================================")
    print("\n" + reason + "Game over!")
    play_again()


def play_again():
    print(
        "==================================================================================================================")
    print("Would you like to play again? (Yes or No)")
    ans = input(">>").lower().strip()
    if ans == "yes":
        start()
    elif ans == "no":
        print("Thank you for playing!")
        exit()
    else:
        print("Invalid input. Play again.")
        play_again()


def hotel():
    print(
        "==================================================================================================================")
    print("You enter the hotel and you walk over to the receptionist's counter. She seems like a very sweet old lady.")
    print(
        "You tell her that you want a room for the night and she gives you a key and asks you if you want entertainment")
    print("(provided for free) along with your dinner.")
    print("Do you: ")
    print("1) Say Yes")
    print("2) Say No")
    ans = input(">>").strip()
    if ans == "1":
        game_over(
            "You accept the entertainment and head to your room. Just before you can start settling down into your\n "
            "room, you hear a knock on the door saying that your dinner is ready. You open it and the receptionist\n "
            "hands you your dinner. She says that the entertainment will start now as well. She bolts towards\n"
            "you with a knife in her hand and an unnatural smile on her face. She holds you still and stabs you over and over.")

    elif ans == "2":
        books()
    else:
        print("Invalid input. Please try again.")
        hotel()


def books():
    print(
        "==================================================================================================================")
    print("You politely decline the offer and go to your room. You watch the staff members bring your luggage up\n"
          "You settle into your room and decide to look at what the room has to offer. You check out the view and it's\n"
          "actually very pretty! A beautiful view over the pool that's reflecting the moonlight off of it's surface.\n"
          "You turn the lights on in the bathroom and it starts flickering every few seconds. You hear a muffled scream\n"
          "on the other side of your room's wall. Probably kids having fun or something... right? You decide to explore\n"
          "more to take your mind off of whatever just happened and you find a bookshelf! There are 3 books.")
    print("Do you: ")
    print("1) Pick the book about antidotes.")
    print("2) Pick the book about rare animals.")
    print("3) Pick the book about greek mythology.")
    ans = input(">>").strip()
    if ans == "1":
        print(
            "You pick up the book and start to read it. You learn a lot about antidotes and are surprised about how \n"
            "easy it is to make them. Suddenly the lights in your room start to flicker and eventually go out.")
        book = "antidote"
        reception(book)
    elif ans == "2":
        print("You pick up the book and start to read it. You learn a lot about so many animals you've never heard of\n"
              "before. You learn about their likes and dislikes and even how to tame a few! Suddenly the lights in your\n"
              "room start to flicker and eventually go out.")
        book = "animals"
        reception(book)
    elif ans == "3":
        print(
            "You pick up the book and start to read it. You learn a lot about the greek gods and their weird and cool\n"
            "stories.You learn about what each god governs over.Suddenly the lights in your room start to flicker and\n"
            " eventually go out.")
        book = "greek"
        reception(book)
    else:
        print("Invalid input. Please try again.")
        books()


def reception(book):
    print(
        "==================================================================================================================")
    print("You decide to look for the receptionist, and so you go down to the reception. You open your room door and \n"
          "it's so dark that you can't even see your own feet. You're barely able to see things in-front of you. Your\n"
          "only saving grace is the eerie moonlight shining through the tiny windows. When you reach the reception, you\n"
          "realise the receptionist isn't here. You see a pool on your left and a long hallway to your right. She might\n"
          "be at the pool or perhaps down the hall?, you think to yourself.")
    print("Do you: ")
    print("1) Go to the pool.")
    print("2) Go down the hallway.")
    ans = input(">>").strip()
    if ans == "1":
        pool(book)
        print("1")
    elif ans == "2":
        hallways(book)
        print("2")
    else:
        print("Invalid input. Please try again.")
        reception(book)


def pool(book):
    print(
        "==================================================================================================================")
    print(
        "You decide to go to the pool. Something looks very fishy about the water there, so you decide to get closer to\n"
        "investigate the water. It seems to be glowing and giving off a rancid smell. Just as you move back due to the\n"
        "smell of the pool, you feel to bony hands on your back. You turn around and see the receptionist. Wearing\n"
        "that horrifying smile, she pushes you into the pool. You fall into the pool and sink to the bottom, as you're\n"
        "too shocked to even try to swim out. Suddenly, you feel your legs burning, then your chest, then your arms\n"
        "and even your face.")
    if book == "antidote":
        print(
            "Luckily you remembered about this smell from reading that book in your room! You quickly jump out of the\n"
            "pool and rush back to your room to make the antidote. You hastily prepare it but it worked as you feel\n"
            "the burning sensation slowly fade away.")
        basement()
    else:
        game_over("You quickly swim to the surface but it's too late. You slowly feel the burning sensation seep deeper \n"
                  "and deeper into your body until you lose consciousness. ")


def hallways(book):
    print(
        "==================================================================================================================")
    print(
        "You decide to walk down the long and dark hallway. You continue walking in a straight line for what seems like\n"
        "an eternity. Eventually in all the darkness, you're able to see something ahead of you. A wall. A plain white\n"
        "wall. You reach the wall and end up having to turn right to continue. As you turn right to move into the next\n"
        "hallway, you feel the ground rumble and hear a loud sound behind. There's dust flying everywhere. After a\n"
        "good minute of coughing and clearing your eyes you look behind you to investigate the noise. To your surprise,\n"
        "there's a wall behind you, with the words YOU CAN NEVER GO BACK, written on it in blood. You decide to press\n"
        "on. Eventually you make your way to a giant room. There seems to be something that looks like mountain blocking\n"
        "your path. You get closer to investigate it. You find out that it's a three headed dog. It wakes up with it's\n"
        "eyes trained on you.\n")
    if book == "greek":
        print(
            "You suddenly remember that you've read about this creature in that greek book! They fall asleep if you shout the\n"
            "ancient word -Kalinikta- You scream it at the giant dog bounds toward you. It instantly falls asleep.\n"
            "You run past it and through the door behind it.")
        basement()
    else:
        game_over(
            "The dog gets on it's feet and bounds toward you. You stand still shocked. You make your final prayers\n"
            "and close your eyes. Forever.")


def basement():
    print(
        "==================================================================================================================")
    print("You hear something calling you so you slowly make your way to the source of the sound (the basement). You \n"
          "find that it's a broken record playing your name over and over. " + name + "... " + name + "... You stop \n"
          "the record from spinning. You see a book with your name on it. You pick it and open it. It's pictures of \n"
          "the staff members along with the date that they died. You start to panic and rush out of the basement and\n"
          "towards the main door. Just as you leave the room, you hear metal scraping against the ground and loud \n"
          "footsteps right after. You start to run faster. You notice the pattern of the footsteps is uneven.")

    print(
        "You finally end up at the door of the hotel. You try opening the door, but it doesn't budge. You find a 4 digit")
    print("combination lock on it with each digit ranging from 1 to 4. There is a note on the door which says:")
    print(r'                                "The answEr you seek"                                            ')
    print(r'                                "Lies before yoUr eyes"                                          ')
    print(r'                                "Think carefully noW, for"                                       ')
    print(r'                                "You have three trieS..."')
    print("Do you: ")
    print("1) Jump out the window and run for your life.")
    print("2) Try to solve the 4 digit combination.")
    ans = input(">>").strip()
    if ans == "1":
        game_over("You jump out the window and land on your foot awkwardly and end up breaking it. You try your best to\n"
                  "crawl from there but the bony fingers are back and they grab your legs and pull you into eternal\n"
                  "darkness. ")
    elif ans == "2":
        for i in range(0, 3):
            print("Please enter the 4 digit combination.")
            ans = input(">>").strip()
            if ans == "2334":
                print("The lock clicks open. You swing open the door with incredible speed and run for your life. You\n"
                      "hear the old lady speak some harsh sounding words in what sounds like a foreign language. You make\n"
                      "a promise to yourself that you'll never stay at a hotel ever again.")
                print(
                    "==================================================================================================================")
                print(
                    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CONGRATULATIONS YOU WIN!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                play_again()
                break
        game_over("You run out of turns. The monster has made it's way to you. You've run out of time. You close eyes,\n"
                  "knowing that you're never going to see the light of day again. ")
    else:
        print("Invalid option. Please pick again")
        basement()


start()