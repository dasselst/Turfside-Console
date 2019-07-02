import random

traitlist = ["speed", "stamina", "breaking", "power", "courage"]


def bool_input(question):
    true_answer = ["yes", "y"]
    return input(question).lower() in true_answer


def ghost_race():
    field = []
    winners = []
    history = []

    def mean_calc(numbers):
        return float(sum(numbers)) / len(numbers)

    name = input("Name: ")
    division = input("Division: ")
    stat = int(input("Total: "))
    is_wallet = bool_input("Is there a Wallet? ")
    is_greyhound = bool_input("Is there a Greyhound? ")
    is_goat = bool_input("Is there a Goat? ")
    negative = int(input("Negative Traits? "))
    bool2 = input("Does consistency string contain any 0s (Y/N)? ")
    if bool2.lower() == "n":
        for n in range(0, 3):
            pl = int(input("Placing? (newest to oldest) "))
            history.append(pl)
        for n in range(1, 3):
            pl = int(input("Static " + str(n) + "? "))
            history.append(pl)
    else:
        history = [0, 0, 0, 0, 0]
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
        tot = random.randint(lo, int((hi * 0.95)))
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
        allowed_winners = 4 if is_greyhound else 9
        field.append([name, stat])

        x = 0
        while x < allowed_winners:
            if division.lower() == "iii":
                field_gen(5, 100)
            elif division.lower() == "ii":
                field_gen(43, 200)
            elif division.lower() == "i":
                field_gen(83, 350)
            elif division.lower() == "silver":
                field_gen(143, 450)
            else:
                field_gen(203, 650)
            x += 1

        for n in range(0, allowed_winners):
            place_finder()
            if winners[n] != "NPC":
                place = n + 1

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

        x = random.randint(0, 100)
        if not is_goat and x <= 10:
            if stat > 740:
                if place != 1:
                    place = place - 1
            length = str(random.randint(1, 7))
            fifty = random.randint(1, 2)
            if fifty == 1:
                print("\n\n" + name + " has placed " + str(place) + "!")
                if place == 1:
                    if is_wallet:
                        print("3,000 coins have been added to your bank!")
                    else:
                        print("2,000 coins have been added to your bank!")
                elif place == 2:
                    if is_wallet:
                        print("1,500 coins have been added to your bank!")
                    else:
                        print("1,000 coins have been added to your bank!")
                elif place == 3:
                    if is_wallet:
                        print("750 coins have been added to your bank!")
                    else:
                        print("500 coins have been added to your bank!")
                else:
                    if is_wallet:
                        print("150 coins have been added to your bank!")
                    else:
                        print("100 coins have been added to your bank!")
                print(name + " has been injured for " + length + " days!")
            else:
                print(
                    "\n\n" + name + " has been injured for " + length + " days! "
                                                                        "Sadly, they were unable to complete the race.")

        else:
            print("\n\n" + name + " has placed " + str(place) + "!")
            if place == 1:
                if is_wallet:
                    print("3,000 coins have been added to your bank!")
                else:
                    print("2,000 coins have been added to your bank!")
            elif place == 2:
                if is_wallet:
                    print("1,500 coins have been added to your bank!")
                else:
                    print("1,000 coins have been added to your bank!")
            elif place == 3:
                if is_wallet:
                    print("750 coins have been added to your bank!")
                else:
                    print("500 coins have been added to your bank!")
            else:
                if is_wallet:
                    print("150 coins have been added to your bank!")
                else:
                    print("100 coins have been added to your bank!")


