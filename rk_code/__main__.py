from rk_code.rk_settings.rk_states_manager import *
from rk_code.rk_states.rk_game_menu import GameMenuState
from rk_code.rk_states.interstitial import *
from rk_code.rk_states.rk_game_loop import *
from rk_code.rk_data.rk_consts import *
# main game loop
# game state machine
# switch between game states
# splash screen
# main menu choices
# new game
#   choose time, theme
#   get list of possible names
#   get image randomly from series of choices
#   show split image
#   show first 4 tiles
#   let user drag and drop until done
# options
#   difficulty
# quit
# about

#
puzzleGame = RKPuzzleGame("RK_PUZZLE", 600, 800)
mainMenuState = GameMenuState(puzzleGame)
gameOverState = InterstitialState(puzzleGame, GLOBAL_GAME_OVER_MSG, 5000, mainMenuState )
playGameState = PlayGameState( puzzleGame, gameOverState )
getReadyState = InterstitialState( puzzleGame, GLOBAL_GAME_GET_READY_MSG, 2000, playGameState )
mainMenuState.setPlayState( getReadyState )

puzzleGame.run(mainMenuState)

'''
def getSearchString():
    search_string = input("tell me what to search for you puzzle ")

def getImageToParse():
    ss = input("tell me what to search for you puzzle ")


def main():
    pygame.init()
    surface = pygame.display.set_mode((600, 900))
    pygame.display.set_caption('RK puzzle')
    getSearchString()
    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


main()

'''
