def compare():
    for player_1 in list_players:
        for player_2 in list_players:
            player_1.Note = 0
            if player_1 != player_2 and player_1.gender.lower() != player_2.gender.lower():
                if player_1.prefone == 1:
                    if abs(player_2.height - player_1.ideal_height) <= 5:
                        player_1.Note += 20
                    else:
                        player_1.Note += 2

                if player_1.prefone != 1:
                    if abs(player_2.height - player_1.ideal_height) <= 5:
                        player_1.Note += 5
                    else:
                        player_1.Note += 0

                if player_1.preftwo == 1:
                    if abs(player_2.height - player_1.ideal_height) <= 5:
                        player_1.Note += 10
                    else:
                        player_1.Note += 1

                if player_1.preftwo != 1:
                    if abs(player_2.height - player_1.ideal_height) <= 5:
                        player_1.Note += 5
                    else:
                        player_1.Note += 0

                if player_1.prefone == 2:
                    if abs(player_2.weight - player_1.ideal_weight) <= 5:
                        player_1.Note += 20
                    else:
                        player_1.Note += 2

                if player_1.prefone != 2:
                    if abs(player_2.weight - player_1.ideal_weight) <= 5:
                        player_1.Note += 5
                    else:
                        player_1.Note += 0

                if player_1.preftwo == 2:
                    if abs(player_2.weight - player_1.ideal_weight) <= 5:
                        player_1.Note += 10
                    else:
                        player_1.Note += 1

                if player_1.preftwo != 2:
                    if abs(player_2.weight - player_1.ideal_weight) <= 5:
                        player_1.Note += 5
                    else:
                        player_1.Note += 0

                if player_1.prefone == 3:
                    if player_1.ideal_skin_color.lower() == player_2.skin_color.lower():
                        player_1.Note += 20
                    else:
                        player_1.Note += 2

                if player_1.prefone != 3:
                    if player_1.ideal_skin_color.lower() == player_2.skin_color.lower():
                        player_1.Note += 5
                    else:
                        player_1.Note += 0

                if player_1.preftwo == 3:
                    if player_2.skin_color.lower() == player_1.ideal_skin_color.lower():
                        player_1.Note += 10
                    else:
                        player_1.Note += 1

                if player_1.preftwo != 3:
                    if player_2.skin_color.lower() == player_1.ideal_skin_color.lower():
                        player_1.Note += 5
                    else:
                        player_1.Note += 0

                list_note.append([player_1.name, player_1.Note, player_2.name])


def calculate():
    for ele1 in list_note:
        for ele2 in list_note:

            if ele1[0] == ele2[2] and ele1[2] == ele2[0]:
                addition = ele1[1] + ele2[1]
                matches.append([ele1[0], addition, ele2[0]])


def match():
    for match1 in matches:
        for match2 in matches:

            if match1 != match2 and match1[0] == match2[0] and match1[1] > match2[1] and match1[0] in list_final and \
                    match1[2] in list_final:
                print(f"{match1[0]}'s match is {match1[2]} ({match1[1]}%)")

                list_final.remove(match1[0])
                list_final.remove(match1[2])

            if match1 != match2 and match1[0] == match2[0] and match1[1] == match2[1] and match1[0] in list_final and \
                    match1[2] in list_final:
                print(f"{match1[0]}'s match is {match1[2]} ({match1[1]}%)")

                list_final.remove(match1[0])
                list_final.remove(match1[2])


class AYTO:
    def __init__(self):
        self.name = input("Hello, what is your name?\n")
        self.gender = input("Are you a male or a female?\n")
        self.height = int(input("What is your height? (cM)\n"))
        self.weight = int(input("What is your weight? (kG)\n"))
        self.skin_color = input(
            "What is your skin color? \nDark\nLight\nWhite\nYellow\n")
        self.ideal_height = int(
            input("Describe your soulmate. What would the ideal height be? (cM)\n"))
        self.ideal_weight = int(
            input("What would the ideal weight be? (kG)\n"))
        self.ideal_skin_color = input(
            "What would the ideal skin color be?\nDark \nLight\nWhite\nYellow\n")
        self.prefone = int(
            input("Choose first pref:\n1 for Height\n2 for Weight\n3 for Skin color\n"))
        self.preftwo = int(
            input("Choose first pref:\n1 for Height\n2 for Weight\n3 for Skin color\n"))
        self.Note = 0


# MAIN
num_players = int(input("How many players?\n"))
list_players = []
list_note = []
list_final = []
matches = []
i = 0

while i < num_players:
    User = AYTO()
    list_players.append(User)
    list_final.append(User.name)
    if num_players - i == 1:
        print("\nAlright. Let's start!!!\n")
    else:
        print("Okay " + User.name + "!\nLet's create another player \n")
    i += 1

print("Participants: ")
for k in list_players:
    print("- ", k.name, "\n")

compare()
calculate()
match()

print("RÉDIGE LA DOCU!!!")
