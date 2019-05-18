from livewires import games, color
from random import randint


games.init(screen_width=640, screen_height=480, fps=50)


class GameOver(games.Sprite):
    def __init__(self, x, y):
        super(GameOver, self).__init__(image=games.load_image("over.png"), x=x, y=y)


class Ball(games.Sprite):
    ball = games.load_image("ball.png")

    def __init__(self, bar, x, y):
        super(Ball, self).__init__(image=Ball.ball, x=x, y=y)
        self.bar = bar

    def update(self):
        self.y += 2
        if self.bar.overlaps(self):
            self.bar.score.value += 1
            ball = Ball(self.bar, x=randint(10, games.screen.width - 10), y=10)
            self.destroy()
            games.screen.add(ball)
        if self.y == games.screen.height:
            games.screen.clear()
            game_over = GameOver(games.screen.width / 2, games.screen.height / 2)
            games.screen.add(game_over)


class Bar(games.Sprite):
    bar = games.load_image("bar.png")

    def __init__(self):
        super(Bar, self).__init__(image=Bar.bar, x=games.screen.width / 2, y=games.screen.height)
        self.score = games.Text(value=0,
                                size=60,
                                right=games.screen.width - 60,
                                top=20,
                                color=color.white)
        games.screen.add(self.score)

    def update(self):
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x -= 5
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x += 5


def main():
    bg = games.load_image("fon.jpg")
    games.screen.background = bg

    bar = Bar()
    games.screen.add(bar)

    ball = Ball(bar, x=randint(10, games.screen.width - 10), y=10)
    games.screen.add(ball)
    games.screen.mainloop()


if __name__ == '__main__':
    main()
