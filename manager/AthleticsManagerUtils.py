import doctest
from model.Athletics import Athletics
from model.SortType import SortType


class AthleticsManagerUtils:

    def __init__(self, athletics_list=None):
        if athletics_list is None:
            self.athletics_list = []
        else:
            self.athletics_list = athletics_list

    def __del__(self):
        return

    def sort_types_of_athletics_by_stage_duration(self, type_of_sort: str):
        """
        >>> athletic1 = Athletics('Long', 20, 10, 2000)
        >>> athletic2 = Athletics('Base', 10, 20, 1000)
        >>> athletic3 = Athletics('Sprint', 2, 8, 200)
        >>> athletics = [athletic1, athletic2, athletic3]
        >>> manager_utils = AthleticsManagerUtils(athletics)
        >>> sorted_athletics = manager_utils.sort_types_of_athletics_by_stage_duration(SortType.ASCENDING.value)
        >>> for athletics in sorted_athletics: print(athletics.athletics_name)
        Sprint
        Base
        Long
        >>> sorted_athletics = manager_utils.sort_types_of_athletics_by_stage_duration(SortType.DESCENDING.value)
        >>> for athletics_1 in sorted_athletics: print(athletics_1.athletics_name)
        Long
        Base
        Sprint
        """
        sorted_athletics = sorted(self.athletics_list, key=lambda athletics: athletics.stage_duration)
        if type_of_sort == SortType.ASCENDING.value:
            return sorted_athletics
        elif type_of_sort == SortType.DESCENDING.value:
            return sorted_athletics[::-1]
        else:
            return sorted_athletics

    def sort_types_of_athletics_by_number_of_participants(self, type_of_sport: str):
        """
        >>> athletic11 = Athletics('Long', 20, 10, 2000)
        >>> athletic21 = Athletics('Base', 10, 20, 1000)
        >>> athletic31 = Athletics('Sprint', 2, 8, 200)
        >>> athletics = [athletic11, athletic21, athletic31]
        >>> manager_utils = AthleticsManagerUtils(athletics)
        >>> sorted_athletics = manager_utils.sort_types_of_athletics_by_number_of_participants(SortType.ASCENDING.value)
        >>> for athletics in sorted_athletics: print(athletics.athletics_name)
        Sprint
        Long
        Base
        >>> sorted_athletics = manager_utils.sort_types_of_athletics_by_number_of_participants(SortType.DESCENDING.value)
        >>> for athletics_1 in sorted_athletics: print(athletics_1.athletics_name)
        Base
        Long
        Sprint
        """
        sorted_athletics = sorted(self.athletics_list, key=lambda athletics: athletics.number_of_participants)
        if type_of_sport == SortType.ASCENDING.value:
            return sorted_athletics
        elif type_of_sport == SortType.DESCENDING.value:
            return sorted_athletics[::-1]


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
