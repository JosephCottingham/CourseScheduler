from course_graph.node import Node

class Course_Graph():
    
    _graph = dict()

    def add_node(self, name, prerequisites):
        if name in self._graph.keys():
            raise Class_Name_Already_Used()            
        new_node = Node(course_name=name, prerequisites=prerequisites)
        self._graph[name] = new_node

    def get_by_name(self, name):
        return self._graph[name]

    def get_prerequisites(self, course_name:str, prerequisites=None):
        if not prerequisites:
            prerequisites = list()
        temp_course = self.get_by_name(name=course_name)
        for course in temp_course.prerequisites:
            if course not in prerequisites:
                prerequisites.append(course)
                prerequisites = self.get_prerequisites(course, prerequisites=prerequisites)
        return prerequisites

    def get_num_prerequisites(self, course_name:str):
        temp_course = self.get_by_name(name=course_name)
        prerequisites = 0
        for course in temp_course.prerequisites:
            prerequisites+=1
        return prerequisites

    def add_nodes_from_json(self, courses_json:dict):
        for course_json in courses_json:
            self.add_node(name=course_json['name'], prerequisites=course_json['prerequisites'])

    def get_all_courses(self):
        course_list = list()
        for course_name in self._graph.keys():
            course_list.append(self._graph[course_name])
        return course_list

    def get_all_courses_names(self):
        return self._graph.keys()

    def get_schdule(self):
        ordered_courses = list()
        temp_graph = self._graph
        while len(temp_graph) > 0:
            for course_name in temp_graph.keys():
                for prerequisite in temp_graph[course_name].prerequisites:
                    if prerequisite in temp_graph.keys():
                        break
                ordered_courses.append(course_name)
                del temp_graph[course_name]
                break
        return ordered_courses


class Class_Name_Already_Used(Exception):
    
    def __init__(self, message="Name is already in use."):
        self.message = message
        super().__init__(self.message)
