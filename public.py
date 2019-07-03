import random

traitlist = ["speed", "stamina", "breaking", "power", "courage"]


def bool_input(question):
    true_answer = ["yes", "y"]
    return input(question).lower() in true_answer


def race():
    def input_stats():
        name = input("\nName: ")
        stat = int(input("Total: "))
        negative = int(input("Negative Traits? "))

        stat = negative_adjust(stat, negative)
        field.append([name, stat])

    def negative_adjust(stat, negative):
        for n in range(0, negative):
            stat = stat * 0.95
        stat = int(stat)
        return stat

    def opponent_choice(size, divis):
        for n in range(0, size):
            if divis.lower() == "iii":
                tot = random.randint(5, 100)
            elif divis.lower() == "ii":
                tot = random.randint(43, 200)
            elif divis.lower() == "i":
                tot = random.randint(83, 350)
            elif divis.lower() == "silver":
                tot = random.randint(143, 500)
            else:
                tot = random.randint(203, 750)
            horse = ["NPC", tot]
            field.append(horse)

    field = []

    size = int(input("# of Horses? "))
    chars = int(input("Entrants? "))
    divis = input("Division? ")

    for n in range(0, chars):
        input_stats()
        size -= 1

    opponent_choice(size, divis)

    winners = []
    results = []

    for n in range(0, len(field)):
        if winners[n] == "NPC":
            results.append([n + 1, winners[n]])
        else:
            string = ""
            z = random.randint(0, 5)
            if z == 0:
                nothing = True
            else:
                nothing = False
            while z > 0:
                y = random.randint(0, z)
                t = random.choice(traitlist)
                if y != 0:
                    string += "+" + str(y) + " " + t
                    z -= y
                    if z != 0:
                        string += ", "

            x = random.randint(0, 100)
            if x <= 10:
                length = str(random.randint(1, 3))
                fifty = random.randint(1, 2)
                if fifty == 1:
                    if nothing:
                        results.append([n + 1, winners[n], (length + " days")])
                    else:
                        results.append([n + 1, winners[n], string, (length + " days")])
                else:
                    results.append(["DQ", winners[n], (length + " days")])
            else:
                if nothing:
                    results.append([n + 1, winners[n]])
                else:
                    results.append([n + 1, winners[n], string])

    results.sort()
    print(results)
    print("\n---------------\n")
    for i in range(0, len(results)):
        if results[i][0] != "DQ":
            results[i][0] = i + 1
        print(results[i])


def ghost_race():
    field = []
    winners = []
    history = []

    def mean_calc(numbers):
        return float(sum(numbers)) / len(numbers)

    name = input("Name: ")
    stat = int(input("Total: "))
    negative = int(input("Negative Traits? "))
    for n in range(0, 3):
        pl = int(input("Placing? (newest to oldest) "))
        history.append(pl)
    for n in range(1, 3):
        pl = int(input("Static " + str(n) + "? "))
        history.append(pl)
    how_many = int(input("How many times? "))

    def consistency(cons):
        toggle = random.randint(0, 100)
        if toggle <= cons:
            toggle = True
        else:
            toggle = False
        return toggle

    def negative_adjust(stat, negative):
        for n in range(0, negative):
            stat = stat * 0.95
        stat = int(stat)
        return stat

    def field_gen(lo, hi):
        tot = random.randint(lo, (hi * 0.9))
        field.append(["NPC", tot])

    def place_finder():
        size = calculator()
        choice = random.randint(0, size)
        for n in range(0, len(field)):
            add = field[n]
            if choice <= add[1]:
                winners.append(add[0])
                field.remove(add)
                break
            else:
                choice = choice - add[1]

    def calculator():
        total = 0
        for n in range(0, len(field) - 1):
            add = field[n]
            total += add[1]
        return total

    stat = negative_adjust(stat, negative)

    for y in range(0, how_many):
        boolean = False
        cons = 90
        field = []
        winners = []
        field.append([name, stat])

        x = 0
        while x < 9:
            if stat <= 100:
                field_gen(5, 100)
            elif stat <= 200:
                field_gen(43, 200)
            elif stat <= 350:
                field_gen(83, 350)
            elif stat <= 500:
                field_gen(143, 500)
            else:
                field_gen(203, 750)
            x += 1

        for n in range(0, 10):
            place_finder()
            if winners[n] != "NPC":
                place = n + 1

        op = place
        if mean_calc(history) >= 1:
            boolean = consistency(cons)
        if boolean:
            m = int(round(mean_calc(history), 0))
            bracket = []
            for j in range(1, 5):
                if m == 1:
                    bracket = [1, 1, 1, 1, 1, 1, 2, 2, 3, 3]
                elif m == 2:
                    bracket = [1, 1, 1, 1, 2, 2, 3, 3, 4, 4]
                elif m == 9:
                    bracket = [7, 7, 8, 8, 9, 9, 10, 10, 10, 10]
                elif m == 10:
                    bracket = [8, 8, 9, 9, 10, 10, 10, 10, 10, 10]
                else:
                    bracket = [m - 2, m - 2, m - 1, m - 1, m, m, m + 1, m + 1, m + 2, m + 2]
            place = bracket[place - 1]

        if mean_calc(history) >= 1:
            history.remove(history[2])
            history.insert(0, place)

        string = ""
        z = random.randint(0, 5)
        while z > 0:
            y = random.randint(0, z)
            t = random.choice(traitlist)
            if y != 0:
                string += "+" + str(y) + " " + t
                z -= y
                if z != 0:
                    string += ", "

        x = random.randint(0, 100)
        if x <= 10:
            length = str(random.randint(1, 14))
            fifty = random.randint(1, 2)
            if fifty == 1:
                if z == 0:
                    print("\n\n" + name + " has placed " + str(place) + "!")
                else:
                    print("\n\n" + name + " has placed " + str(place) + " and has gained " + string + "!")
                print("They can race ? more times this week!")
                print(name + " has been injured for " + length + " days!")
            else:
                print(
                    "\n\n" + name + " has been injured for " + length +
                    " days! Sadly, they were unable to complete the race.")

        else:
            if z == 0:
                print("\n\n" + name + " has placed " + str(place) + "!")
            else:
                print("\n\n" + name + " has placed " + str(place) + " and has gained " + string + "!")
            if place == 1:
                print("2,000 coins have been added to your bank!")
            elif place == 2:
                print("1,000 coins have been added to your bank!")
            elif place == 3:
                print("500 coins have been added to your bank!")
            else:
                print("100 coins have been added to your bank!")
            print("They can race ? more times this week!")
        print("Consistency: " + str(boolean) + ", OP: " + str(op))
    print(history)


