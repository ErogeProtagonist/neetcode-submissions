class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_head = ListNode(-1)
        current = student_head
        for i in range(len(students)):
            current.next = ListNode(students[i])
            current = current.next
        student_tail = current
    
        sandwich_head = ListNode(-2)
        current = sandwich_head
        for i in range(len(sandwiches)):
            current.next = ListNode(sandwiches[i])
            current = current.next
        
        
        current_sandwich = sandwich_head.next
        current_student = student_head.next
        student_count = len(students)
        consecutive_rejections = 0
        while current_sandwich:
            
            if current_student.val == current_sandwich.val:
                current_sandwich = current_sandwich.next
                sandwich_head.next = current_sandwich
                
                
                current_student = current_student.next
                student_head.next = current_student
                
                student_count -= 1
                consecutive_rejections = 0
            else:
                student_to_move = current_student
                current_student = current_student.next
                student_head.next = current_student
                student_tail.next = student_to_move
                student_tail = student_tail.next
                student_to_move.next = None
                consecutive_rejections += 1
            
            
            if consecutive_rejections == student_count:
                return student_count
            if student_count == 0:
                return 0
        return student_count
        