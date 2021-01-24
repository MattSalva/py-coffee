# Write your code here
class Coffee:
    req_espresso = {'water': 250, 'milk': 0, 'beans': 16, 'cost': 4}
    req_latte = {'water': 350, 'milk': 75, 'beans': 20, 'cost': 7}
    req_cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'cost': 6}

    def __init__(self, water, milk, beans, money, disposable_cups):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.money = money
        self.disposable_cups = disposable_cups

    def buy(self, coffee):
        if self.req_check(coffee):
            if coffee == '1':
                self.water -= coffee_machine.req_espresso['water']
                self.milk -= coffee_machine.req_espresso['milk']
                self.beans -= coffee_machine.req_espresso['beans']
                self.money += coffee_machine.req_espresso['cost']
                self.disposable_cups -= 1
            elif coffee == '2':
                self.water -= coffee_machine.req_latte['water']
                self.milk -= coffee_machine.req_latte['milk']
                self.beans -= coffee_machine.req_latte['beans']
                self.money += coffee_machine.req_latte['cost']
                self.disposable_cups -= 1
            elif coffee == '3':
                self.water -= coffee_machine.req_cappuccino['water']
                self.milk -= coffee_machine.req_cappuccino['milk']
                self.beans -= coffee_machine.req_cappuccino['beans']
                self.money += coffee_machine.req_cappuccino['cost']
                self.disposable_cups -= 1

            print('I have enough resources, making you a coffee!')
        else:
            print("I don't have enough resources.")

    def fill(self):
        print("Write how many ml of water do you want to add:")
        in_water = int(input())
        print("Write how many ml of milk do you want to add:")
        in_milk = int(input())
        print("Write how many grams of coffee do you want to add:")
        in_beans = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        amount_cups = int(input())
        self.water += in_water
        self.milk += in_milk
        self.beans += in_beans
        self.disposable_cups += amount_cups

    def take(self):
        print(f'I gave you {self.money}')
        self.money = 0


    def req_check(self, choice):
        if self.disposable_cups < 1:
            return False
        elif choice == '1':
            r = (self.req_espresso['water'] <= self.water) and (self.req_espresso['beans'] <= self.beans) and (
                        self.req_espresso['milk'] <= self.milk)
            return r
        elif choice == '2':
            r = (self.req_latte['water'] <= self.water) and (self.req_latte['beans'] <= self.beans) and (
                        self.req_latte['milk'] <= self.milk)
            return r
        elif choice == '3':
            r = (self.req_cappuccino['water'] <= self.water) and (self.req_cappuccino['beans'] <= self.beans) and (
                        self.req_cappuccino['milk'] <= self.milk)
            return r

    def print_state(self):
        print(f'''The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.beans} of coffee beans
        {self.disposable_cups} of disposable cups
        {self.money} of money
        ''')


coffee_machine = Coffee(400, 540, 120, 550, 9)

while True:
    print('Write action (buy, fill, take, remaining, exit):')

    user_input = input()

    if user_input == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - back:')
        coffee_choice = input()
        if user_input == 'back':
            continue
        coffee_machine.buy(coffee_choice)
    elif user_input == 'fill':
        coffee_machine.fill()
    elif user_input == 'take':
        coffee_machine.take()
    elif user_input == 'remaining':
        coffee_machine.print_state()
    elif user_input == 'exit':
        break


# coffee = Coffee(in_water, in_milk, in_beans)
# cups_available = coffee.req_check(amount_cups)

# if amount_cups == cups_available:
#     print("Yes, I can make that amount of coffee")
# elif amount_cups < cups_available:
#     print(f"Yes, I can make that amount of coffee (and even {cups_available-1} more than that.")
# else:
# print(f"No, I can make only {cups_available} cups of coffee.")
