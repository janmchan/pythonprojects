import mancala_player as mp

class MancalaGame:
   def __init__(self):
        self.players = [mp.Player(1), mp.Player(2)]  # two players
        self.player_index = 0
   @property
   def current_player(self):
        return self.players[self.player_index]

   @property
   def other_player(self):
        return self.players[1 - self.player_index]

   def switch_turn(self):
        self.player_index = 1 - self.player_index

   def player_move(self, choice:int):
      hole = choice - 1 # change to index
      player_side = True
      marbles = self.current_player.Holes[hole]
      holes = self.current_player.Holes
      #print('Current marbles ' + str(marbles))
      holes[hole] = 0 # empty the hole
      #print('Remove marbles')
      #print(self.current_player.Holes)
      # todo implement correct logic for Game
      next_hole = hole + 1
      while marbles != 0:
         if next_hole >= mp.Player.Size and marbles > 0:
            next_hole = 0
            if player_side:
                #print('Mancala!')
                #print(self.current_player.Holes)
                self.current_player.Mancala += 1
                holes = self.other_player.Holes
                marbles -= 1
                next_hole = 0
            else:
                holes = self.current_player
         if marbles > 0:
             holes[next_hole]  +=1
             next_hole += 1
             marbles -= 1
             #print('Normal move')
             
   def print_status(self):
         print('Game of Mancala'.center(30, '#'))
         print('next player {0} Score: {1}'.format(self.current_player.Holes, self.current_player.Mancala))
         print('last player {0} Score: {1}'.format(self.other_player.Holes, self.other_player.Mancala))
   def game_start(self):
      self.print_status()
      while sum(self.current_player.Holes) !=0 or sum(self.other_player.Holes) !=0:
          try:
            move = input('Player {0}, Choose a hole number (1-6) or 0 to exit: '.format(self.current_player.Order))
            #validate input
            if move == '0':
               print('Thank you for playing')    
               return
            choice = int(move)
            if  choice < 0 or choice > mp.Player.Size:
               print("Enter a number between 1 and 6")
               continue

            self.player_move(choice)
            self.switch_turn()
            self.print_status()
          except ValueError:
              print("Enter a number between 1 and 6")         



