class ClubMembers:
    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def display(self):
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Age:", self.age)
        print("Favorite food:", self.favorite_food)
        print("Goal:", self.goal)


class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, favorite_food, goal, position):
        super().__init__(name, birthday, age, favorite_food, goal)
        self.position = position

    def display(self):
        super().display()
        print("Position:", self.position)

#create objects
m_1 = ClubMembers("Tom", "January 16", 14, "Ice cream", "To be happy")
o_4 = ClubOfficers("Vera", "June 22", 16, "Beef stroganoff", "To be the world's greatest chef", "Treasurer")

#call methods
m_1.display()
print(" ")
o_4.display()
