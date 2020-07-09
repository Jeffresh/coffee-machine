class CoffeeMachine:

    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.STATES = ['fill-operation', 'buy-operation', 'waiting']
        self.FILL_STATES = ['fill_water', 'fill_milk', 'fill_beans', 'fill_cups']
        self.actual_state = 'waiting'
        self.actual_fill_state = None

    def machine_state(self):
        print("\nThe coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.cups))
        print("${} of money \n".format(self.money))

    def fill(self, operation):
        if self.actual_fill_state == self.FILL_STATES[0]:
            self.water += int(operation)
            self.actual_fill_state = self.FILL_STATES[1]
            print("Write how many ml of milk do you want to add:")
        elif self.actual_fill_state == self.FILL_STATES[1]:
            self.milk += int(operation)
            self.actual_fill_state = self.FILL_STATES[2]
            print("Write how many g coffee beans do you want to add:")

        elif self.actual_fill_state == self.FILL_STATES[2]:
            self.beans += int(operation)
            self.actual_fill_state = self.FILL_STATES[3]
            print("Write how many disposable cups of coffee do you want to add:")

        elif self.actual_fill_state == self.FILL_STATES[3]:
            self.cups += int(operation)
            self.actual_fill_state = None
            self.actual_state = self.STATES[2]
        else:
            raise Exception("Error: Incorrect fill state")

    def need_resources(self, resource, resource_name, amount):
        if resource - amount < 0:
            print('Sorry, not enough {}!\n'.format(resource_name))
            return False
        else:
            return True

    def buy(self, coffee_type):
        coffee_done = False
        if coffee_type == 'back':
            pass
        else:
            coffee_type = int(coffee_type)
            if coffee_type == 1:
                if self.need_resources(self.water, 'water', 250) and self.need_resources(self.beans, 'beans',
                                                                                         16) and self.need_resources(
                    self.cups,
                    'cups',
                    1):
                    self.water -= 250
                    self.beans -= 16
                    self.money += 4
                    self.cups -= 1
                    coffee_done = True
            elif coffee_type == 2:
                if self.need_resources(self.water, 'water', 350) and self.need_resources(self.milk, 'milk',
                                                                                         75) and self.need_resources(
                    self.beans,
                    'beans',
                    20) and self.need_resources(self.cups, 'cups', 1):
                    self.water -= 350
                    self.milk -= 75
                    self.beans -= 20
                    self.money += 7
                    self.cups -= 1
                    coffee_done = True
            elif coffee_type == 3:
                if self.need_resources(self.water, 'water', 200) and self.need_resources(self.milk, 'milk',
                                                                                         100) and self.need_resources(
                    self.beans,
                    'beans',
                    12) and self.need_resources(self.cups, 'cups', 1):
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.money += 6
                    self.cups -= 1
                    coffee_done = True

            if coffee_done:
                print('I have enough resources, making you a coffee!\n')

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0

    def operate(self, operation):

        if self.actual_state == self.STATES[2]:
            if operation == 'fill':
                self.actual_state = self.STATES[0]
                self.actual_fill_state = self.FILL_STATES[0]
                print("Write how many ml of water fo you want to add:")
            elif operation == 'buy':
                self.actual_state = self.STATES[1]
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
            elif operation == 'take':
                self.take()
            elif operation == 'remaining':
                self.machine_state()

        elif self.actual_state == self.STATES[0]:
            self.fill(operation)
        elif self.actual_state == self.STATES[1]:
            self.buy(operation)
            self.actual_state = self.STATES[2]

    def start(self):
        operation = ''
        while operation != 'exit':
            if my_coffee_machine.actual_state == my_coffee_machine.STATES[2]:
                print("Write action (buy, fill, take, remaining, exit):\n")
            operation = input()
            my_coffee_machine.operate(operation)


if __name__ == '__main__':
    my_coffee_machine = CoffeeMachine()
    my_coffee_machine.start()
