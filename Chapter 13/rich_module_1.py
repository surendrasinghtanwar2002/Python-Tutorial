from rich import print as rprint
import os
import rich

from rich import inspect

os.system("clear")

#List Print
nums_list = [1, 2, 3, 4]
rprint(nums_list)

##Bool Print
bool_list = [True, False]
rprint(bool_list)

##Dictionary Print
nums_tuple = (1, 2, 3, 4)
nums_dict = {'nums_list': nums_list, 'nums_tuple': nums_tuple}
rprint(nums_dict)

inspect(rich)

