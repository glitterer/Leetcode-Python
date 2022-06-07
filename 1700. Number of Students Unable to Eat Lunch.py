class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        line = collections.deque()
        for i in students:
            line.append(i)
            
        count = 0 # 넘긴 횟수 (rotate 횟수)
        
        while True:
            if len(line) == 0:
                return 0
            else:
                if count == len(line):
                    break
                    print(count)
                else:
                    if line[0] == sandwiches[0]:
                        line.popleft()
                        sandwiches.pop(0)
                        count = 0
                    else:
                        line.append(line.popleft())
                        count += 1
        return len(line)
