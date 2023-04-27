class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque([0])

        while queue:
            elem = queue.popleft()
            visited.add(elem)

            for neighbor in rooms[elem]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return len(visited) == len(rooms)