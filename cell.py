class Cell: 
    """A cell that lives in a Sudoku Board.
    """

    def __init__(self, value: str, row: int, col: int) -> None:
        """ Initializes a Cell.

        Args:
            value (str): The value contained in the cell.
            row (int): The row the cell is in.
            col (int): The col the cell is in. 
        """
        self._row = row
        self._col = col
        self._value = value
        self._possible_chars = []

    def get_row(self) -> int:
        """Gets the row of the cell.

        Returns:
            int: The row. 
        """
        return self._row  

    def get_col(self) -> int:
        """Gets the col of the cell.

        Returns:
            int: The col
        """ 
        return self._col 

    def get_possible_chars(self) -> list: 
        """Gets the possible characters of the cell.

        Returns:
            list: The possible characters can than be in value.
        """
        return self._possible_chars

    def get_value(self) -> str: 
        """Gets the value of the cell. 

        Returns:
            str: The value contained in the cell
        """
        return self._value

    def set_possible_chars(self, _possible_chars: list) -> None:
        """Sets the possible characters that can be in values

        Args:
            _possible_chars (list): The characters that can be in values
        """
        self._possible_chars = _possible_chars    

    def set_value(self, value: str) -> None: 
        """Sets the value of the cell

        Args:
            value (str): The value to be contained in the cell. 
        """
        self._value = value
        self._possible_chars = []

    def __repr__(self):
        return self._value