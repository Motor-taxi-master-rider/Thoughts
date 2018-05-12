from typing import Tuple


def max_rectangle_in_histogram(heights: list) -> int:
    """
    输入列表为柱状图各柱的高度，计算该图中形成的最大矩形的面积。如[3, 2, 3]则返回高为2宽为3的矩形面积6
    :param heights: 柱状图的高度序列
    :return: 最大矩形面积
    """

    def expand_column(current_index: int) -> Tuple[int, int]:
        """
        计算以柱状图第center柱为中心向两边拓展的最大矩形面积。
        第center柱的高度大于或等于第right柱高度。当前者大于后者时，右边界为right，左边界为left；
        当两者相等时，所返回面积将小于等于真实值（右边界大于等于第right柱），此时以第right柱为中心的
        拓展矩形面积为更大值。
        :return: 以第center柱为中心拓展的最大矩形面积
        """
        nonlocal heights, previous_low
        center = previous_low.pop()
        left = previous_low[-1] + 1 if previous_low else 0
        right = current_index - 1
        width = right - left + 1
        height = heights[center]
        return center, width * height

    previous_low = []
    expand_area = [0] * len(heights)
    for index, value in enumerate(heights):
        while previous_low and value <= heights[previous_low[-1]]:
            center_index, area_size = expand_column(index)
            expand_area[center_index] = area_size
        previous_low.append(index)

    while previous_low:
        center_index, area_size = expand_column(len(heights))
        expand_area[center_index] = area_size

    return max(expand_area)


if __name__ == '__main__':
    test = [3, 4, 5, 4, 3, 6]
    assert max_rectangle_in_histogram(test) == 18

    test = [1, 2, 6, 2, 1, 1, 1]
    assert max_rectangle_in_histogram(test) == 7

    test = [1, 2, 8, 2, 1, 1, 1]
    assert max_rectangle_in_histogram(test) == 8

    test = [1, 2, 1, 2, 4, 4, 1]
    assert max_rectangle_in_histogram(test) == 8

    test = [1, 8, 1, 2, 3, 3, 1]
    assert max_rectangle_in_histogram(test) == 8

    test = [4, 4, 1, 1, 3, 3, 3]
    assert max_rectangle_in_histogram(test) == 9
