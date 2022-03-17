import codewars_test as test
"""For this exercise you will be strengthening your page-fu mastery. You will complete the 
PaginationHelper class, which is a utility class helpful for querying paging information 
related to an array.

The class is designed to take in an array of values and an integer indicating how many items 
will be allowed per each page. The types of values contained within the collection/array are 
not relevant."""


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
  
    # returns the number of pages
    def page_count(self):
        return (len(self.collection) // self.items_per_page) + 1
    
    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0 or page_index > (self.page_count() - 1):
            return -1
        
        if page_index == (self.page_count() - 1):
            return len(self.collection) % self.items_per_page
        else:
            return self.items_per_page


    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index > (len(self.collection) - 1):
            return -1
        else:
            return item_index // self.items_per_page
        

@test.describe("Sample tests")
def sample_tests():
    @test.it("Tests")
    def it_1():
        collection = range(1, 25)
        helper = PaginationHelper(collection, 10)

        test.assert_equals(helper.page_count(), 3, 'page_count is returning incorrect value.')
        test.assert_equals(helper.page_index(23), 2, 'page_index returned incorrect value')
        test.assert_equals(helper.item_count(), 24, 'item_count returned incorrect value')
