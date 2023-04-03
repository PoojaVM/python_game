# Pooja Mule <pmule@stevens.edu>

## Github Repo Link
https://github.com/PoojaVM/python_game

## Time spent on project
36 hours approximately

## How I tested my code
1. I did a step by step testing of this program manually.
2. First I implemented the basic features and tested them.
3. I added extensions on top of that and tested them.
4. In the end, I tested the entire program with different use cases.

## Any bugs or issues you could not resolve
There are no known bugs in this program

## An example of a difficult bug which you resolved
Issue - I was having a problem in handling the EOFError exception. I was calling the driver code again when an exception occurred so the next time an exception occurred, I would get an error saying "Sn exception occurred while handling another exception."
Fix - I fixed this issue by moving it one step inside after the driver code calls the first method and I handled it there so it does bubble up and become a cycle.

## List of the three extensions chosen to implement
### Extension 1 - Abbreviations for verbs, directions, and items
1. Players can use abbreviations of verbs, directions, and items.
2. For example - `drop item` can be written as any of the above `drop i`, `drop it`, `drop ite`, `d i`, `dr i` and all other possible combinations.
3. If multiple verbs start with the same alphabet or substring, then the player is asked for confirmation. For example, if they write `g` as verb then they have to clarify further if they meant `go` or `get`.
4. Above point also applies to directions and items.
### Extension 2 - Drop
1. Players can drop items they have picked.
2. Command is `drop item_name`.
3. Players can use abbreviations as implemented in the first extension. Ex - `d k` is equivalent to `drop knife`.
### Extension 3 - Win and lose conditions
1. All rooms except one have troops in it.
2. The troops can be of 3 types - air, ground, and underwater.
3. Each room contains only 1 type of troops.
4. `collect` verb is introduced to gather troops. Command can be given as `collect troop_name`.
5. Each of these troops have hit points associated with them which are integer numbers.
6. A player would not know the hit points associated with the troop while picking them.
7. One of the rooms has the enemy.
8. Enemy has hit points allocated in each of air, ground, and underwater.
9. Each of the enemy's hit points are integer numbers.
10. Player has to break any one of the three defenses of the enemy to win the battle.
11. `attack` verb is introduced to start the battle. Players can use command `attack` to start the battle. All the troops then attack the enemy one after another in the order in which they were picked and reduce the hit points from the enemy based on their skills (air, water, and ground).
12. Attack can only be done in the room where the enemy is present.
13. If any(air, ground, water) defenses of the enemy is broken i.e., it becomes 0 or less, the player wins and the game exits after informing them.
14. If after all the player's troop attack and none of the enemy's defense (air, water, or ground) is broken, the player loses and the game exits after informing them.
15. In this particular game, there are 2 win conditions and a combination of los conditions</br >
    1. If a player has collected all ground troops, they win.
    2. If a player has collected all underwater troops, they win.
    3. Even if a player collects all air defense, they lose because the hit points are not enough to break down the enemy's defense.
    4. Any other combination where the entire ground or underwater defense is not picked, the player loses.

## Execution instructions
1. Download all files - itinerary.map, README.md, adventure.py
2. To execute in your command line, go to the path where these files are located and run `python adventure.py battle.map`.
3. Note that you do not have to provide the second argument. The default map downloaded will be used. If you provide the second argument, default map will be overwritten.

## Note
A list of more extensions can be found in following branch https://github.com/PoojaVM/python_game/tree/extra_features <br />
The list of extensions available in this branch is <br />
1. Abbreviations for verbs, directions, and items
2. A `help` verb
3. Directions as verbs
4. A `drop` verb
5. Winning and losing conditions