

import matplotlib.pyplot as plt
from model import World, Zombie, Doctor


class Controller:

    def __init__(self, population, initial_infection_rate, closeness, dimensions, speed, frequency, turns, no_doctors, length_of_immunity, train_new_doctor_frequency):
        self.my_world = World(population, initial_infection_rate, closeness, dimensions, speed, frequency, turns, no_doctors, length_of_immunity)
        self.my_world.populate_world(population, initial_infection_rate, closeness)
        self.infectedCount = []
        self.healthyCount = []
        self.count = 0
        self.frequency = frequency
        self.train_new_doctor_frequency = train_new_doctor_frequency

    def runTurn(self, count):

        self.my_world.update_world(count)

        if count % self.train_new_doctor_frequency == 0:
            self.my_world.train_doctor()

        infected, healthy, doctors = self.my_world.create_coord_list()
        self.my_world.plot(infected[2:], healthy[2:], doctors, count)
        plt.savefig('web/snapshots/{}.png'.format(count))


        self.infectedCount.append(self.my_world.get_number_infected())
        self.healthyCount.append(self.my_world.get_number_well())

        return 'snapshots/{}.png'.format(count)

