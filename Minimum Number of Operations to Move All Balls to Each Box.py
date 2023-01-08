class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        prefix = [0] * len(boxes)
        postfix = [0] * len(boxes)
        self.prefixSum(prefix, boxes)
        self.prefixSum(postfix, boxes[::-1])

        minOps = [0] * len(boxes)
        for i in range(len(boxes)):
            minOps[i] = prefix[i] + postfix[len(boxes)-i-1]

        return minOps

    def prefixSum(self, array, boxes):
        ones = 0
        for i in range(1, len(boxes)):
            if boxes[i-1] == "1":
                ones += 1
            array[i] = array[i-1] + ones
