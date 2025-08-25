from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
# def overfishedAnywhere(world: World, state: CollectionState, player: int):
#     """Has the player collected all fish from any fishing log?"""
#     for cat, items in world.item_name_groups:
#         if cat.endswith("Fishing Log") and state.has_all(items, player):
#             return True
#     return False

# # You can also pass an argument to your function, like {function_name(15)}
# # Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
# def anyClassLevel(state: CollectionState, player: int, level: str):
#     """Has the player reached the given level in any class?"""
#     for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
#         if state.count(item, player) >= int(level):
#             return True
#     return False

# # You can also return a string from your function, and it will be evaluated as a requires string.
# def requiresMelee():
#     """Returns a requires string that checks if the player has unlocked the tank."""
#     return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"

def change_victory(world: World):
    """Edits the modules required for victory depending on the bomb."""
    mission = world.options.bomb_mission.value
    modules_required = []

    for category in ["Centurion Module", "Praetorian Module", "OWAE Module"][0:mission+1]:
        modules_required.extend([
            name for name, l in world.item_name_to_item.items()
                if category in l.get('category', [])
        ])

    # Time Keeper
    if "The Time Keeper" in modules_required and not world.options.enable_timekeeper_check.value:
        modules_required.remove("The Time Keeper")

    logic = "|" + "| AND |".join(modules_required) + "|"
    return logic

def swan_logic(world: World):
    """Calculates the number of modules needed to solve The Swan (~40%)"""
    mission = world.options.bomb_mission.value

    match mission:
        case 0:
            return ""
        case 1:
            return "|@Regular Module:65|" # 161 * 0.4
        case 2:
            return "|@Regular Module:95|" # 236 * 0.4