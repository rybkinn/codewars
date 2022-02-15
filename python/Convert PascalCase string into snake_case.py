import codewars_test as test
"""Complete the function/method so that it takes a PascalCase string and returns the string in 
snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, 
it should return a string."""


def to_underscore(string):
    if isinstance(string, int):
        return str(string)

    words = []
    now_index = 0
    for index, char in enumerate(string):
        if index and char.isupper():
            words.append(string[now_index:index])
            now_index = index
    words.append(string[now_index:])

    edit_words = [word[0].lower() + word[1:] for word in words]

    return '_'.join(edit_words)


@test.describe("Sample tests")
def sample_tests():
    @test.it("Tests")
    def it_1():
        test.assert_equals(to_underscore("TestController"), "test_controller")
        test.assert_equals(to_underscore("MoviesAndBooks"), "movies_and_books")
        test.assert_equals(to_underscore("App7Test"), "app7_test")
        test.assert_equals(to_underscore(1), "1")
