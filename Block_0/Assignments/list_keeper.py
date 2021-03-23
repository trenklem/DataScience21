class ListKeeperError(Exception):
    pass


class ListKeeper:
    """
    Stores named lists
    """

    def __init__(self, name: str = "example", li: [int] = [1, 2, 3, 4, 5]):
        self.__list = {}
        if name is not None and li is not None:
            self.add(name, li)

    def show(self) -> [str]:
        """
        Returns all list names
        :return: List which contains the list names
        """
        names = []
        for name in self.__list.keys():
            names.append(name)
        return names

    def add(self, name: str, li: [int]) -> [int]:
        """
        Adds a new list with the given name. If the name already exists a ListKeeperError is raised
        :param name: Name of the list
        :param li: List of integers
        :return: The added list
        """
        if name in self.__list.keys():
            raise ListKeeperError("A list with that name already exists")
        self.__list[name] = li
        return self.__list[name]

    def delete(self, name: str) -> str:
        """
        Remove a list
        :param name: The name of the list to remove
        :return: The name of the deleted list
        """
        if name in self.__list.keys():
            del self.__list[name]
        return name

    def sort(self, name: str) -> [int]:
        """
        Sorts the list with the given name ascending. If the name does not exists a ListKeeperError is raised
        :param name: The name of the list to sort
        :return: The sorted list
        """
        if name not in self.__list.keys():
            raise ListKeeperError("A list with that name does not exist")
        self.__list[name].sort()
        return self.__list[name]

    def append(self, name: str, li: [int]) -> [int]:
        """
        Appends the given list to the list with the given name. If the list does not yet exist it gets created
        :param name: The name of the list to sort
        :param li: List of integers
        :return: The list for the given name
        """
        if name not in self.__list.keys():
            return self.add(name, li)
        self.__list[name] = self.__list[name] + li
        return self.__list[name]
