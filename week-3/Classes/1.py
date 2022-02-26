class SimpleClass:
    value = ""

    def get_string(self):
        self.value = input("Insert something:\n")

    def print_string(self):
        print(self.value.upper())


cl = SimpleClass()
cl.get_string()
cl.print_string()