def breed():
    stats = [0, 0, 0, 0, 0]
    traits = []
    avgs = []
    minimum = []
    final = ["N", "N", "N"]
    par_genes = []
    twins = False

    mirror = bool_input("Mirror? (Y/N) ")
    stork = bool_input("Stork? (Y/N) ")

    if not mirror:
        print(
            "\nPlease ensure that you leave placeholder genes with 'nn' where one parent has a gene and the other "
            "doesn't.")
        length = int(input("\nNumber of Unique Genes: "))
        s_inp = list(input("\nSire's Genes: "))
        d_inp = list(input("Dam's Genes: "))

        for z in range(length):
            par_genes.append(["m", "m", "m", "m"])

        count, n = 0, 0
        while n < len(s_inp):
            if s_inp[n] == " ":
                count += 1
            else:
                if par_genes[count][0] == "m":
                    ch = 0
                else:
                    ch = 1

                if s_inp[n] == "A" and s_inp[n + 1] == "t":
                    par_genes[count][ch] = "At"
                    n += 1
                if s_inp[n] == "C" and s_inp[n + 1] == "r":
                    par_genes[count][ch] = "Cr"
                    n += 1
                if s_inp[n] == "R" and s_inp[n + 1] == "b":
                    par_genes[count][ch] = "Rb"
                    n += 1
                if s_inp[n] == "S" and s_inp[n + 1] == "b":
                    par_genes[count][ch] = "Sb"
                    n += 1
                if s_inp[n] == "S" and s_inp[n + 1] == "t" and s_inp[n + 2] == "y":
                    par_genes[count][ch] = "Sty"
                    n += 2
                if s_inp[n] == "S" and s_inp[n + 1] == "p" and s_inp[n + 2] == "l":
                    par_genes[count][ch] = "Spl"
                    n += 2
                if par_genes[count][ch] == "m":
                    par_genes[count][ch] = s_inp[n]
            n += 1

        count, n = 0, 0
        while n < len(d_inp):
            if d_inp[n] == " ":
                count += 1
            else:
                if par_genes[count][2] == "m":
                    ch = 2
                else:
                    ch = 3

                if d_inp[n] == "A" and d_inp[n + 1] == "t":
                    par_genes[count][ch] = "At"
                    n += 1
                if d_inp[n] == "C" and d_inp[n + 1] == "r":
                    par_genes[count][ch] = "Cr"
                    n += 1
                if d_inp[n] == "R" and d_inp[n + 1] == "b":
                    par_genes[count][ch] = "Rb"
                    n += 1
                if d_inp[n] == "S" and d_inp[n + 1] == "b":
                    par_genes[count][ch] = "Sb"
                    n += 1
                if d_inp[n] == "S" and d_inp[n + 1] == "t" and d_inp[n + 2] == "y":
                    par_genes[count][ch] = "Sty"
                    n += 2
                if d_inp[n] == "S" and d_inp[n + 1] == "p" and d_inp[n + 2] == "l":
                    par_genes[count][ch] = "Spl"
                    n += 2
                if par_genes[count][ch] == "m":
                    par_genes[count][ch] = d_inp[n]
            n += 1

    def genetics():
        genes = []
        very = ["Birdcatcher Spots", "Bend-Or Spots", "Chubari Spots"]
        extremely = ["Chimera", "Brindle", "Reverse Brindle"]
        rare = ""

        r = random.randint(1, 100)
        if r <= 5:
            rare += random.choice(very)
        r = random.randint(1, 100)
        if r <= 3:
            rare += random.choice(extremely)

        for n in range(0, len(par_genes)):
            for x in range(0, 2):
                y = random.randint(1, 2)
                z = random.randint(1, 2)
                if y == 1 and z == 1:
                    one, two = par_genes[n][0], par_genes[n][2]
                elif y == 1 and z == 2:
                    one, two = par_genes[n][0], par_genes[n][3]
                elif y == 2 and z == 1:
                    one, two = par_genes[n][1], par_genes[n][2]
                else:
                    one, two = par_genes[n][1], par_genes[n][3]
            if one == "n" and two == "n":
                genes = genes
            elif one > two or two == "n":
                temp = two, one
                genes.append(temp)
            else:
                temp = one, two
                genes.append(temp)
        return genes, rare

    def data_gather():
        global division
        division = input("Division: ")
        static(division)
        for n in range(0, 3):
            trait = input("Trait: ")
            traits.append(trait)
        average = int(input("Average: "))
        avgs.append(average)

    def static(div):
        if div.lower() == "iii":
            a = 5
            b = 10
        elif div.lower() == "ii":
            a = 4
            b = 8
        elif div.lower() == "i":
            a = 3
            b = 6
        elif div.lower() == "silver" or div.lower() == "s":
            a = 2
            b = 5
        elif div.lower() == "gold" or div.lower() == "g":
            a = 1
            b = 4
        elif div.lower() == "hof":
            a = 1
            b = 3
        else:
            a = 0
            b = 0

        minimum.append(a)
        minimum.append(b)

    t = random.randint(1, 100)
    if stork:
        if t <= 25:
            twins = True
    else:
        if t == 1 or t == 2:
            twins = True

    for n in range(len(stats)):
        stats[n] = random.randint(1, 19)

    stats = [list(stats)]

    if twins:
        stats.append([0, 0, 0, 0, 0])
        for n in range(len(stats[1])):
            stats[1][n] = random.randint(1, 19)
        print("\nSIRE")
        data_gather()
        print("\nDAM")
        data_gather()

    else:
        print("\nSIRE")
        data_gather()
        print("\nDAM")
        data_gather()

    print("\n\n")
    tempo = traits[:]
    if not mirror:
        genes, rare = genetics()
    else:
        genes, rare = [], ""

    for z in range(0, 3):
        g = random.choice(tempo)
        tempo.remove(g)
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

    print("ID#: ")
    print("Phenotype: ")
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
    print("- Courage: ")
    print("Static: \n")

    if rare != "":
        print(genot + "+ " + rare)
    else:
        print(genot)
    print(sex)
    print('Foal')
    print(final)
    print(stats[0][0], stats[0][1], stats[0][2], stats[0][3], stats[0][4])

    if avgs[0] == avgs[1]:
        a = avgs[0]
    elif avgs[0] > avgs[1]:
        a = random.randint(avgs[1], avgs[0])
    else:
        a = random.randint(avgs[0], avgs[1])

    if minimum[0] < minimum[2]:
        mi = minimum[0]
    else:
        mi = minimum[2]
    if minimum[1] > minimum[3]:
        ma = minimum[1]
    else:
        ma = minimum[3]
    b = random.randint(mi, ma)
    print("Statics = " + str(int(a)) + ", " + str(b) + "\n")

    if twins:
        print("Congratulations, you have rolled for twins!\n")
        tempo = traits[:]
        genes, rare = genetics()

        for z in range(0, 3):
            g = random.choice(tempo)
            tempo.remove(g)
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

        if rare != "":
            print(genot + "+ " + rare)
        else:
            print(genot)
        print(sex)
        print('Foal')
        print(final)
        print(stats[1][0], stats[1][1], stats[1][2], stats[1][3], stats[1][4])

        if avgs[0] == avgs[1]:
            a = avgs[0]
        elif avgs[0] > avgs[1]:
            a = random.randint(avgs[1], avgs[0])
        else:
            a = random.randint(avgs[0], avgs[1])

        if minimum[0] < minimum[2]:
            mi = minimum[0]
        else:
            mi = minimum[2]
        if minimum[1] > minimum[3]:
            ma = minimum[1]
        else:
            ma = minimum[3]
        b = random.randint(mi, ma)
        print("Statics = " + str(int(a)) + ", " + str(b) + "\n")

    print("At this time, please decide on a name for your new horse and reply with your choice!")


