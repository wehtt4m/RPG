class Person:
    def __init__(self, name, email, phone, greeting_count = None, friends = None, uniqueGreet = None): 
        self.name = name 
        self.email = email 
        self.phone = phone 
        self.greeting_count = 0
        self.friends = []
        self.uniqueGreet = []

    def greet(self, other_person): 
        print(f'Hello {other_person.name}, I am {self.name}!')
        self.greeting_count += 1
        self.uniqueGreet.append(other_person.name)
        print(f"Greeting Count: {self.greeting_count}")
    
    def print_contact_info(self):
        print(f"Sonny's email: {self.email}, Sonny's phone number {self.phone}")
    
    def add_friend(self,friendName):
        self.friends.append(friendName.name)
        print(self.friends)
    
    def num_friends(self):
        print(len(self.friends))

    def __str__(self):
        return f'Person: {self.name} {self.email} {self.phone}'
    
    def num_unique_people_greeted(self):
        sort = sorted(set(self.uniqueGreet))
        numberSort = len(sort)
        print("Number of Unique Greets: ", numberSort)


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# print(sonny.__str__())
# sonny.add_friend(jordan)
# sonny.num_friends()


jordan.greet(sonny)
sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)


sonny.num_unique_people_greeted()
print(" ")
# print(sonny.email, " ", sonny.phone)
# print(jordan.email, " ", jordan.phone)

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def print_info(self):
#         print(f"Make:{self.make}. Model:{self.model}. Year: {self.year}")


# firstCar = Vehicle("Toyota", "Corolla", "1997")
# firstCar.print_info()