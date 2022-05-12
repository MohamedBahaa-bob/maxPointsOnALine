# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def maxPoints(self, points) -> int:
        points.sort()
        # print(points)
        result = 0
        for i in range(0, len(points) - 1):
            slope_count = {}
            for j in range(i + 1, len(points)):
                if points[j][0] - points[i][0] == 0:
                    slope = "vertical"
                else:
                    slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                slope_count[slope] = slope_count.get(slope, 0) + 1
            result = max(result, max(slope_count.values()))
        # print(slope_count)
        return result + 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
