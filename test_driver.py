from course_graph.course_graph import Course_Graph
import json, os
if __name__ == '__main__':
    json_file = open('test.json',)
    courses_json = json.load(json_file)
    json_file.close()
    cg = Course_Graph()
    cg.add_nodes_from_json(courses_json=courses_json)
    print(cg.get_all_courses_names())
    print('')
    print('FEW 2.3')
    print(cg.get_prerequisites('FEW 2.3'))
    print(cg.get_num_prerequisites('FEW 2.3'))
    print('')
    print('WEB 1.1')
    print(cg.get_prerequisites('WEB 1.1'))
    print(cg.get_num_prerequisites('WEB 1.1'))
    print('')
    print('WEB 1.0')
    print(cg.get_prerequisites('WEB 1.0'))
    print(cg.get_num_prerequisites('WEB 1.0'))
    print('')
    print(cg.get_schdule())