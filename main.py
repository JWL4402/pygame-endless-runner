from src.Game import Game

# Settings dictionary to centralize all the game parameters, such as the size
# of the screen and it's title.
settings = {
	"game_title": "Endless Runner", # ! TEMPLATE: decide on a name for the end product
	"FPS": 60,
	"screen_size": (900, 600),
	"scroll_speed": 1,
}

def main():
	game = Game(settings)
	game.start()

if __name__ == "__main__":
	main()