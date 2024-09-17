from go.group import Group

class Stone():
    """A class to represent a stone in the model.
    """
    
    def __init__(self, board, coord, colour):
        """Initialises a stone with the board it is associated with,
        it's coordinates relative to the board, and a colour. Stones
        are given a group immediately upon placement.

        Args:
            board (Board): The board the stone is on
            coord (Tuple): A relative position for the stone
            colour (Bool): Either black or white
        """
        self.board = board
        self.coord = coord
        self.colour = colour
        self.group = self.find_group()
        self.board.update_points()
        
    def neighbours(self):
        """Find the neighbours of a point on the board and return their coordinates.

        Returns:
            arr[Tuple]: List of the neighbours' coordinates.
        """
        neighbours = [(self.coord[0] - 1, self.coord[1]),
                      (self.coord[0], self.coord[1] + 1),
                      (self.coord[0] + 1, self.coord[1]),
                      (self.coord[0], self.coord[1] - 1)]
        # handle out of bounds instances on 9x9 board
        new_neighbours = {(x,y) for x, y in neighbours if 1 <= x <= 9 and 1 <= y <= 9}
        return new_neighbours
    
    def find_group(self):
        """Finds a group for the stone. This method is run
        on the initialisation of the stone being created and either
        appends to an existing group, creates a new one or merges a
        stone with one or more groups.

        Returns:
            Group: The group the new stone now belongs to
        """
        
        result = []
        stones = self.board.find_stones(self.neighbours())
        for stone in stones:
            # group together if colour is same
            if stone.colour == self.colour and stone.group not in result:
                result.append(stone.group)
        if not result:
            new_group = Group(self.board, self)
            return new_group
        else:
            if len(result) > 1:
            # if there is more than one group, merge them all to the first one
                for group in result[1:]:
                    result[0].merge(group)
            # append to the stones in the group that was found (there should be one)
            result[0].stones.add(self)
            return result[0]
        
    def get_liberties(self):
        """A method to return the liberties of a stone. Liberties
        are simply the neighbours of a stone that are unoccupied.

        Returns:
            arr[Tuple]: coordinates of a stone's liberties
        """
        liberties = self.neighbours()
        stones_coords = {stone.coord for stone in self.board.find_stones(liberties)}
        liberties -= stones_coords
        return list(liberties)
        
    def delete(self):
        """Delete method for a stone
        """
        del self