def train():

    def get_item():
        items = [
            'Lunge Whip',
            'First Aid Kit',
            'Polo Wraps',
            'Bag of Sugarcubes',
            'Mirror',
            'Hourclass',
            'Freezer',
            'Scrambler',
            'Lucky Shoes',
            'Pair of Dice',
            'Milk Carton',
            'Paintbrush',
            'Typewriter'
        ]
        return items[random.randint(0, len(items)-1)]

    trait_list = []
    name = input("Horse name: ")
    is_fox = bool_input("Is there a fox? ")
    is_goat = bool_input("Is there a goat? ")
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
            z = random.randint(1, 5)
            result = "+" + str(z) + " " + trait
            sum_of += z
            training.append(result)
        print("\n" + name + " has gained " + ', '.join(training) + "!")
        x = random.randint(0, 100)
        if is_fox:
            fox_roll = random.randint(1, 5)
            if fox_roll == 1:
                print("\n" + get_item() + "was found during training!")
        if not is_goat and x <= risk:
            days = str(random.randint(1, 7))
            print(name + " has been injured! They will need " + days + " days rest to heal!")


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

    print("\nID#: ")
    print("Phenotype:")
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
        "\nAt this time, please decide on a name for your new horse and reply with your choice! Once you've decided on "
        "a name, you'll be able to start training, racing, etc.\n")
    print(trait_roll)
    print(total, stat_roll)


