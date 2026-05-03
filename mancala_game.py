class Player:
    def __init__(self):
        self.Holes = [4] * 6  # each player gets their own list
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
      marbles = self.current_player.Holes[hole]
      print('Current marbles ' + str(marbles))
      self.current_player.Holes[hole] = 0 # empty the hole
      # todo implement correct logic for game
      nextHole = hole
      while marbles != 0:
         nextHole += 1
         if nextHole < len(self.current_player.Holes):
             self.current_player.Holes[nextHole]  +=1
         else:
          print('next move')
         marbles -= 1

   def GameStart(self):
      while sum(self.current_player.Holes) !=0 or sum(self.other_player.Holes) !=0:
         move = input('Player ' + str(self.turn) + ', Choose a hole number (1-6)')
         print('you chose ' + move + ', player ' + str(self.turn) + ' turn.')
         self.PlayerMove(int(move) - 1)
         self.switch_turn()
         print(self.current_player.Holes)
         print(self.current_player.Mancala)
         print(self.other_player.Holes)
         print(self.other_player.Mancala)

         
g = Game()
g.GameStart()



