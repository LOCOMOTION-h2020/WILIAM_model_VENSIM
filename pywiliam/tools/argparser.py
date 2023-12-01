"""
cmdline parser
"""

from pathlib import Path
from ast import literal_eval
from argparse import ArgumentParser, Action
import pandas as pd

from .config import read_config
from ._version import __version__


parser = ArgumentParser(
    description='WILIAM model',
    prog='pywiliam')

# getting the default values from the 'config.json' file
config = read_config()


#########################
# functions and actions #
#########################

def check_externals_file(string):
    """
    Check validity of the path passed by the user.

    Parameters
    ----------
    string: str
        relative path to the externals file

    Returns
    -------
    string: str
        path passed by the user.
    """

    if not string.endswith(".nc"):
        parser.error(
            f'when parsing {string}:'
            '\nThe external objects file name must be have the .nc extension')

    return string


def check_output(string):
    """
    Checks that out put file ends with tab, csv or nc

    """
    if not string.endswith('.nc'):
        parser.error(
            f'when parsing {string}'
            '\nThe output file name must be a .nc file')

    return string


def split_vars(string):
    """
    Splits the arguments from new_values.
    'a=5' -> {'a': ('param', 5.)}
    'b=[[1,2],[1,10]]' -> {'b': ('param', pd.Series(index=[1,2], data=[1,10]))}
    'a:5' -> {'a': ('initial', 5.)}

    """
    try:
        if '=' in string:
            # new variable value
            var, value = string.split('=')
            type_ = 'param'

        if ':' in string:
            # initial time value
            var, value = string.split(':')
            type_ = 'initial'

        if all(char.isdigit() or char in [".", ","] for char in value.strip()):
            # value is float
            return {var.strip(): (type_, float(value))}

        # value is series
        assert type_ == 'param'
        value = literal_eval(value)
        assert len(value) == 2
        assert len(value[0]) == len(value[1])
        return {var.strip(): (type_,
                              pd.Series(index=value[0], data=value[1]))}

    except Exception:
        parser.error(
                f'when parsing {string}:'
                '\nYou must use variable=new_value to redefine values or '
                'variable:initial_value to define initial values.'
                'variable must be a model component, new_value can be a '
                'float or a list of two list, initial_value must be a float'
                '...\n')


class SplitVarsAction(Action):
    """
    Convert the list of split variables from new_values to a dictionary.
    [{'a': 5.}, {'b': pd.Series(index=[1, 2], data=[1, 10])}] ->
        {'a': 5., 'b': pd.Series(index=[1, 2], data=[1, 10])}
    """
    def __init__(self, option_strings, dest, **kwargs):
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        main_dict = {'param': {}, 'initial': {}}
        for var in values:
            for var_name, (type_, val) in var.items():
                main_dict[type_][var_name] = val
        setattr(namespace, self.dest, main_dict)


################
# main options #
################

parser.add_argument(
    '-v', '--version',
    action='version', version=f'wiliam model {__version__}')


parser.add_argument(
    '-n', '--fname', dest='results_fname',
    type=check_output, metavar='FILE',
    help='name of the results file, default is '
         'results_{scenario sheet}_{initial time}_{final time}'
         '_{time step}.csv')

parser.add_argument(
    '-e', '--externals', dest='external_objects',
    type=check_externals_file, metavar='FILE',
    help='path to the netCDF file where the external objects are stored')

parser.add_argument(
    '-p', '--plot', dest='plot',
    action='store_true', default=config.plot,
    help='opens the plot gui after simulation')

parser.add_argument(
    '-c', '--scen', dest='scenario_file',
    type=str, metavar='SHEET', default=str(config.model.scenario_file),
    help='scenario file path')

parser.add_argument(
    '-x', '--export', dest='export_file',
    type=str, metavar='FILE',
    help='export stateful objects states to a pickle at the end of the '
         'simulation')

parser.add_argument(
    '-b', '--headless', dest='headless',
    action='store_true', default=config.headless,
    help='headless mode  (only CLI, no GUI)')

parser.add_argument(
    '-s', '--silent', dest='silent',
    action='store_true', default=config.silent,
    help='silent mode. No user input will be required during execution. Useful'
          'when running batch simulations')


###################
# Model arguments #
###################

model_arguments = parser.add_argument_group(
    'model arguments',
    'Modify model control variables.')

model_arguments.add_argument(
    '-F', '--final-time', dest='final_time',
    default=config.model_arguments.final_time,
    action='store', type=float, metavar='VALUE',
    help='modify final year of the simulation, default is '
         f'{config.model_arguments.final_time}')

model_arguments.add_argument(
    '-T', '--time-step', dest='time_step',
    default=config.model_arguments.time_step,
    action='store', type=float, metavar='VALUE',
    help='modify time step (in years) of the simulation, default is '
         f'{config.model_arguments.time_step}')

model_arguments.add_argument(
    '-S', '--saveper', dest='return_timestamp',
    default=config.model_arguments.return_timestamp,
    action='store', type=float, metavar='VALUE',
    help='modify time step (in years) of the output, default is '
         f'{config.model_arguments.return_timestamp} year')


#######################
# Warnings and errors #
#######################

warn_err_arguments = parser.add_argument_group(
    'warning and errors arguments',
    'Modify warning and errors management.')

warn_err_arguments.add_argument(
    '--missing-values', dest='missing_values', default=config.missing_values,
    action='store', type=str, choices=['warning', 'raise', 'ignore', 'keep'],
    help='exception with missing values, \'warning\' (default) shows a '
         'warning message and interpolates the values, \'raise\' raises '
         'an error, \'ignore\' interpolates the values without showing '
         'anything, \'keep\' keeps the missing values')


########################
# Positional arguments #
########################

parser.add_argument('new_values',
                    metavar='variable=new_value', type=split_vars,
                    nargs='*', action=SplitVarsAction,
                    help='redefine the value of variable with new value.'
                    'variable must be a model component, new_value can be a '
                    'float or a a list of two list')

# The destionation new_values2 will never be used as the previous argument
# is given also with nargs='*'. Nevertheless, the following variable
# is declared for documentation
parser.add_argument('new_values2',
                    metavar='variable:initial_value', type=split_vars,
                    nargs='*', action=SplitVarsAction,
                    help='redefine the initial value of variable.'
                    'variable must be a model stateful element, initial_value'
                    ' must be a float')


#########
# Usage #
#########

parser.usage = parser.format_usage().replace(
    "usage: wiliam", "python run.py")