def mystery_box():
    def get_first_gene():
        genes_list = ['EE', 'Ee', 'ee']
        return genes_list[random.randint(0, len(genes_list)-1)]

    def get_second_gene():
        genes_list = ['AA', 'Aa', 'aa', 'Ata', 'AtAt', 'AAt']
        return genes_list[random.randint(0, len(genes_list)-1)]

    def get_tier_1_genes():
        return_genes = []
        genes_list = [
            ('nSty', 'StySty'),
            ('Ff', 'ff'),
            ('nG', 'GG'),
            'nSpl',
            'nT',
            'nRb',
        ]

        for gene in range(0, random.randint(0, 2)):
            random_gene = random.randint(0, len(genes_list)-1)
            if isinstance(genes_list[random_gene], str):
                return_genes.append(genes_list[random_gene])
            else:
                random_gene_type = random.randint(0, len(genes_list[random_gene])-1)
                return_genes.append(genes_list[random_gene][random_gene_type])
            del genes_list[random_gene]

        return return_genes

    def get_tier_2_genes():
        return_genes = []
        genes_list = [
            ('nSty', 'StySty'),
            ('Ff', 'ff'),
            ('nG', 'GG'),
            ('nSpl', 'SplSpl'),
            ('nT', 'TT'),
            ('nRb', 'RbRb'),
            'nR',
            'nSb',
            'nO',
            'nW',
            'nCr'
        ]

        for gene in range(0, random.randint(1, 4)):
            random_gene = random.randint(0, len(genes_list)-1)
            if isinstance(genes_list[random_gene], str):
                return_genes.append(genes_list[random_gene])
            else:
                random_gene_type = random.randint(0, len(genes_list[random_gene])-1)
                return_genes.append(genes_list[random_gene][random_gene_type])
            del genes_list[random_gene]

        return return_genes

    def get_tier_3_genes():
        return_genes = []
        genes_list = [
            ('nSty', 'StySty'),
            ('Ff', 'ff'),
            ('nG', 'GG'),
            ('nSpl', 'SplSpl'),
            ('nT', 'TT'),
            ('nRb', 'RbRb'),
            ('nR', 'RR'),
            ('nSb', 'SbSb'),
            'nO',
            'nW',
            ('nCr', 'CrCr')
        ]

        for gene in range(0, random.randint(4, 8)):
            random_gene = random.randint(0, len(genes_list)-1)
            if isinstance(genes_list[random_gene], str):
                return_genes.append(genes_list[random_gene])
            else:
                random_gene_type = random.randint(0, len(genes_list[random_gene])-1)
                return_genes.append(genes_list[random_gene][random_gene_type])
            del genes_list[random_gene]

        return return_genes

    def get_additional(tier):
        additional_list = [
            'Birdcatcher Spots',
            'Bend-Or Spots',
            'Chubari Spots',
            'Brindle',
            'Chimera'
        ]
        is_additional = False

        additioanl_roll = random.randint(1, 100)
        if tier == 1 and additioanl_roll == 100:
            is_additional = True
        elif tier == 2 and additioanl_roll > 95:
            is_additional = True
        elif tier == 3 and additioanl_roll > 90:
            is_additional = True

        return additional_list[random.randint(0, len(additional_list)-1)] if is_additional else None

    def get_genes(tier):
        genes = list()
        genes.append(get_first_gene())
        genes.append(get_second_gene())

        if tier == 1:
            genes += get_tier_1_genes()
        elif tier == 2:
            genes += get_tier_2_genes()
        elif tier == 3:
            genes += get_tier_3_genes()

        return genes

    tier = int(input("Which tier? (1, 2, or 3) "))

    sex = random.randint(0, 1)
    if sex:
        sex = "Filly"
    else:
        sex = "Colt"
    random_genes = get_genes(tier)
    additional = None

    additional = get_additional(tier)

    print("\nGenes: " + str(random_genes))
    print("Gender: " + sex)
    if additional:
        print("Additional Roll: " + additional)


def exploration():
    item_list = [
        'Lunge Whip',
        'First Aid Kit',
        'Polo Wraps',
        'Bag of Sugar Cubes',
        'Lucky Shoes'
    ]
    item_generation_roll = random.randint(1, 10)

    if item_generation_roll < 5:
        item_count = random.randint(1, 3)
        item = ('stone' if item_count == 1 else 'stones') if random.randint(0, 1) else 'wood'
        print("\nFound " + str(item_count) + ' ' + item)
    elif item_generation_roll == 5:
        item = item_list[random.randint(0, len(item_list) - 1)]
        print("\nFound " + item)
    else:
        print("\nNothing was found")
        return


print("Welcome to shiips' Turfside generator!\n")
while True:
    print("Would you like to:"
          "\n      1. Ghost Race"
          "\n      2. Breed"
          "\n      3. Train"
          "\n      4. Starter"
          "\n      5. Mystery Box"
          "\n      6. Exploration"
          "\n      7. Quit")
    choice = int(input("\nEnter Choice: "))

    if choice == 1:
        print("\n")
        ghost_race()
        print("\n---------------------------------------------------------------\n\n")
    elif choice == 2:
        print("\n")
        breed()
        print("\n---------------------------------------------------------------\n\n")
    elif choice == 3:
        print("\n")
        train()
        print("\n---------------------------------------------------------------\n\n")
    elif choice == 4:
        print("\n")
        foundation()
        print("\n---------------------------------------------------------------\n\n")
    elif choice == 5:
        print("\n")
        mystery_box()
        print("\n---------------------------------------------------------------\n\n")
    elif choice == 6:
        print("\n")
        exploration()
        print("\n---------------------------------------------------------------\n\n")
    else:
        break
