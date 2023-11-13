
# Initialize
current_items = []
spat_rels, wall, flooring, lighting, windows, spacious, doors, item = "", "", "", "", "", "", "", ""


# Welcome
def welcome():
    print("--------------------------------------------------------------------------------")
    print("\033[1mWelcome to the user input example!\033[0m")
    print("You will be shown a room and asked to describe it.")
    print("You will be asked to describe:")
    print("\t1. The items you see in the room")
    print("\t2. The spatial relationships between the items")
    print("\t3. The type and color of the walls")
    print("\t4. The type and color of the flooring")
    print("\t5. The lighting in the room")
    print("\t6. The number of windows in the room")
    print("\t7. How spacious the room is")
    print("\t8. The number of doors in the room")
    print("\t9. A specific item in the room")
    print("--------------------------------------------------------------------------------")
# ---- Get user input
def question1(current_items):
    print("\033[1mQuestion 1\033[0m")
    print("Can you type the items you saw in the room, and press enter after each item?")
    while True:
        print("\tCurrent items: " + str(current_items))
        new_item = input("\tType an item or press q if you are done: ")
        # Quit?
        if new_item.lower() == "q":
            break
        elif new_item.lower() not in current_items:
            # Add item
            current_items.append(new_item.lower())
        print("")
    return current_items

def question2(spat_rels):
    print("--------------------------------------------------------------------------------")
    print("\033[1mQuestion 2\033[0m")
    print("The items you just provided are: " + str(current_items))
    print("\tCan you describe the spatial relationships between the items?")
    print("\tFor example: 'the chair is next to the table' or 'the table is in front of the chair':")
    spat_rels += " " + input("\t\t")
    return spat_rels

# Question 3
def question3(wall):
    print("--------------------------------------------------------------------------------")
    print("\033[1mQuestion 3\033[0m")
    print("Can you name the type and color of the walls?: ")
    wall += " " + input("\t")
    return wall

# Question 4
def question4(flooring):
    print("--------------------------------------------------------------------------------")
    print("\033[1mQuestion 4\033[0m")
    print("What kind of flooring does the room have (type and color)?: ")
    flooring += " " + input("\t")
    return flooring

def question5(lighting):
    print("--------------------------------------------------------------------------------")
    print("\033[1mQuestion 5\033[0m")
    print("Can you describe the lighting in the room?: ")
    lighting += " " + input("\t")
    return lighting

def question6(windows):
    print("--------------------------------------------------------------------------------")
    print("\033[1mQuestion 6\033[0m")
    print("How many windows does the room have?: ")
    windows += " " + input("\t")
    return windows

def question7(spacious):
    print("--------------------------------------------------------------------------------")
    print("\033[1mQuestion 7\033[0m")
    print("How spacious is the room?: ")
    spacious += " " + input("\t")
    return spacious

def question8(doors):
    print("--------------------------------------------------------------------------------")
    print("\033[1mQuestion 8\033[0m")
    print("How many doors does the room have?: ")
    doors += " " + input("\t")
    return doors

def question9(item):
    print("--------------------------------------------------------------------------------")
    print("\033[1mQuestion 9\033[0m")
    print("Can you describe the item (what, color, shape)?: ")
    item += " " + input("\t")
    return item

def repeat_question():
    while True:
        print("--------------------------------------------------------------------------------")
        print("\033[1mPrint would you like to add to a question? Type the question number (1-9) or q to quit.\033[0m")
        question = input("\t")
        if question == "q":
            break
        elif question in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            qnumber = int(question)
            if qnumber == 1:
                print("--------------------------------------------------------------------------------")
                print("What you have already typed for question 1: " + str(current_items))
                current_items = question1(current_items)
            elif qnumber == 2:
                print("What you have already typed for question 2: " + str(spat_rels))
                spat_rels = question2(spat_rels)
            elif qnumber == 3:
                print("What you have already typed for question 3: " + str(wall))
                wall = question3(wall)
            elif qnumber == 4:
                print("What you have already typed for question 4: " + str(flooring))
                flooring = question4(flooring)
            elif qnumber == 5:
                print("What you have already typed for question 5: " + str(lighting))
                lighting = question5(lighting)
            elif qnumber == 6:
                print("What you have already typed for question 6: " + str(windows))
                windows = question6(windows)
            elif qnumber == 7:
                print("What you have already typed for question 7: " + str(spacious))
                spacious = question7(spacious)
            elif qnumber == 8:
                print("What you have already typed for question 8: " + str(doors))
                doors = question8(doors)
            elif qnumber == 9:
                print("What you have already typed for question 9: " + str(item))
                item = question9(item)
    return current_items, spat_rels, wall, flooring, lighting, windows, spacious, doors, item


# Welcome
welcome()
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("HERE SHOULD BE A PICTURE OF A ROOM/THE ASSIGNMENT KIND OF THING. STILL VAGUE HOW THIS IS PERFORMED DURING THE EXPERIMENT. --> ASK TEACHERS")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# Ask questions
current_items = question1(current_items)
spat_rels = question2(spat_rels)
wall = question3(wall)
flooring = question4(flooring)
lighting = question5(lighting)
windows = question6(windows)
spacious = question7(spacious)
doors = question8(doors)
item = question9(item)
# Repeat questions
current_items, spat_rels, wall, flooring, lighting, windows, spacious, doors, item = repeat_question()






