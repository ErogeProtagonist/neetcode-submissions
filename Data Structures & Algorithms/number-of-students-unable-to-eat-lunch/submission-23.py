class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        preferences = [students.count(0), students.count(1)]
        for i in sandwiches:
            if preferences[i] == 0:
                break
            preferences[i] -= 1
        return sum(preferences)
