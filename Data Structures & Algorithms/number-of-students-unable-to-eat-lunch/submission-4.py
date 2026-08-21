class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches:
            while students:
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    students.append(students[0])
                    students.pop(0)
                    
                print(students)
                print(sandwiches)
                if len(students) < 1:
                    return 0
                if (sum(students) == 0 or sum(students) == len(students)) and (students[0] != sandwiches[0]):
                    return len(students)
            
        return len(students)