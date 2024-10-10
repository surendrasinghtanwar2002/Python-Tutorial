                                    ## How to style your console with Rich ##

from rich.console import Console

console = Console()

def mergedict(dict_one, dict_two):
    merge_dict = dict_one | dict_two
    console.log(merge_dict,log_locals=True)


mergedict({"id":1},{"name":"surendra","age":24})