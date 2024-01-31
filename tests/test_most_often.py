from lib.most_often import *

"""
Given and empty list
return None but test will pass
"""

def test_given_initial_list_added_to_starting_list():
    initialise = MostOften([1, 2, 3, 4])
    assert initialise.starting_list == [1, 2, 3, 4]

def test_given_initial_list_plus_1_added_item_returns_revised_list():
    initialise = MostOften([1, 2, 3, 4])
    initialise.add_new(5)
    assert initialise.starting_list == [1, 2, 3, 4, 5]

def test_given_initial_list_plus_multiple_added_item_returns_revised_list():
    initialise = MostOften([1, 2, 3, 4])
    initialise.add_new(5)
    initialise.add_new('six')
    initialise.add_new(True)
    initialise.add_new(5.685)
    assert initialise.starting_list == [1, 2, 3, 4, 5, 'six', True, 5.685]    

"""
Given a list with 5 items, with 1 item value repeated twice
Returns the repeated item when get_most_often method called
""" 

def test_get_most_often_winner_from_initial_list():
    initialise = MostOften([1, 2, 3, 3, 4])
    assert initialise.get_most_often() == 3

"""
Given a list with 5 unique items.
Call get_most_often method 
Returns "no clear winner"
""" 

def test_get_unique_list_return_no_winner():
    initialise = MostOften([1, 2, 3, 4, 5])
    assert initialise.get_most_often() == 'no clear winner'

"""
Given a list with 5 items, 3 of them unique and 2 items repeating twice
Call get_most_often method
Returns "no clear winner"
"""

def test_get_list_with_two_repeated_items_return_no_winner():
    initialise = MostOften([1, 2, 2, '2', '2'])
    assert initialise.get_most_often() == 'no clear winner'

"""
Given an initial list with 2 unique items and then 3 new items added.  2 new items match
Call get_most_often method
Returns "no clear winner"
"""

def test_get_list_add_items_return_winner_after_items_added():
    initialise = MostOften([1, 2])
    initialise.add_new('Firat')
    initialise.add_new(2)
    initialise.add_new(2)
    assert initialise.get_most_often() == 2
    
def test_get_list_add_items_return_winner_decided_by_items_added():
    initialise = MostOften([1, 1, 'Tom'])
    initialise.add_new('Firat')
    initialise.add_new('Firat')
    initialise.add_new('Firat')
    assert initialise.get_most_often() == 'Firat'

def test_get_list_add_items_return_no_winner_item_count_equal():
    initialise = MostOften([1, 'Tom'])
    initialise.add_new('Tom')
    initialise.add_new(True)
    initialise.add_new(True)
    assert initialise.get_most_often() == 1

def test_get_empty_list_return_no_winner():
    initialise = MostOften([])
    assert initialise.get_most_often() == 'no clear winner'
    # # with pytest.raises(UnboundLocalError) as e:
    # #     initialise.get_most_often()
    # # error_message = str(e.value)
    # assert  error_message == "cannot access local variable 'highest_items' where it is not associated with a value"