class Email:
    company = "dlsud.edu.ph"

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        char = self.fname
        firstChar = char[0]
        lastName = self.lname.replace(" ","")
        return f"{firstChar.lower()}{lastName.lower()}@{Email.company}"

def name():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    return Email(fname, lname)

def create(names):
    print("=============================Generated Email=============================")
    print("")
    counter = 1
    for nam in names:
        print(str(counter), ".", nam)
        counter += 1

names = []

while True:
    option = input("Add name?: ")
    if option.lower() == "yes":
        names.append(name())
    elif option.lower() == "no":
        create(names)
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
