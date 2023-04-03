Pooja Mule <pmule@stevens.edu>

# Github Repo Link
https://github.com/PoojaVM/python_game

# Running instructions
1. Please download all files - itinerary.map, README.md, adventure.py
2. To execute in your command line, go to the path where these files are located and run `python adventure.py`
3. Please note that you do not have to provide second argument. The default map downloaded will be used. If you provide 2nd argument, this map will be overwritten.

# Basic commands
1. Please run `help` to know what all commands you can use to play this game.
2. All the basic verbs required by this program are in place which are - go, get, look, inventory
3. Following extensions have been implemented <br /> 1. Drop <br /> 2. Abbreviations <br /> 3. Help <br /> 4. Win and lose conditions
4. First 3 extensions are inplemented as per the directions provided in canvas.
5. Following 3 extenions are implemented
    ## Extension 1 - Drop
    ## Extension 2 - Abbreviations for verbs, directions, and items
    ## Extension 3 - Win and lose conditions
    1. All rooms except one have troops in it.
    2. The troops can be of 3 types - air, ground, and underwater
    3. Each room contains only 1 type of troops
    4. These troops can be collected with command `collect troop_name`
    5. Each of these troops have hitpoints associated with them which are integer numbers.
    6. Player would not know the hitpoints associated with the troop while picking them.
    7. One room has the enemy.
    8. Enemey has 3 kinds of hitpoints - air, ground, and underwater
    9. Each of enemy's hitpoints are integer numbers.
    10. Player has to break any one of the three defenses of enemy to win the battle.
    11. Player can use command `attack` to attack the enemy with the troop and enemy will lose the hitpoints equivalent to troop's hitpoint from their defense.
    12. Attack can only be done in the room where enemy is present.
    13. If player loses their hitpoints before completely removing the enemy defense, they lose.
    14. In this particular game, there are 2 win conditions and only one loss condition</br >
        1. If players have collected ground troops worth more hitpoints than enemy's ground hitpoints, they win
        2. If players have collected underwater troops worth more hitpoints than enemy's ground hitpoints, they win
        3. In any condition, if players only have air troops they will lose since enemy has higher air hitpoints
    

# Error handling
1. If there are any issues with the map file provided (does not exist or incorrect name or incorrect path), the program will show relevant message and exit
2. All the validations mentioned in canvas are in place

# Known bugs
There are no known bugs in this program

# Note
There are more 