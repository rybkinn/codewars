import codewars_test as test
"""Your task is to make a simple class called SnakesLadders. The test cases will call the method 
play(die1, die2) independantly of the state of the game or the player turn. The variables 
die1 and die2 are the die thrown in a turn and are both integers between 1 and 6. 
The player will move the sum of die1 and die2.

1.  There are two players and both start off the board on square 0.
2.  Player 1 starts and alternates with player 2.
3.  You follow the numbers up the board in order 1=>100
4.  If the value of both die are the same then that player will have another go.
5.  Climb up ladders. The ladders on the game board allow you to move upwards and get ahead faster.
 If you land exactly on a square that shows an image of the bottom of a ladder, then you may move 
 the player all the way up to the square at the top of the ladder. (even if you roll a double).
6.  Slide down snakes. Snakes move you back on the board because you have to slide down them. 
If you land exactly at the top of a snake, slide move the player all the way to the square at 
the bottom of the snake or chute. (even if you roll a double).
7.  Land exactly on the last square to win. The first person to reach the highest square on the 
board wins. But there's a twist! If you roll too high, your player "bounces" off the last square 
and moves back. You can only win by rolling the exact number needed to land on the last square. 
For example, if you are on square 98 and roll a five, move your game piece to 100 (two moves), 
then "bounce" back to 99, 98, 97 (three, four then five moves.)
8.  If the Player rolled a double and lands on the finish square “100” without any remaining 
moves then the Player wins the game and does not have to roll again."""


class SnakesLadders():

    def __init__(self):
        self.player1 = {'name': 'Player 1', 'score': 0, 'isMove': True}
        self.player2 = {'name': 'Player 2', 'score': 0, 'isMove': False}
        self.winner = False
        self.cages_with_ladders_and_snakes = {
            2: ('ladder', 38),
            7: ('ladder', 14),
            8: ('ladder', 31),
            15: ('ladder', 26),
            16: ('snake', 6),
            21: ('ladder', 42),
            28: ('ladder', 84),
            36: ('ladder', 44),
            46: ('snake', 25),
            49: ('snake', 11),
            51: ('ladder', 67),
            62: ('snake', 19),
            64: ('snake', 60),
            71: ('ladder', 91),
            74: ('snake', 53),
            78: ('ladder', 98),
            87: ('ladder', 94),
            89: ('snake', 68),
            92: ('snake', 88),
            95: ('snake', 75),
            99: ('snake', 80),
        }

    def play(self, die1, die2):
        if self.winner:
            return 'Game over!'

        if self.player1['isMove']:
            score_sum_player1 = self.player1['score'] + die1 + die2
            if score_sum_player1 > 100:
                score_sum_player1 = 100 - (score_sum_player1 % 100)
            if score_sum_player1 in self.cages_with_ladders_and_snakes:
                self.player1['score'] = self.cages_with_ladders_and_snakes[score_sum_player1][1]
            else:
                self.player1['score'] = score_sum_player1
            if score_sum_player1 == 100:
                self.winner = True
                result = f'{self.player1["name"]} Wins!'
            else:
                result = f'{self.player1["name"]} is on square {self.player1["score"]}'
        else:
            score_sum_player2 = self.player2['score'] + die1 + die2
            if score_sum_player2 > 100:
                score_sum_player2 = 100 - (score_sum_player2 % 100)
            if score_sum_player2 in self.cages_with_ladders_and_snakes:
                self.player2['score'] = self.cages_with_ladders_and_snakes[score_sum_player2][1]
            else:
                self.player2['score'] = score_sum_player2
            if score_sum_player2 == 100:
                self.winner = True
                result = f'{self.player2["name"]} Wins!'
            else:
                result = f'{self.player2["name"]} is on square {self.player2["score"]}'
        
        if die1 != die2:
            if self.player1['isMove']:
                self.player1['isMove'] = False
                self.player2['isMove'] = True
            else:
                self.player1['isMove'] = True
                self.player2['isMove'] = False

        return result


@test.describe('Example Tests')

def example_tests():
    game = SnakesLadders()
    @test.it("Should return: 'Player 1 is on square 38'")
    def example_test_case():
        test.assert_equals(game.play(1, 1), "Player 1 is on square 38")

    @test.it("Should return: 'Player 1 is on square 44'")
    def example_test_case():
        test.assert_equals(game.play(1, 5), "Player 1 is on square 44")

    @test.it("Should return: 'Player 2 is on square 31'")
    def example_test_case():
        test.assert_equals(game.play(6, 2), "Player 2 is on square 31")

    @test.it("Should return: 'Player 1 is on square 25'")
    def example_test_case():
        test.assert_equals(game.play(1, 1), "Player 1 is on square 25")
    
    @test.it("Should return: 'Player 1 is on square 32'")
    def example_test_case():
        test.assert_equals(game.play(4, 3), "Player 1 is on square 32")
