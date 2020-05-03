from rk_code.rk_control import Control

GLOBAL_GAME_OVER_MSG = 'G A M E  O V E R !'
GLOBAL_GAME_GET_READY_MSG = 'Get Ready!'
GLOBAL_TILE_SIZE = 512
settings = {
    'size':(600,400),
    'fps' :60
}
app = Control(**settings)
state_dict = {
    'menu': Menu(),
    'game': Game()
}
app.setup_states(state_dict, 'menu')
app.main_game_loop()