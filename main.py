from random import random
from time import sleep

class FSM:
    def __init__(self, num_days):
        self.time = 0
        self.num_days = num_days

        # current state of the system
        self.current_state = self.q0

        # stopped flag to denote that iteration is stopped
        self.stopped = False

    def show_time(self):
        '''Just print time.
        '''
        print(f'-------------------------------------\nO`clock: {self.time % 24}\n')

    # sleep
    def q0(self):
        ''''''
        rand = random()

        if self.time >= self.num_days * 24: # end the system
            self.stopped = True
            self.time = 0

        if self.time % 24 != 7:
            print('*sleep*')
            self.time += 1
        elif rand < 0.4:
            self.show_time()
            print('Wow! On time. Let`s grab a bite!')
            self.current_state = self.q2 # eat
        elif 0.4 <= rand < 0.6:
            self.time += 1
            self.show_time()
            print('Shit. One hour later... Don`t have time for breakfast.')
            self.current_state = self.q2 # commute
        elif rand >= 0.6:
            self.time += 2
            self.show_time()
            print('F*CK! I have passed a class! I have to run.')
            self.current_state = self.q2 # commute

    # eat
    def q1(self):
        ''''''
        if self.time % 24 < 12:
            print('Avarage breakfast.')
            self.current_state = self.q2
        elif self.time % 24 < 18:
            print('Finally, lunch!')
            self.time += 1
            self.current_state = self.q2
        else:
            print('Dinner is... Ok. Now I want to sleep.')
            self.current_state = self.q0

        self.time += 1

    # commute
    def q2(self):
        ''''''
        if self.time % 24 < 12:
            print('Commuting to UCU.')
            self.current_state = self.q3 # classes
        else:
            print('Commuting home!')
            self.current_state = self.q4 # Netflix
        
        rand = random()
        if rand > 0.7:
            print('Yoooo, bus!')
        else:
            self.time += 1

    # classes
    def q3(self):
        ''''''
        print('Classes time... Yay...')
        self.time = (self.time // 24) * 24 + 15
        self.show_time()
        print('Classes ended.')
        self.current_state = self.q1 # eat

    # Netflix
    def q4(self):
        ''''''
        print('Let`s relax and watch some Netflix.')

        rand = random()
        if rand > 0.6:
          print('Wow! What wonderful series!')
          self.time += 3
        else:
          print('Ehh... Nothing especial...')
          self.time += 1

        self.show_time()
        self.current_state = self.q1 # eat

if __name__ == '__main__':
    print('Enter number of days to simulate.')
    system = FSM(int(input('>>> ')))

    while not system.stopped:
        if not system.current_state == system.q0:
            system.show_time()
        system.current_state()
        sleep(1)
    
    print('Simulation is ended.')
