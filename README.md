# Pooja Mule <pmule@stevens.edu>

## Github Repo Link
https://github.com/PoojaVM/python_game

## Time spent on project
36 hours approximately

## How I tested my code
1. I did a step by step testing of this program manually.
2. First I implemented the basic features and tested them.
3. I added extensions on top of that and tested them.
4. In the end, I tested the entire program with different usecases.

## Any bugs or issues you could not resolve
There are no known bugs in this program

## An example of a difficult bug which you resolved
Issue - I was having problem in handling EOFError exception. I was calling the driver code again when exception occurs so when next time exception occurred, I would get an error saying "En exception occurred while handling another exception."
Fix - I fixed this issue by moving it one step inside after driver code calls the first method and I handled it there so it does bubble up and become a cycle.

## List of the three extensions chosen to implement
### Extension 1 - Abbreviations for verbs, directions, and items
1. Players can use abbreviation of verbs, directions, and items.
2. For example - `drop item` can be wrriten as any of the above `drop i`, `drop it`, `drop ite`, `d i`, `dr i` and all other possible combinations
3. If multiple verbs start with same alphabet or sub-string, then player is asked for confirmation. For example, if they write `g` as verb then they have to clarify further if they meant `go` or `get`
4. Above point also applies to directions and items
### Extension 2 - Drop
1. Player can drop items they have picked.
2. Command is `drop item_name`.
3. Player can use abbreviation as implemented in the first extesion. Ex - `d k` is equivalent to `drop knife`.
### Extension 3 - Win and lose conditions
1. All rooms except one have troops in it.
2. The troops can be of 3 types - air, ground, and underwater
3. Each room contains only 1 type of troops
4. `collect` verb is introduced to gather troops. Command can be given as `collect troop_name`
5. Each of these troops have hitpoints associated with them which are integer numbers.
6. Player would not know the hitpoints associated with the troop while picking them.
7. One room has the enemy.
8. Enemey has 3 kinds of hitpoints - air, ground, and underwater
9. Each of enemy's hitpoints are integer numbers.
10. Player has to break any one of the three defenses of enemy to win the battle.
11. `attack` verb is introduced to start the battle. Player can use command `attack` to start the battle. All the troops then one bye one will attack enemy and break its respective defense based on their skills.
12. Attack can only be done in the room where enemy is present.
13. If any(air, ground, water) defenses of enemy is broken i.e., it becomes 0 or less, player wins and game exits after informing them.
13. If player loses their hitpoints before completely removing the enemy defense, they lose and game exits after informing them.
14. In this particular game, there are 2 win conditions and a combination of los conditions</br >
    1. If player has collected all ground troops, they win.
    2. If player has collected all underwater troops, they win.
    3. Even if player collects all air defense, they lose because the hitpoints are not enough to break down enemy's defense.
    4. Any other combination where entire ground or underwater defense is not picked, player loses.

## Execution instructions
1. Please download all files - itinerary.map, README.md, adventure.py
2. To execute in your command line, go to the path where these files are located and run `python adventure.py itinerary.map`
3. Please note that you do not have to provide second argument. The default map downloaded will be used. If you provide 2nd argument, default map will be overwritten.

## Note
A list of more extenions can be found in following branch https://github.com/PoojaVM/python_game/tree/extra_features <br />
The list of extensions available in this branch is <br />
1. Abbreviations for verbs, directions, and items
2. A `help` verb
3. Directions as verbs
4. A `drop` verb
5. Winning and losing conditions