# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class BombMission(Choice):
    """Choose which bomb mission you are playing.
    Centurion: 101 Modules
    Praetorian: 161 Modules
    One With Absolutely Everything: 236 Modules"""
    option_centurion = 0
    option_praetorian = 1
    option_owae = 2
    default = 0

class NumberOfStartingModules(Range):
    """Number of Modules you start with.
    Has no effect if start_with_ttks_modules is enabled."""
    range_start = 0
    range_end = 15
    default = 6

class StartWithTTKsModules(Toggle):
    """Adds all pre keys-turned modules to the starting inventory instead of random modules.
    Recommended if playing the standard Centurion/Praetorian with TTKs on the bomb."""
    default = True

class EnableTTKCheck(Toggle):
    """Adds a check for solving Turn the Key.
    Always in logic."""
    default = False

class Enable3Vanillas(Toggle):
    """Adds a check for a third vanilla module. (Centurion Only)
    This option should be enabled if playing the No-Needy Centurion, otherwise turn it off."""
    default = True

class EnableSwanCheck(Toggle):
    """Adds a check for solving The Swan. (Praetorian and OWAE Only)
    Only in logic after ~40% of the total module items have been received."""
    default = True

class EnableForgetEverythingCheck(Toggle):
    """Adds a check for solving Forget Everything. (OWAE Only)
    Only in logic after 100 module items have been received."""
    default = True

class StartWithTaxReturns(Toggle):
    """Adds Tax Returns to the starting inventory so it can be solved within its 10 minute time limit. (OWAE Only)
    If disabled, Tax Returns will be shuffled into the item pool (Recommended if playing on zen mode and tanking the strike)."""
    default = False

class EnableTimeKeeperCheck(Toggle):
    """Adds a check for solving The Time Keeper. (OWAE Only)
    Only in logic after receiving the Time Keeper item."""
    default = True

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["bomb_mission"] = BombMission
    options["number_of_starting_modules"] = NumberOfStartingModules
    options["start_with_ttks_modules"] = StartWithTTKsModules
    options["enable_ttk_check"] = EnableTTKCheck
    options["enable_3rd_vanilla"] = Enable3Vanillas
    options["enable_swan_check"] = EnableSwanCheck
    options["enable_fe_check"] = EnableForgetEverythingCheck
    options["start_with_tax_returns"] = StartWithTaxReturns
    options["enable_timekeeper_check"] = EnableTimeKeeperCheck
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