def breed():
    stats = [0, 0, 0, 0, 0]
    traits = []
    choices = []
    avgs = []
    minimum = [0, 0, 0, 0, 0]
    maximum = [0, 0, 0, 0, 0]
    foal = [0, 0, 0, 0, 0]
    final = ["N", "N", "N"]

    def genetics():
        genes = []
        very = ["Birdcatcher Spots", "Bend-Or Spots", "Chubari Spots"]
        extremely = ["Chimera", "Brindle", "Reverse Brindle"]
        rare = ""

        def find_traits():
            a = input("\nSire A: ")
            b = input("Sire B: ")
            c = input("Dam A: ")
            d = input("Dam B: ")
            return a, b, c, d

        number = int(input("Number of unique traits: "))

        r = random.randint(1, 100)
        if r <= 5:
            rare = random.choice(very)
        r = random.randint(1, 100)
        if r <= 3:
            rare = random.choice(extremely)

        for n in range(0, number):
            a, b, c, d = find_traits()
            for x in range(0, 2):
                y = random.randint(1, 2)
                z = random.randint(1, 2)
                if y == 1 and z == 1:
                    one, two = a, c
                elif y == 1 and z == 2:
                    one, two = a, d
                elif y == 2 and z == 1:
                    one, two = b, c
                else:
                    one, two = b, d
            if one == "n" and two == "n":
                genes = genes
            elif two == "n" or one > two:
                temp = two, one
                genes.append(temp)
            else:
                temp = one, two
                genes.append(temp)
        return genes, rare

    def control():
        print("\nSIRE")
        random_stats()
        print("\nDAM")
        random_stats()
        division_fit()
        return foal

    def data_gather():
        division = input("Division: ")
        for n in range(0, 5):
            stat = int(input("Stat: "))
            stats[n] = stat
        for n in range(0, 3):
            trait = input("Trait: ")
            traits.append(trait)
        average = int(input("Average: "))
        avgs.append(average)
        return division

    def round_up(x):
        x = int(x)
        x += 1
        return x

    def parameters(div, stats):
        for n in range(0, len(stats)):
            if div.lower() == "iii":
                a = 0
                b = 0.15
            elif div.lower() == "ii":
                a = 0.1
                b = 0.3
            elif div.lower() == "i":
                a = 0.2
                b = 0.45
            elif div.lower() == "silver":
                a = 0.3
                b = 0.6
            elif div.lower() == "gold":
                a = 0.4
                b = 0.75
            elif div.lower() == "hof":
                a = 0.5
                b = 0.75

            x = stats[n] * a
            x = round_up(x)
            minimum[n] = x

            y = stats[n] * b
            y = round_up(y)
            maximum[n] = y

    def random_stats():
        parameters(data_gather(), stats)
        for n in range(0, len(minimum)):
            if minimum[n] == maximum[n]:
                z = minimum[n]
            else:
                z = random.randint(minimum[n], maximum[n])
            foal[n] += z

        for n in range(0, len(choices)):
            final[n] = choices[n]

    def over_dist(overflow, n):
        while overflow != 0:
            for x in range(0, 4):
                if foal[x] < n:
                    if n - foal[x] < overflow:
                        y = random.randint(0, n - foal[x])
                    else:
                        y = random.randint(0, overflow)
                    overflow = overflow - y
                    foal[x] = foal[x] + y

    def stat_adjust(n):
        for z in range(0, 4):
            if foal[z] > n:
                overflow = foal[z] - n
                foal[z] = foal[z] - overflow
                over_dist(overflow, n)

    def division_fit():
        cont = sorted(foal)[-3]
        if cont > 76:
            stat_adjust(150)
        elif cont > 51:
            stat_adjust(100)
        elif cont > 31:
            stat_adjust(70)
        elif cont > 21:
            stat_adjust(40)
        else:
            stat_adjust(20)

    genes, rare = genetics()

    control()

    for z in range(0, 3):
        g = random.choice(traits)
        traits.remove(g)
        final[z] = g

    sex = random.randint(1, 2)
    if sex == 1:
        sex = "Filly"
    else:
        sex = "Colt"

    genot = ""
    for j in range(0, len(genes)):
        temporary = genes[j][0] + genes[j][1] + " "
        genot += temporary

    print("\n\nPhenotype: ")
    print("Genotype: ")
    print("Gender: ")
    print("Age: Foal (until mm/dd)")
    print("Traits: ")
    print("Division: ")
    print("Total Stats: ")
    print("- Speed: ")
    print("- Stamina: ")
    print("- Breaking: ")
    print("- Power: ")
    print("- Courage: \n")

    if rare != "":
        print(genot, rare)
    else:
        print(genot)
    print(sex)
    print(final)
    print(sum(foal), foal)

    a = round((sum(avgs) / 2), 0)
    if a % 1 != 0:
        a = round_up(a)
    print("Static", int(a))


