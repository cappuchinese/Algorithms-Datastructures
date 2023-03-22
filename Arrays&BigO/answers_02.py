"""some python examples for a few problems"""


def insert_from_start(sorted_int_list, item):
    """
    goal: insert int item into a SORTED list, sorted_int_list, starting at the start of the list
    input: sorted list of integers sorted_int_list, integer item
    output: -
    preconditions: sorted_int_list is sorted from small to large
    postconditions: item is inserted into sorted_int_list; sorted_int_list is still sorted
    """

    index = 0

    # look for the insertion point
    while index <= len(sorted_int_list) - 1:
        if sorted_int_list[index] < item:
            # just proceed
            pass
        else:
            # insert item
            tmp = sorted_int_list[index]
            sorted_int_list[index] = item
            item = tmp
        index += 1
    # at the end of the list, append the last item
    sorted_int_list.append(item)


def insert_from_back(sorted_int_list, item):
    """
    goal: insert int item into a SORTED list, sorted_int_list, starting at the back of the list
    input: sorted list of integers sorted_int_list, integer item
    output: -
    preconditions: sorted_int_list is sorted from small to large
    postconditions: item is inserted into sorted_int_list; sorted_int_list is still sorted
    """

    index = len(sorted_int_list)
    # making space. len(list) ≠ sizeof(list)!
    sorted_int_list.append(item)

    while index > 0:
        if sorted_int_list[index - 1] > item:
            sorted_int_list[index] = sorted_int_list[index - 1]
        else:
            sorted_int_list[index] = item
            # ready! break out of the loop
            index = -1
        index = index - 1
    if index == 0:
        sorted_int_list[0] = item
