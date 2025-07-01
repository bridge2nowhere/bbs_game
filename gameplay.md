# Controllers
## Payphone
- Coin Acceptor will take quarters for making calls
- Keypad will work for making calls
- Switch hook will work for hanging up from a BBS

## Marktek Delta-128 Computer System
- 20 Key kepad, 0-F, Enter, Clear, Get, Load. Arrows will be overlayed on keys
  
- Thermal Receipt Printer
- Tricolor 20x8 VFD Display
- Acoustic Coupler to connect to payphone handest

# BBS Menus
## Main Menu
1 Messages
2 Downloads
3 Node Management

## Messages Menu
1 List Messages
2 Read Messages

## Downloads Menu
1 List Files
2 Download File
3 Setup Batch Download

## Node Management
This is the interactive portion of the game. I decided not to use arrows on the pad.

# PC/NPC Attributes
- AMPlitude which is Strength of attack
- HEAT which is your health (processer temperature)

# Items
Items have an 
- index is the four digit hex (0x23ac) that the player enters to ineract with the item
- id is the names the player sees when they find an item
- true id is shown after it is identified

## Talisman - These are buffs and curses that affect the player
- +1 crit
- +2 crit
- -2 crit
- -1 power
- +1 power
- +2 power
- +3 power
- +1 heat
- +2 heat
- +3 heat
- -2 heat
- +1 shield
- +2 shield
- -1 vulnerable
- 1 turn stun
- no effect 
## Mesmers - These are castable spells that affect enemies
- 1 turn stun
- 2 turn stun
- -1 power
- -2 power
- -1 heat
- -2 heat
- +1 power
- +1 heat
- -1 vulnerable
- -2 vulnerable
- +1 shield
- break connection/deletion
- no effect
## Procedures - These are upgraded weapons.
- +1 power
- +2 power
- +3 power
- +4 power
- +1 power/+1 crit
- +2 power/+2 crit

# Enemy Classes?
Should enemies have different types?

If so we would use the first number of the index to indicate type:
1xxx
2xxx
3xxx
4xxx
5xxx
6xxx
7xxx
8xxx
9xxx
Axxx
Bxxx
Cxxx
Dxxx
Exxx
Fxxx
