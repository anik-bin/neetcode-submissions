class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                index, poped_height = stack.pop()

                width = i - index
                area = poped_height * width

                max_area = max(max_area, area)

                start = index

            stack.append((start, height))

        while stack:
            index, height = stack.pop()

            width = len(heights) - index
            area = height * width

            max_area = max(max_area, area)

        return max_area