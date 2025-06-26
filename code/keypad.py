import keypad
import board

KEY_NAMES = (
    'C','D','E','F','STORE',
    '8','9','A','B','LOAD',
    '4','5','6','7','CLEAR',
    '0','1','2','3','ENTER'
)


km = keypad.KeyMatrix(
    row_pins=(board.D5, board.D6, board.D9, board.D10),
    column_pins=(board.D11, board.D12, board.D13, board.D25, board.D24),
    columns_to_anodes = True,
)

while True:
    event = km.events.get()
    if event:
        print(
            KEY_NAMES[event.key_number],
            "pressed" if event.pressed else "released",
        )
