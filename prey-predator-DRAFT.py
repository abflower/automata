import matplotlib.pyplot as plt
import random


class fish1():
    def __init__(self, age):
        self.eat = 3
        self.lifespan = 14
        self.age = age

class fish2():
    def __init__(self, age):
        self.eat = 1
        self.lifespan = 16
        self.age = age

f1_fishery = []
f1_hatching = [0,0]
f1_birth_2 = 0
f1_birth_1 = 0
f1_born = 0
f1_born_record = 0
food = 200

f2_fishery = []
f2_hatching = [0,0,0]
f2_birth_3 = 0
f2_birth_2 = 0
f2_birth_1 = 0
f2_born = 0
f2_born_record = 0


fish1_data = []
fish2_data = []
food_data = []
iteration = []

def populate(num):
    count = 0
    while count<num:
        new_age = random.randint(0,14)
        f1_fishery.append(fish1(age=new_age))
        count += 1

def populate_f2(num):
    count = 0
    while count<num:
        new_age = random.randint(0,16)
        f2_fishery.append(fish2(age=new_age))
        count += 1

def reproduce(num):
    cycle = len(f1_hatching)
    count = 0
    global f1_born_record
    f1_born_record = f1_hatching[0]
    print('Born fish: %s' % f1_born_record)
    while count < f1_hatching[0]:
        f1_fishery.append(fish1(0))
        count += 1
    count = 1
    while count < cycle:
        f1_hatching[count-1] = f1_hatching[count]
        count += 1
    if count == cycle:
        f1_hatching[cycle-1] = 4*int(num/2)



def reproduce_f2(num):
    cycle = len(f2_hatching)
    count = 0
    global f2_born_record
    f2_born_record = f2_hatching[0]
    print('Born fish: %s' % f2_born_record)
    while count < f2_hatching[0]:
        f2_fishery.append(fish2(0))
        count += 1
    count = 1
    while count < cycle:
        f2_hatching[count-1] = f2_hatching[count]
        count += 1
    if count == cycle:
        f2_hatching[cycle-1] = int(num/2)


def iterate(num):
    count = 1
    while count <= num:

        print('- - - - Iteration: %s - - - - \nFish: %s' % (count, len(f1_fishery)))
        count += 1
        f1_mature_fish = 0
        f1_dead_fish = 0

        f2_mature_fish = 0
        f2_dead_fish = 0
        global food

        # checks on age and food availability

        for fish in f1_fishery:
            if fish.age >= 1 < fish.lifespan:
                f1_mature_fish += 1
            fish.age += 1
            if fish.age >= fish.lifespan:
                f1_fishery.remove(fish)
                f1_dead_fish += 1
            else:
                if (food - 2*fish.eat) <= 0:
                    #f1_fishery.remove(fish)
                    f1_fishery.pop(random.randint(0, len(f1_fishery) - 1))
                    f1_dead_fish += 1
                else:
                    food -= fish.eat
        print('Mature fish: %s' % (f1_mature_fish))

        reproduce(f1_mature_fish)
        print('Dead fish: %s' % (f1_dead_fish))
        print('Food left: %s' % (food))
        print()



        print('Fish: %s' % (len(f2_fishery)))

        f2_mature_fish = 0
        f2_dead_fish = 0

        # checks on age and food availability

        for fish in f2_fishery:
            if fish.age >= 1 < fish.lifespan:
                f2_mature_fish += 1
            fish.age += 1
            if fish.age >= fish.lifespan:
                f2_fishery.remove(fish)
                f2_dead_fish += 1
            else:
                if (len(f1_fishery) - 3*fish.eat) <= 0:
                    #f2_fishery.remove(fish)
                    f2_fishery.pop(random.randint(0, len(f2_fishery) - 1))
                    f2_dead_fish += 1
                else:
                    f1_fishery.pop(random.randint(0,len(f1_fishery)-1))

        if count%2==0:
            reproduce_f2(f2_mature_fish)

        print('Mature fish: %s' % (f2_mature_fish))
        print('Dead fish: %s' % (f2_dead_fish))




        # replenish food stock
        food += 15

        #f.write('%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%(len(f1_fishery),f1_mature_fish,f1_born,f1_dead_fish,food,len(f2_fishery),f2_mature_fish,f2_born,f2_dead_fish))
        f.write('%s,%s,%s\n' % (len(f1_fishery), len(f2_fishery), (food/10)))
        fish1_data.append(len(f1_fishery))
        fish2_data.append((len(f2_fishery)))
        iteration.append(count)
        food_data.append(food)



with open('stat.csv','w') as f:

    populate(5)
    populate_f2(5000)
    iterate(3000)

    #print(food_data)


    plt.title('Small ecosystem simulation')
    #plt.plot(iteration, food_data, ':b', label="Food")
    plt.plot(iteration, fish1_data, label="Prey")
    plt.plot(iteration, fish2_data, label="Predator")
    plt.legend()
    plt.show()

