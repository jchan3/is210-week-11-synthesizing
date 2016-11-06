#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Week 11 Chessmaster class task."""


import time


class ChessPiece(object):
    """A Chess Piece class definition.

    Attributes:
        prefix (string): A class attribute of ChessPiece. Defaults to empty
            string.
    """
    prefix = ''

    def algebraic_to_numeric(self, tile):
        """Takes tile and converts it to a tuple with two values, a 0-based
            y-coordinate and a 0-based x-coordinate.

        Args:
            tile (string): The tile position of the chess piece.

        Returns:
            tuple: A tuple with two values, a 0-based y-coordinate and a
            0-based x-coordinate.
        """
        xspot = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        yspot = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7}

        tile0 = tile[0].lower()
        tile1 = int(tile[1])

        if tile1 > 8 or tile1 < 1:
            return None

        xkeys = xspot.keys()
        if tile0 not in xkeys:
            return None

        numeric = (xspot[tile0], yspot[tile1])
        return numeric

    def is_legal_move(self, position):
        """The function tests if the suggested move is legal.

        Args:
            position (string): The tile position of the chess piece.

        Returns:
            boolean: Returns True if the move is legal and False if it is not.
        """
        temp_tuple = self.algebraic_to_numeric(position)

        if temp_tuple:
            return True
        else:
            return False

    def __init__(self, position):
        """Constructor for the ChessPiece() class.

        Args:
            position (string): The tile notation of its current position.

        Attributes:
            position (string): Stores the tile notation of its current position.
            moves (list): A list that stores tuples of information about each
                move this piece has taken.

        Examples:
            >>> piece = ChessPiece('a1')
            >>> piece.position
            'a1'
        """
        self.position = position
        self.moves = []

        if self.is_legal_move(position) is False:
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))

    def move(self, position):
        """The function will move the chess piece.

        Args:
            position (string): The new position if the chess piece is moved.

        Returns:
            tuple: Returns tuple of the old position, new position, and
                timestamp, or False if new move is not legal.
        """
        if self.is_legal_move(position):
            oldposition = self.prefix + self.position
            newposition = self.prefix + position
            timestamp = time.time()

            self.position = position
            temp_tuple = (oldposition, newposition, timestamp)

            self.moves.append(temp_tuple)

            return temp_tuple
        else:
            return False


class Rook(ChessPiece):
    """A Rook is a subclass of the ChessPiece class.

    Args:
        None

    Attributes:
        prefix (string): A class attribute of ChessPiece. Defaults to 'R'
    """
    prefix = 'R'

    def __init__(self, position):
        """Constructor for the Rook() sub-class.

        Args:
            position (string): The tile notation of its current position.

        Attributes:
            position (string): Stores the tile notation of its current position.
            moves (list): A list that stores tuples of information about each
                move this piece has taken.
        """
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """The function tests if the suggested move for the Rook is legal.

        Args:
            position (string): The tile position of the Rook piece.

        Returns:
            boolean: Returns True if the move is legal and False if it is not.
        """
        if ChessPiece.is_legal_move(self, position) is False:
            return False

        old = self.position
        old_numeric = self.algebraic_to_numeric(old)
        new_move = self.algebraic_to_numeric(position)

        old0 = old_numeric[0]
        old1 = old_numeric[1]
        new0 = new_move[0]
        new1 = new_move[1]

        if old0 == new0 or old1 == new1:
            return True
        else:
            return False


class Bishop(ChessPiece):
    """A Bishop is a subclass of the ChessPiece class.

    Args:
        None

    Attributes:
        prefix (string): A class attribute of ChessPiece. Defaults to 'B'
    """
    prefix = 'B'

    def __init__(self, position):
        """Constructor for the Bishop() sub-class.

        Args:
            position (string): The tile notation of its current position.

        Attributes:
            position (string): Stores the tile notation of its current position.
            moves (list): A list that stores tuples of information about each
                move this piece has taken.
        """
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """The function tests if the suggested move for the Bishop is legal.

        Args:
            position (string): The tile position of the Bishop piece.

        Returns:
            boolean: Returns True if the move is legal and False if it is not.
        """
        if ChessPiece.is_legal_move(self, position) is False:
            return False

        old = self.position
        old_numeric = self.algebraic_to_numeric(old)
        new_move = self.algebraic_to_numeric(position)

        old0 = old_numeric[0]
        old1 = old_numeric[1]
        new0 = new_move[0]
        new1 = new_move[1]

        diff1 = abs(old0 - new0)
        diff2 = abs(old1 - new1)

        if diff1 == diff2:
            return True
        else:
            return False


