import sys
import json

file_name = 'battle.map'
if len(sys.argv) == 2:
  file_name = sys.argv[1]

try:
  file = open(file_name)
except FileNotFoundError:
  print('Please make sure the map file exists, is named correctly, and is located in the same path as current file.')
  sys.exit()
# Stores game map
game_engine = json.load(file)
# Stores current state of game
state = {
  'location': game_engine[0],
  'input': '',
  'action' : '',
  'inventory': []
}
# Stores messages to show in different cases while parsing input
messages = {
  'go': "Sorry, you need to 'go' somewhere.",
  'get': "Sorry, you need to 'get' something",
  'drop': "Sorry, you need to 'drop' something",
  'collect': "Sorry, you need to 'collect' something"
}
# Stores valid verbs. Value is number of words required to execute them.
# TODO - Delete if you are not using it
# verbs = { 'go': 2, 'get': 2, 'drop': 2, 'collect': 2, 'look': 1, 'inventory': 1, 'quit': 1, 'help': 1, 'attack': 1 }
verbs = ['go', 'get', 'drop', 'look', 'inventory', 'quit', 'collect', 'attack']

def view_room(room):
  # TODO - Give new line between every print
  print(f"> {room['name']}")
  print()
  print(room['desc'])
  if 'items' in room and len(list(room['items'])) > 0:
    print()
    print(f"Items: {', '.join(list(room['items']))}")
  print()
  print(f"Exits: {' '.join(list(room['exits']))}")
  print()
  if 'troops' in room and len(list(room['troops'])) > 0:
    print(f"Troops: {', '.join(list(room['troops']))}")
    print()

# Only comes here for verbs - go, get, drop
# TODO - Handle drop
def parse_input_helper(words):
  verb = words[0].lower()
  if len(words) == 1:
    print(f"{messages[verb]}")
  else:
    if verb == 'go':
      next_room = words[1].lower()
      if next_room in state['location']['exits']:
        room = game_engine[state['location']['exits'][next_room]]
        state['location'] = room
        print(f'You go {next_room}.')
        print()
        view_room(room)
      else:
        possible_choices = list(filter(lambda exit: next_room in exit and exit.index(next_room) == 0, state['location']['exits']))
        if len(possible_choices) == 0:
          print(f"There's no way to go {next_room}.")
        elif len(possible_choices) == 1:
          room = game_engine[state['location']['exits'][possible_choices[0]]]
          state['location'] = room
          print(f'You go {possible_choices[0]}')
          print()
          view_room(room)
        else:
          print(f"Do you want to go to {' or '.join(possible_choices)}")
    elif verb == 'get':
      item_to_get = words[1].lower()
      if 'items' in state['location']:
        if item_to_get in state['location']['items']:
          state['inventory'].append(item_to_get)
          state['location']['items'].remove(item_to_get)
          print(f"You pick up the {item_to_get}.")
        else:
          possible_choices = list(filter(lambda item: item_to_get in item and item.index(item_to_get) == 0, state['location']['items']))
          if len(possible_choices) == 0:
            print(f"There's no {item_to_get} anywhere.")
          elif len(possible_choices) == 1:
            item_to_get = possible_choices[0]
            state['inventory'].append(item_to_get)
            state['location']['items'].remove(item_to_get)
            print(f"You pick up the {item_to_get}.")
          else:
            if len(possible_choices) == 2:
              print(f"Did you want to get the {possible_choices[0]} or the {possible_choices[1]}")
            else:
              print(f"Did you want to get the {possible_choices[0]}, {', '.join(possible_choices[1:len(possible_choices) - 1])} or the {possible_choices[len(possible_choices) - 1]}")
      else:
        print(f"There's no {item_to_get} anywhere.")
    elif verb == 'drop':
      item_to_drop = words[1].lower()
      if item_to_drop in state['inventory']:
        # TODO - This might throw error if items array does not exist in a room. Verify.
          if 'items' in state['location']:
            state['location']['items'].append(item_to_drop)
          else:
            state['location']['items'] = [item_to_drop]
          state['inventory'].remove(item_to_drop)
          print(f"You drop the {item_to_drop}.")
      else:
        possible_choices = list(filter(lambda item: item_to_drop in item and item.index(item_to_drop) == 0, state['inventory']))
        if len(possible_choices) == 0:
          print(f"There's no {item_to_drop} in inventory to drop.")
        elif len(possible_choices) == 1:
          item_to_drop = possible_choices[0]
          if 'items' in state['location']:
            state['location']['items'].append(item_to_drop)
          else:
            state['location']['items'] = [item_to_drop]
          state['inventory'].remove(item_to_drop)
          print(f"You drop the {item_to_drop}.")
        else:
          print(f"There are multiple items to drop. Please pick one from {', '.join(possible_choices)}")
    elif verb == 'collect':
      item_to_collect = words[1].lower()
      if item_to_collect in state['location']['troops']:
        # TODO - This might throw error if items array does not exist in a room. Verify.
          if 'troops' in state:
            state['troops'][item_to_collect] = state['location']['troops'][item_to_collect]
          else:
            state['troops'] = {item_to_collect: state['location']['troops'][item_to_collect]}
          del state['location']['troops'][item_to_collect]
          print(f"Congrats! {item_to_collect} now will attack the enemy for you.")
      else:
        possible_choices = list(filter(lambda item: item_to_collect in item and item.index(item_to_collect) == 0, state['location']['troops']))
        if len(possible_choices) == 0:
          print(f"There's no {item_to_collect} to collect.")
        elif len(possible_choices) == 1:
          item_to_collect = possible_choices[0]
          if 'troops' in state:
            state['troops'][item_to_collect] = state['location']['troops'][item_to_collect]
          else:
            state['troops'] = {item_to_collect: state['location']['troops'][item_to_collect]}
          del state['location']['troops'][item_to_collect]
          print(f"Congrats! {item_to_collect} now will attack the enemy for you")
        else:
          print(f"There are multiple items to drop. Please pick one from {', '.join(possible_choices)}")

