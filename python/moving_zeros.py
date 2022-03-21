import codewars_test as test
"""Write an algorithm that takes an array and moves all of the zeros to the end, preserving the 
order of the other elements."""


def move_zeros(array):
    zeros_count = array.count(0)
    zeros_array = [0 for _ in range(zeros_count)]

    for _ in range(zeros_count):
        if array[-zeros_count:] == zeros_array:
            return array
        
        first_zero_index = array.index(0)
        array_element = array.pop(first_zero_index)
        array.append(array_element)
    return array


@test.describe("Sample tests")
def sample_tests():
    @test.it("Basic tests")
    def youarecute():
        test.assert_equals(move_zeros(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        test.assert_equals(move_zeros(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        test.assert_equals(move_zeros([0, 0]), [0, 0])
        test.assert_equals(move_zeros([0]), [0])
        test.assert_equals(move_zeros([]), [])
