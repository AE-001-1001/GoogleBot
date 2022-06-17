pe1 = ["Software Engineer", "Andrew", 20, "Junior", 5000]
pe2 = ["Software Engineer", "John", 20, "Junior", 5000]

#class
class SoftwareEngineer:

    alias = "Keyboard Magic"

    def __init__(self, name, age, level, salary):
        #Instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

#Instance methods

pe1 = SoftwareEngineer("Andrew", 20, "Junior", 5000)
print(pe1.name,pe1.level,pe1.salary)
pe2 = SoftwareEngineer("John", 20, "Junior", 5000)
print(pe2.name,pe2.level,pe2.alias)


