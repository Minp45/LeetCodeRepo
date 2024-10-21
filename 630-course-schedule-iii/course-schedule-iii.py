import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Step 1: Sort the courses by their lastDay
        courses.sort(key=lambda x: x[1])
        
        total_time = 0
        max_heap = []
        
        # Step 2: Iterate through the sorted courses
        for duration, lastDay in courses:
            total_time += duration
            heapq.heappush(max_heap, -duration)  # Use negative for max-heap behavior
            
            # Step 3: If total_time exceeds the current course's lastDay, drop the longest course
            if total_time > lastDay:
                longest_course = -heapq.heappop(max_heap)
                total_time -= longest_course  # Remove the longest course from the total time
                
        # Step 4: The number of courses we can take is the size of the max-heap
        return len(max_heap)
