import codewars_test as test
"""
Complete the solution so that it strips all text that follows any 
of a set of comment markers passed in. Any whitespace at the end of 
the line should also be stripped out.
"""


def solution(string, markers):
    result_list = []
    lines = string.split('\n')
    for line in lines:
        largest_marker_index = -1
        for iter_number, marker in enumerate(markers):
            if marker in line:
                index_marker = line.find(marker)
                if largest_marker_index == -1:
                    largest_marker_index = index_marker
                elif index_marker < largest_marker_index:
                    largest_marker_index = index_marker
            if iter_number == len(markers) - 1:
                if largest_marker_index == -1:
                    result_list.append(line)
                    break
                else:
                    result_list.append(line[:largest_marker_index].rstrip())
                    break
        else:
            result_list.append(line)
    return '\n'.join(result_list)


test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), 
                            "apples, pears\ngrapes\nbananas")
test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
