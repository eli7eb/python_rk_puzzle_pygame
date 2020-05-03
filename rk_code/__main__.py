from rk_code.rk_settings.rk_control import *
from rk_code.rk_states.rk_game_menu import Menu
from rk_code.rk_states.interstitial import *
from rk_code.rk_states.rk_game_main_state import GameState
from rk_code.rk_data.rk_consts import *
from rk_code.rk_states.rk_game_start import StartState
from rk_code.rk_states.rk_game_menu import Options
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
settings = {
    'size': (600, 800),
    'fps': 60
}

app = Control()
state_dict = {
    'menu': Menu(),
    'game': StartState(),
    'options':Options()
}
app.setup_states(state_dict, 'menu')
app.main_game_loop()
pygame.quit()
sys.exit()
'''
puzzleGame = RKPuzzleGame("RK_PUZZLE", 600, 800)
mainMenuState = GameMenuState(puzzleGame)
gameOverState = InterstitialState(puzzleGame, GLOBAL_GAME_OVER_MSG, 5000, mainMenuState )
playGameState = PlayGameState( puzzleGame, gameOverState )
getReadyState = InterstitialState( puzzleGame, GLOBAL_GAME_GET_READY_MSG, 2000, playGameState )
mainMenuState.setPlayState( getReadyState )

puzzleGame.run(mainMenuState)
'''
