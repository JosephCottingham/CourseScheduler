
class Node():

    name = None
    prerequisites = list()

    def __init__(self, course_name:str, prerequisites:list()):
        self.name=course_name
        self.prerequisites=prerequisites
