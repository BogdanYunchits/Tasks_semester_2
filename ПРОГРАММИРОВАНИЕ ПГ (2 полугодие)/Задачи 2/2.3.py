class Soda:
    def __init__(self, add_on=None):
        self.add_on = add_on

    def describe_soda(self):
        if self.add_on:
            print(f"Soda with {self.add_on}")
        else:
            print("Regular Soda")


soda1 = Soda("lemon")
soda1.describe_soda()  # Output: Soda with lemon

soda2 = Soda()
soda2.describe_soda()  # Output: Regular Soda
