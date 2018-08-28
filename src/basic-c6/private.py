class Game:
    def __goal(self):
        print("非公開のメソッド")

    def play(self):
        print("公開のメソッド")

game = game()
game.play()
game.__goal()
