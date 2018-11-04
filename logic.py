"""
ttt_logic
  This module contains the logic to drive a two-player Tic-Tac-Toe
  game.
"""

class ttt_logic:
    def __init__(self):
        self.NW = None
        self.N = None
        self.NE = None
        self.W = None
        self.C = None
        self.E = None
        self.SW = None
        self.S = None
        self.SE = None
        self.currentplayer = "X"

    def check_status(self):
        """
        Checks to see if either player has won or if the board is filled.  
        Returns a two-tuple in which the first component is the string
        "x" or the string "O" or the value None; the second component
        of the tuple is one of the following strings that indicates the
        Tic-Tac-Toe board's status:
          "Playing"     No one has won and a move is available
          "Win_NW_NE"   Win across top row
          "Win_W_E"     Win across middle row
          "Win_SW_SE"   Win across bottom row
          "Win_NW_SW"   Win along left colunm
          "Win_N_S"     Win along center column
          "Win_NE_SE"   Win along right column
          "Win_NW_SE"   Win from left-top corner to right-bottom 
          "Win_NE_SW"   Win from right-top corner to left-bottom 
          "Draw"        All squares filled with no winner
        The first component of the resulting tuple represents the game
        winner, and the second component of the tuple represents the
        winning configuration.  If the status component is "Playing" or
        "Draw", the winner component should be None; for example, the
        tuple ("x", "Win_NE_SE") would be a valid return value, but
        neither ("x", "Draw") nor ("O", "Playing") represents a valid
        result.
        """
        
        if self.NW == self.N and self.N == self.NE and self.N != None:
                return ( self.NW ,'Win_NW_NE')
    
        if self.NW == self.W and self.W == self.SW and self.W != None:
                return (self.NW ,'Win_NW_SW')
        
        if self.NW == self.C and self.C == self.SE and self.C != None:
                return (self.NW ,'Win_NW_SE')
            
        if self.N == self.C and self.C == self.S and self.C != None:
                return (self.N,'Win_N_S')
            
        if self.NE == self.C and self.C == self.SW and self.C != None:
                return (self.NE ,'Win_NE_SW')
            
        if self.NE == self.E and self.E == self.SE and self.E != None:
                return (self.NE, 'Win_NE_SE')
    
        if self.W == self.C and self.C == self.E and self.C != None:
                return (self.E,'Win_W_E')
            
        if self.SW == self.S and self.S == self.SE and self.S != None:
                return (self.SW, 'Win_SW_SE')
            
        if self.NW != None and self.N != None and self.NE != None and self.W != None and self.C != None and \
           self.E != None and self.SW != None and self.S != None and self.SE != None:
            return None, 'Draw'
        
        return None, 'Playing'
        
    
    
    def move(self,location):
        """
        Places the current player's mark at the given location, if possible.
        The caller must pass one of the following strings specifying
        the location:
          "NorthWest"   Top, left square
          "North"       Top, middle square
          "NorthEast"   Top, right square
          "West"        Left, middle square
          "Center"      Center square
          "East"        Right, middle square
          "SouthWest"   Bottom, left square
          "South"       Bottom, middle square
          "SouthEast"   Bottom, right square
    
        Returns True if the specified location is available (that is,
        the global variable keeping track of that position is None);
        otherwise the function returns False for an illegal move.
        If the current player makes a valid move, the function ensures
        that control passes to the other player; otherwise, the move
        function does not affect the current player.
        """
        
        if location == 'NorthWest':
            if self.NW == None:
                if self.currentplayer == 'X':
                    self.NW = 'X'
                if self.currentplayer == 'O':
                    self.NW = 'O'            
                self.change_player()
                return True
            else:
                return False
        
        if location == 'North':
            if self.N == None:
                if self.currentplayer == 'X':
                    self.N = 'X'
                if self.currentplayer == 'O':
                    self.N = 'O'            
                self.change_player()
                return True
            else:
                return False    
        
        if location == 'NorthEast':
            if self.NE == None:
                if self.currentplayer == 'X':
                    self.NE = 'X'
                if self.currentplayer == 'O':
                    self.NE = 'O'            
                self.change_player()
                return True
            else:
                return False
        
        if location == 'West':
            if self.W == None:
                if self.currentplayer == 'X':
                    self.W = 'X'
                if self.currentplayer == 'O':
                    self.W = 'O'            
                self.change_player()
                return True
            else:
                return False
        
        if location == 'Center':
            if self.C == None:
                if self.currentplayer == 'X':
                    self.C = 'X'
                if self.currentplayer == 'O':
                    self.C = 'O'            
                self.change_player()
                return True
            else:
                return False 
            
        if location == 'East':
            if self.E == None:
                if self.currentplayer == 'X':
                    self.E = 'X'
                if self.currentplayer == 'O':
                    self.E = 'O'            
                self.change_player()
                return True
            else: 
                return False
        
        if location == 'SouthWest':
            if self.SW == None:
                if self.currentplayer == 'X':
                    self.SW = 'X'
                if self.currentplayer == 'O':
                    self.SW = 'O'            
                self.change_player()
                return True
            else:
                return False
        
        if location == 'South':
            if self.S == None:
                if self.currentplayer == 'X':
                    self.S = 'X'
                if self.currentplayer == 'O':
                    self.S = 'O'            
                self.change_player()
                return True
            else:
                return False
        
        if location == 'SouthEast':
            if self.SE == None:
                if self.currentplayer == 'X':
                    self.SE = 'X'
                if self.currentplayer == 'O':
                    self.SE = 'O'            
                self.change_player()
                return True
            else:
                return False  
    
    
    def current_player(self):
        """
        Returns the player whose turn it is to move.  This allows the
        presentation to report whose turn it is.
        Return value is one of either "x" or "O".
        """
        
        if self.currentplayer == 'X':
            return "X"
        else:
            return "O"
    
    def set_player(self,new_player):
        """
        Sets the current player.  Useful for games that require the
        player to answer a question correctly before a move.  If the
        player answers incorrectly, the turn moves to the opponent.
        Valid values for new_player are "x" or "O"; any other strings
        will not change the current player.
        """
        if new_player == 'X' or new_player == 'O':
            self.change_player()
    
    
    def change_player(self):
        """
        Alternates turns between players.  x becomes O, and O becomes X.
        """
         
        player = self.current_player()
        
        if player == 'X':
            self.currentplayer = 'O'
        else:
            self.currentplayer = 'X'     
    
    
    def look(self,location):
        """
        Returns the mark at the given location.  The caller must pass 
        one of the following strings specifying the location:
          "NorthWest"   Top, left square
          "North"       Top, middle square
          "NorthEast"   Top, right square
          "West"        Left, middle square
          "Center"      Center square
          "East"        Right, middle square
          "SouthWest"   Bottom, left square
          "South"       Bottom, middle square
          "SouthEast"   Bottom, right square
    
        The function's valid return values are None, "X", or "O".
        Returns None if neither player has marked 
        the given location.  The function also returns None if the
        caller passes any string other than one of the location strings
        listed above.
        This function allows the presentation to draw the contents
        of the Tic-Tac-Toe board.
        """
        if location == "NorthWest":
            return self.NW       
        if location == "North":
            return self.N
        if location == "NorthEast":
            return  self.NE
        if location == 'West':
            return self.W
        if location == 'Center':
            return self.C
        if location == 'East':
            return self.E
        if location == 'SouthWest':
            return self.SW
        if location == 'South':
            return self.S
        if location == 'SouthEast':
            return self.SE
        if location == None:
            pass
    
    def initialize_board(self):
        """
        Make all the board locations empty and set current player to
        "x" (that is, reset the board to the start of a new game)
        """
        
        self.currentplayer = 'X'
        self.NW = None
        self.N = None
        self.NE = None
        self.W = None
        self.C = None
        self.E = None
        self.SW = None
        self.S = None
        self.SE = None
    
        pass   


if __name__ == "__main__":
    pass   #  This module is not meant to be run as a standalone program
