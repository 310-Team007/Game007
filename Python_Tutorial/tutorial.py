"""
This is a simply tutorial in using classes
and common python progress
"""

class Info():
    """
    This class will control how code inthe file flows
    """
    def __init__(self):
       self.f_name = str
       self.l_name = str
       
       
    def get_info(self):
        self.f_name = input("What is your first name: ")
        self.l_name = input("What is your last name: ")
        
    def display_info(self):
        print(f'Hello {self.f_name} {self.l_name}!')
        


def main():
    info = Info()
    info.get_info()
    info.display_info()
    
    

if __name__ == "__main__":
  main()