class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        schedule = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            schedule[prereq].append(course)
            indegree[course] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        processed_courses = 0
        while queue:
            course = queue.popleft()
            processed_courses += 1

            for neighbor in schedule[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return processed_courses == numCourses