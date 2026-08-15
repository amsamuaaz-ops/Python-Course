class IOstring:
    def __init__(self):
        self.str1 = ""
    def get_string(self):
      self.str1 =  input("WHAT IS YOUR STRING")

    def print_string(self):
       print("THE RESULT IS" ,self.str1.upper())

str1 = IOstring()
str1.get_string()
str1.print_string()