def train():
    trait_list = []
    name = input("Horse name: ")
    how_many = int(input("How many times? "))
    number = int(input("How many stats to train? "))
    if number != 5:
        for z in range(0, number):
            trait = input("Enter stat: ")
            trait_list.append(trait)
    risk = 2 * number
    for y in range(0, how_many):
        training = []
        sum_of = 0
        for n in range(0, number):
            if number == 5:
                trait = traitlist[n]
            else:
                trait = trait_list[n]
            z = random.randint(1, 10)
            result = "+" + str(z) + " " + trait
            sum_of += z
            training.append(result)
        print("\n" + name + " has gained " + ', '.join(training) + "!")
        x = random.randint(0, 100)
        if x <= risk:
            days = str(random.randint(1, 14))
            print(name + " has been injured! They will need " + days + " days rest to heal!")
        print(name + " may train ? more times this week.")
        print("\n (" + str(sum_of) + ") \n")


def foundation():
    div = input("Division: ")

    def roll_found(div):
        trait_roll = []
        stat_roll = []

        n = random.randint(0, 3)
        for i in range(1, n):
            trait_roll.append("N")
        while len(trait_roll) < 3:
            trait_roll.append("P")

        if div.lower() == "ii":
            u = 30
            l = 20
        elif div.lower() == "i":
            u = 50
            l = 40
        elif div.lower() == "silver":
            u = 80
            l = 70
        elif div.lower() == "gold":
            u = 110
            l = 100
        else:
            u = 10
            l = 1

        for n in range(0, 5):
            if n == 0 or n == 1:
                x = random.randint(l, u)
            else:
                x = random.randint(1, u)
            stat_roll.append(x)
        total = sum(stat_roll)

        return trait_roll, total, stat_roll

    trait_roll, total, stat_roll = roll_found(div)

    print("\n\nPhenotype:")
    print("Genotype:")
    print("Gender:")
    print("Age:")
    print("Traits:")
    print("Division: ")
    print("Total Stats:")
    print("- Speed:")
    print("- Stamina:")
    print("- Breaking:")
    print("- Power:")
    print("- Courage:")
    print(
        "\nYour horse will be designed and uploaded as soon as possible. At this time, please decide on a name for "
        "your new horse and reply with your choice! Once you've decided on a name, you'll be able to start training, "
        "racing, etc.\n")
    print(trait_roll)
    print(total, stat_roll)


print("Welcome to shiips' Turfside generator!\n")
while True:
    print(
        "Would you like to:"
        "\n      1. Public Race"
        "\n      2. Ghost Race"
        "\n      3. Breed"
        "\n      4. Train"
        "\n      5. Starter"
        "\n      6. Quit")
    choice = int(input("\nEnter Choice: "))

    if choice == 1:
        print("\n")
        race()
        print("\n---------------------------------------------------------------\n\n")
    elif choice == 2:
        print("\n")
        ghost_race()
        print("\n---------------------------------------------------------------\n\n")
    elif choice == 3:
        print("\n")
        breed()
        print("\n---------------------------------------------------------------\n\n")
    elif choice == 4:
        print("\n")
        train()
        print("\n---------------------------------------------------------------\n\n")
    elif choice == 5:
        print("\n")
        foundation()
        print("\n---------------------------------------------------------------\n\n")
    else:
        break
