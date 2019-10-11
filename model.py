
import numpy as np
import matplotlib.pyplot as plt
from random import random, randint

class World():
    """Class for simulating a world containing Zombies and Doctors"""

    def __init__(self, population, initial_infection_rate, closeness, dimensions, speed, frequency, turns, no_doctors, length_of_immunity):
        """Constructor for zombies"""
        self.objectList = []
        self.doctorsList = []
        self.population = population
        self.initial_infection_rate = initial_infection_rate
        self.length_of_immunity = length_of_immunity
        self.closeness = closeness
        self.dimensions = dimensions
        self.speed = speed
        self.frequency = frequency
        self.turns = turns
        self.no_doctors = no_doctors

    def populate_world(self, population, initial_infection_rate, closeness):
        """Adds doctors and people/zombies to world"""
        for person in range(population):
            self.objectList.append(Zombie(self.speed, initial_infection_rate, closeness, self.dimensions, self.length_of_immunity))
        for doctor in range(self.no_doctors):
            self.doctorsList.append(Doctor(self.speed, closeness, self.dimensions))

    def update_world(self, turn):
        """Moves people and doctors and will infect people if eligible"""
        for person in self.objectList:
            person.move()
            for other_zombie in self.objectList:
                if person.is_infected and person.touching(other_zombie):
                    other_zombie.infect(turn)
        for doctor in self.doctorsList:
            doctor.move()
            for other_zombie in self.objectList:
                if doctor.touching(other_zombie):
                    other_zombie.heal(turn)


    def create_coord_list(self):
        """Create a list of where every Zombie or Doctor is in temrs of x and y"""
        infected = np.zeros(shape=(len(self.objectList), 2))
        healthy = np.zeros(shape=(len(self.objectList), 2))
        doctors = np.zeros(shape=(len(self.doctorsList), 2))
        for i, j in enumerate(self.objectList):
            if j.is_infected:
                infected[i, 0] = j.x
                infected[i, 1] = j.y
            else:
                healthy[i, 0] = j.x
                healthy[i, 1] = j.y
        for i, j in enumerate(self.doctorsList):
            doctors[i, 0] = j.x
            doctors[i, 1] = j.y




        return infected, healthy, doctors

    def plot(self, infected, healthy, doctors, no):
        """Plots the locations of Zombies and doctors on blank map"""
        plt.scatter(infected[:, 0], infected[:, 1], facecolor='red')
        plt.scatter(healthy[:, 0], healthy[:, 1], facecolor='blue')
        plt.scatter(doctors[:, 0], doctors[:, 1], facecolor='green')
        plt.axis('off')
        plt.savefig('snapshots/{}.png'.format(no))
        return 'snapshots/{}.png'.format(no)



    def get_number_infected(self):
        """Returns the number of infected Zombies in the world"""
        count = 0
        for person in self.objectList:
            if person.is_infected:
                count += 1
        return count


    def get_number_well(self):
        """Returns the number of uninfected Zombies in the world"""
        count = 0
        for person in self.objectList:
            if person.is_infected == False:
                count += 1
        return count

    def train_doctor(self):
        """Will create a new doctor object"""
        self.doctorsList.append(Doctor(self.speed, self.closeness, self.dimensions))


class Doctor:

    def __init__(self, speed, closeness, dimensions):
        """Constructor for Zombie"""
        self.speed = speed
        self.dimensions = dimensions
        self.x = randint(0, dimensions)
        self.y = randint(0, dimensions)
        self.closeness = closeness

    def touching(self, zombie):
        """Determines whether or not two Zombies or a Zombie and a doctor are touching"""
        if ((self.x - zombie.x) ** 2 + (self.y - zombie.y) ** 2) ** 0.5 <= self.closeness:
            return True
        else:
            return False

    def move(self):
        self.small_offset = -1 * random()
        x_mover = 2 * (self.speed * (random() - 1) + self.small_offset)
        y_mover = 2 * (self.speed * (random() - 1) + self.small_offset)
        x_move = self.x + x_mover
        y_move = self.y + y_mover
        if x_move > self.dimensions or x_move < 0:
            x_mover = -30 * x_mover
        if y_move > self.dimensions or y_move < 0:
            y_mover = -30 * y_mover
        self.x = self.x + x_mover
        self.y = self.y + y_mover

    def infect(self):
        if not self.infected:
            self.infected = True


class Zombie:
    """"""

    def __init__(self, speed, infection_rate, closeness, dimensions, length_of_immunity):
        """Constructor for Zombie"""
        self.speed = speed
        self.dimensions = dimensions
        self.length_of_immunity = length_of_immunity
        self.x = randint(0, self.dimensions)
        self.y = randint(0, self.dimensions)
        self.turn_healed = 0
        self.closeness = closeness
        if random() < infection_rate:
            self.infected = True
        else:
            self.infected = False

    def touching(self, zombie):
        if ((self.x - zombie.x)**2 + (self.y - zombie.y)**2)**0.5 <= self.closeness:
            return True
        else:
            return False

    def move(self):
        self.small_offset = -1 * random()
        x_mover = 2*(self.speed*(random()-1)+self.small_offset)
        y_mover = 2 * (self.speed * (random() - 1) + self.small_offset)
        x_move = self.x + x_mover
        y_move = self.y + y_mover
        if x_move > self.dimensions or x_move < 0:
            x_mover = -16*x_mover
        if y_move > self.dimensions or y_move < 0:
            y_mover = -16*y_mover
        self.x = self.x + x_mover
        self.y = self.y + y_mover

    def infect(self, count):
        if not self.infected and count-self.turn_healed > self.length_of_immunity:
            self.infected = True

    @property
    def is_infected(self):
        return self.infected

    def heal(self, turn_healed):
        if self.infected:
            self.infected = False
            self.turn_healed = turn_healed


