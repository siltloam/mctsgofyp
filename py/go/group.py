

class Group():
    """A class to represent the groups of stones on the board. Groups
    exist so long as they have liberties, and exist as soon as a stone is created.
    """
    
    def __init__(self, board, first_stone):
        """Initialises a group object

        Args:
            board (Board): The board the group is on
            first_stone (arr[Stone]): The array for the stones in the group
        """
        
        self.board = board
        self.stones = set()
        self.stones.add(first_stone)
        # append to the groups on the board upon init
        self.board.groups.append(self)

    def merge(self, second_group):
        """Merges groups of stones together based on the neighbours of a stone.

        Args:
            second_group (Group): The group to merge into the primary group
        """
        for stone in second_group.stones:
            # set the group of the stones to the current group
            stone.group = self
            self.stones.add(stone)
        # remove second group from the board
        self.board.groups.remove(second_group)
    
    def update_groups(self):
        """Updates the positions of  the liberties in the group and
        removes the group from the board if there are 0.
        """
        liberties = (liberty for stone in self.stones for liberty in stone.get_liberties())
        try:
            # checking that there is at least one liberty in the list
            next(liberties)
        except StopIteration:
            self.delete()

    def delete(self):
        """Deletes all stones in the group from the board, then removes the group object.
        """
        while self.stones:
            self.stones.pop().delete()
        self.board.groups.remove(self)
        del self