class King(ChessPiece):
    """A King is a subclass of the ChessPiece class.

    Args:
        None

    Attributes:
        prefix (string): A class attribute of ChessPiece. Defaults to 'K'
    """
    prefix = 'K'

    def __init__(self, position):
        """Constructor for the King() sub-class.

        Args:
            position (string): The tile notation of its current position.

        Attributes:
            position (string): Stores the tile notation of its current position.
            moves (list): A list that stores tuples of information about each
                move this piece has taken.
        """
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """The function tests if the suggested move for the King is legal.

        Args:
            position (string): The tile position of the King piece.

        Returns:
            boolean: Returns True if the move is legal and False if it is not.
        """
        if ChessPiece.is_legal_move(self, position) is False:
            return False

        old = self.position
        old_numeric = self.algebraic_to_numeric(old)
        new_move = self.algebraic_to_numeric(position)

        old0 = old_numeric[0]
        old1 = old_numeric[1]
        new0 = new_move[0]
        new1 = new_move[1]

        diff1 = abs(old0 - new0)
        diff2 = abs(old1 - new1)

        if diff1 in [0, 1] and diff2 in [0, 1]:
            return True
        else:
            return False


class Queen(ChessPiece):
    """A Queen is a subclass of the ChessPiece class.

    Args:
        None

    Attributes:
        prefix (string): A class attribute of ChessPiece. Defaults to 'Q'
    """
    prefix = 'Q'

    def __init__(self, position):
        """Constructor for the Queen() sub-class.

        Args:
            position (string): The tile notation of its current position.

        Attributes:
            position (string): Stores the tile notation of its current position.
            moves (list): A list that stores tuples of information about each
                move this piece has taken.
        """
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """The function tests if the suggested move for the Queen is legal.

        Args:
            position (string): The tile position of the Queen piece.

        Returns:
            boolean: Returns True if the move is legal and False if it is not.
        """
        if ChessPiece.is_legal_move(self, position) is False:
            return False

        old = self.position
        old_numeric = self.algebraic_to_numeric(old)
        new_move = self.algebraic_to_numeric(position)

        old0 = old_numeric[0]
        old1 = old_numeric[1]
        new0 = new_move[0]
        new1 = new_move[1]

        if old0 == new0 or old1 == new1:
            return True

        diff1 = abs(old0 - new0)
        diff2 = abs(old1 - new1)

        if diff1 == diff2:
            return True
        else:
            return False


class ChessMatch(object):
    """A Chess Piece class definition."""

    def __init__(self, pieces=None):
        """Constructor for the ChessMatch() class.

        Args:
            pieces (dictionary): A dictionary of pieces keyed by their positions
                on the board. Default: None

        Attributes:
            pieces (dictionary): A dictionary of pieces keyed by their positions
                on the board.
            log (list): A list that stores tuples of information about each
                move this piece has taken.
        """
        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces
            self.log = []

    def reset(self):
        """The function resets the match log and places the pieces back at their
            starting positions.

        Args:
            None.

        Returns:
            dictionary: A dictionary of pieces keyed by their positions on the
                board.
        """
        self.log = []

        rook_w1 = Rook('a1')
        rook_w2 = Rook('h1')
        rook_b1 = Rook('a8')
        rook_b2 = Rook('h8')
        bishop_w1 = Bishop('c1')
        bishop_w2 = Bishop('f1')
        bishop_b1 = Bishop('c8')
        bishop_b2 = Bishop('f8')
        king_w = King('e1')
        king_b = King('e8')

        self.pieces = {
            'Ra1': rook_w1,
            'Rh1': rook_w2,
            'Ra8': rook_b1,
            'Rh8': rook_b2,
            'Bc1': bishop_w1,
            'Bf1': bishop_w2,
            'Bc8': bishop_b1,
            'Bf8': bishop_b2,
            'Ke1': king_w,
            'Ke8': king_b
            }

    def move(self, piece, destination):
        """The function will move the chess piece to a new destination.

        Args:
            piece (string): The name of the piece in Full Notation.
            destination (string): The destination coordinate in short notation.

        Returns:
            tuple: Returns tuple of the old position, new position, and
                timestamp, or False if new move is not legal.
        """
        temp_prefix = piece[0]

        chess_object = self.pieces[piece]

        if temp_prefix == 'R':
            temp_tuple = Rook.move(chess_object, destination)
        elif temp_prefix == 'B':
            temp_tuple = Bishop.move(chess_object, destination)
        elif temp_prefix == 'K':
            temp_tuple = King.move(chess_object, destination)
        else:
            return False

        if temp_tuple is False:
            return False
        else:
            self.log.append(temp_tuple)
            new_key = temp_prefix + destination
            self.pieces[new_key] = self.pieces.pop(piece)

    def __len__(self):
        """A Magic Method for the ChessMatch() class to return the number of log
            items.

        Args:
            None.

        Returns:
            integer: Returns the number of log items.

        Examples:
            >>> len(match)
            1
        """
        return len(self.log)
