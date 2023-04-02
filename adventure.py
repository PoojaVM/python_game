import sys
import json

file_name = 'ambig.map'
if len(sys.argv) == 2:
  file_name = sys.argv[1]
file = open(file_name)

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
  'go': {
    'less_words': "Sorry, you need to 'go' somewhere.",
    'more_words': "Try to specify in less words where you'd like to go. For example - 'Go west'."
  },
  'get': {
    'less_words': "Sorry, you need to 'get' something",
    'more_words': "Try to specify in less words what you'd like to get. For example - 'Get hat'."
  },
  'drop': {
    'less_words': "Sorry, you need to 'drop' something",
    'more_words': "Try to specify in less words what you'd like to drop. For example - 'Drop hat'."
  }
}
# Stores valid verbs. Value is number of words required to execute them.
# TODO - Delete if you are not using it
verbs = { 'go': 2, 'get': 2, 'drop': 2, 'look': 1, 'inventory': 1, 'quit': 1, 'help': 1 }


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

# Only comes here for verbs - go, get, drop
# TODO - Handle drop
def parse_input_helper(words):
  verb = words[0].lower()
  if len(words) == 1:
    print(f"{messages[verb]['less_words']}")
  elif len(words) > 2:
    print(f"{messages[verb]['more_words']}")
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
          print(f"Do you want to go {' or '.join(possible_choices)}")
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
          if 'items' in state['location'].keys():
            state['location']['items'].append(item_to_drop)
          else:
            state['location']['items'] = [item_to_drop]
          state['inventory'].remove(item_to_drop)
          print(f"You drop up the {item_to_drop}")
      else:
        possible_choices = list(filter(lambda item: item_to_drop in item and item.index(item_to_drop) == 0, state['inventory']))
        if len(possible_choices) == 0:
          print(f"There's no {item_to_drop} in inventory to drop.")
        elif len(possible_choices) == 1:
          item_to_drop = possible_choices[0]
          if 'items' in state['location'].keys():
            state['location']['items'].append(item_to_drop)
          else:
            state['location']['items'] = [item_to_drop]
          state['inventory'].remove(item_to_drop)
          print(f"You drop up the {item_to_drop}")
        else:
          print(f"There are multiple items to drop. Please pick one from {' '.join(possible_choices)}")

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
    elif verb == 'help':
      print("You can run the following commands:")
      for verb in verbs:
        print(f"{verb} ..." if verbs[verb] > 1 else f"{verb}")
    elif verb in ['go', 'get', 'drop']:
      noun = 'somewhere' if verb == 'go' else 'something'
      print(f"Sorry, you need to '{verb}' {noun}.")
    else:
      possible_directions = list(filter(lambda exit: verb in exit and exit.index(verb) == 0, state['location']['exits']))
      if len(possible_directions) == 1:
        parse_input(f"go {possible_directions[0]}")
      elif len(possible_directions) > 1:
        print(f"Where would you like to go out of {', '.join(possible_directions)}")

  elif verb in ['go', 'get', 'drop']:
    parse_input_helper(words)

# Shows current state of user
def parse_input(input):
  room = state['location']
  if input == '':
    view_room(room)
  else:
    # Do not do anything for look. Just show current room
    words = input.split(" ", 1)
    verb = words[0].lower()
    if verb in verbs:
      process_input(words, room)
    else:
      possible_actions = list(filter(lambda action: verb in action and action.index(verb) == 0, verbs))
      if len(possible_actions) == 0:
        print(f"Please choose actions from {', '.join(verbs)}.")
      elif len(possible_actions) == 1:
        words[0] = possible_actions[0]
        process_input(words, room)
      else:
        print(f"What would you like to do out of {', '.join(possible_actions)}?")

class QuitGameError(Exception):
  pass

def play_game():
  while state['input'] != 'quit':
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
  parse_input('')
  play_game()
except QuitGameError:
  print('Goodbye!')