# Starts processing input to take action if verbs are valid
def process_input(words, room):
  verb = words[0].lower()
  if len(words) == 1:
    if verb == 'look':
      view_room(room)
    elif verb == 'inventory':
      if len(state['inventory']) > 0:
        print('Inventory:')
        for item in state['inventory']:
          print(f'  {item}')
      else:
        print("You're not carrying anything.")
    # Extension - Help verb
    # elif verb == 'help':
    #   print("You can run the following commands:")
    #   for verb in verbs:
    #     print(f"{verb} ..." if verbs[verb] > 1 else f"{verb}")
    elif verb in ['go', 'get', 'drop', 'collect']:
      noun = 'somewhere' if verb == 'go' else 'something'
      print(f"Sorry, you need to '{verb}' {noun}.")
    elif verb == 'attack':
      if 'enemy' not in state['location']:
        print("You can't fight in this room. The enemy is in some other room.")
      else:
        if 'troops' not in state:
          print("Uh oh. You lost! Try gathering some defense before attacking. Better luck next time!")
          sys.exit()
        else:
          enemy_hitpoints = state['location']['enemy']
          for troop in state['troops']:
            attack_type = troop.split('_')[0]
            enemy_hitpoints[attack_type] -= state['troops'][troop]
            if enemy_hitpoints[attack_type] <= 0:
              print(f"Hurray! You broke enemy's {attack_type} defense and won!!! Goodbye!")
              sys.exit()
          print("Uh oh. You lost! Better luck next time!")
          sys.exit()

  elif verb in ['go', 'get', 'drop', 'collect']:
    parse_input_helper(words)

# Shows current state of user
def parse_input(input):
  room = state['location']
  if input != '':
    input = input.lower()
    input = " ".join(input.split())
    words = input.split(" ", 1)
    verb = words[0].lower()
    if verb in verbs:
      process_input(words, room)
    else:
      possible_actions = list(filter(lambda action: verb in action and action.index(verb) == 0, verbs))
      if len(possible_actions) == 0:
        print(f"Please pick an action out of {', '.join(verbs)}.")
        # Extesion - Directions become verbs
        # possible_exits = list(filter(lambda exit: verb in exit and exit.index(verb) == 0, state['location']['exits']))
        # if verb in state['location']['exits']:
        #   process_input(['go', possible_exits[0]], room)
        # elif len(possible_exits) == 0:
        #   print(f"Please choose actions from {', '.join(verbs)}.")
        # elif len(possible_exits) == 1:
        #   process_input(['go', possible_exits[0]], room)
        # else:
        #   print(f"Where would you like to go out of {', '.join(possible_exits)}")
      elif len(possible_actions) == 1:
        words[0] = possible_actions[0]
        process_input(words, room)
      else:
        print(f"What would you like to do out of {', '.join(possible_actions)}?")

# Custom exception class when player types 'quit'
class QuitGameError(Exception):
  pass

# Main method
def play_game():
  while state['input'].lower() != 'quit':
    try:
      state['input'] = input('What would you like to do? ')
      if state['input'].lower() != 'quit':
        parse_input(state['input'])
    except EOFError:
      print("Use 'quit' to exit.")
      continue
  raise QuitGameError()

# Driver code
try:
  view_room(state['location'])
  play_game()
except QuitGameError:
  print('Goodbye!')