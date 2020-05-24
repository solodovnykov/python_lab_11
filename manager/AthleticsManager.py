import doctest
from model.Athletics import Athletics

class AthleticsManager:

    def __init__(self, athletics_list = None):
        if athletics_list is None:
            self.athletics_list = []
        else:
            self.athletics_list = athletics_list

    def __del__(self):
        return

    def find_types_of_athletics_by_distance(self, distance_in_meters):
        """
        >>> athletic1 = Athletics('Long ', 20, 10, 2000)
        >>> athletic2 = Athletics('Base', 10, 20, 1000)
        >>> athletic3 = Athletics('Sprint', 2, 8, 200)
        >>> athletics = [athletic1, athletic2, athletic3]
        >>> manager = AthleticsManager(athletics)
        >>> print(manager.find_types_of_athletics_by_distance(200))
        ['Sprint']
        """
        result_athletics = []
        for athletics in self.athletics_list:
            if athletics.distance_in_meters == distance_in_meters:
                result_athletics.append(athletics.athletics_name)
            else:
                pass
        return result_athletics

if __name__ == '__main__':
    doctest.testmod(verbose=True)