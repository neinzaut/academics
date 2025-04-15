class Customers:
    greeting = "Welcome to Coffee Palace!"

    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total

c_1 = Customers("Name = Nate", "\t|| Beverage = Espresso", "\t|| Food = Pastrami on rye", "\t || Total = 220")
c_2 = Customers("Name = Elaine", "\t|| Beverage = Strawberry frapuccino", "\t|| Food = Tuna wrap", "\t || Total = 270")
c_3 = Customers("Name = Samirah", "\t|| Beverage = Iced caffe latte", "\t|| Food = Cinnamon roll", "\t || Total = 225")
c_4 = Customers("Name = Jery", "\t|| Beverage = Caramel macchiato", "\t|| Food = Glazed doughnut", "\t || Total = 230")
c_5 = Customers("Name = Paz", "\t|| Beverage = Iced tea", "\t|| Food = Blueberry pancakes", "\t || Total = 315")

print(Customers.greeting)
print('==============================================================')
print()

data = [
        (c_1.name, c_1.beverage, c_1.food, c_1.total),
        (c_2.name, c_2.beverage, c_2.food, c_2.total),
        (c_3.name, c_3.beverage, c_3.food, c_3.total),
        (c_4.name, c_4.beverage, c_4.food, c_4.total),
        (c_5.name, c_5.beverage, c_5.food, c_5.total),

        ]

padding = 4

num_cols = len(data[0])
widths = [0] * num_cols
for row in data:
    for i, value in enumerate(row):
        widths[i] = max(widths[i], len(str(value)))

format_string = "".join([f'{{:{w + padding}}}' for w in widths])

for row in data:
    print(format_string.format(*[str(x) for x in row]))

print()

