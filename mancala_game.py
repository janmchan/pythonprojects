class Player:
    Size = 6
    def __init__(self):
        self.Holes = [4] * self.Size   # each player gets their own list
        self.Mancala = 0

class Game:
   def __init__(self):
        self.players = [Player(), Player()]  # two players
        self.turn = 1
   @property
   def current_player(self):
        return self.players[self.turn]

   @property
   def other_player(self):
        return self.players[1 - self.turn]

   def switch_turn(self):
        self.turn = 1 - self.turn

   def IncrementTurn(self):
      if self.turn % 2 == 1:
         self.turn = 2
      else:
         self.turn = 1

   def PlayerMove(self, hole:int):
      playerSide = True
      marbles = self.current_player.Holes[hole]
      holes = self.current_player.Holes
      #print('Current marbles ' + str(marbles))
      holes[hole] = 0 # empty the hole
      #print('Remove marbles')
      print(self.current_player.Holes)
      # todo implement correct logic for game
      nextHole = hole + 1
      while marbles != 0:
         if nextHole >= Player.Size and marbles > 0:
            nextHole = 0
            if playerSide:
                #print('Mancala!')
                #print(self.current_player.Holes)
                self.current_player.Mancala += 1
                holes = self.other_player.Holes
                marbles -= 1
                nextHole = 0
            else:
                holes = self.current_player
         if marbles > 0:
             holes[nextHole]  +=1
             nextHole += 1
             marbles -= 1
             #print('Normal move')
             print(holes)
   def PrintStatus(self):
         print('---------status---------')
         print('next:' + str(self.current_player.Holes))
         print('next:' + str(self.current_player.Mancala))
         print('last:' + str(self.other_player.Holes))
         print('last:' + str(self.other_player.Mancala))
   def GameStart(self):
      self.PrintStatus()
      while sum(self.current_player.Holes) !=0 or sum(self.other_player.Holes) !=0:
         move = input('Player ' + str(self.turn) + ', Choose a hole number (1-6)')
         print('you chose ' + move + ', player ' + str(self.turn) + ' turn.')
         self.PlayerMove(int(move) - 1)
         self.switch_turn()
         self.PrintStatus()
   
         
g = Game()
g.GameStart()



