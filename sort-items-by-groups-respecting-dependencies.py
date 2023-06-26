class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        elemGraph = defaultdict(list)
        elemIncoming = {i: 0 for i in range(n)}
        elemOrder = []
        elemQueue = deque()

        groupGraph = defaultdict(set)
        groupIncoming = {i: 0 for i in range(-1, m+n)}
        groupOrder = []
        groupQueue = deque()

        for i in range(n):
            for elem in beforeItems[i]:
                elemGraph[elem].append(i)
                elemIncoming[i] += 1

        for i in range(n):
            if elemIncoming[i] == 0:
                elemQueue.append(i)

        while elemQueue:
            item = elemQueue.popleft()
            elemOrder.append(item)

            for neighbor in elemGraph[item]:
                if group[item] == -1:
                    if group[neighbor] == -1:
                        if neighbor+m not in groupGraph[item+m]:
                            groupGraph[item+m].add(neighbor+m)
                            groupIncoming[neighbor+m] += 1
                    else:
                        if group[neighbor] not in groupGraph[item+m]:
                            groupGraph[item+m].add(group[neighbor])
                            groupIncoming[group[neighbor]] += 1
                elif group[neighbor] == -1:
                    if neighbor + m not in groupGraph[group[item]]:
                        groupGraph[group[item]].add(neighbor+m)
                        groupIncoming[neighbor+m] += 1

                else:
                    if group[neighbor] not in  groupGraph[group[item]] and group[neighbor] != group[item]:
                        groupGraph[group[item]].add(group[neighbor])
                        groupIncoming[group[neighbor]] += 1

                elemIncoming[neighbor] -= 1

                if elemIncoming[neighbor] == 0:
                    elemQueue.append(neighbor)

        if len(elemOrder) != n:
            return []

        for key, val in groupIncoming.items():
            if val == 0:
                groupQueue.append(key)

        while groupQueue:
            g = groupQueue.popleft()
            groupOrder.append(g)

            for neighbor in groupGraph[g]:
                groupIncoming[neighbor] -= 1

                if groupIncoming[neighbor] == 0:
                    groupQueue.append(neighbor)

        groupElements = defaultdict(list)
        for elem in elemOrder:
            if group[elem] == -1:
                groupElements[elem+m].append(elem)
            else:
                groupElements[group[elem]].append(elem)

        finalOrder = []
        for g in groupOrder:
            finalOrder.extend(groupElements[g])

        if len(finalOrder) != n:
            return []

        return finalOrder