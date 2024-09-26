from rich.tree import Tree
from rich import print as rprint

tree = Tree("My Folder Structure")
scripts_node = tree.add("[blue]Scripts")
scripts_node.add("[red]Get Interface Details")
scripts_node.add("[blue]Get Interface Details")
scripts_node.add("[green]Get Interface Details")
scripts_node.add("[orange]Get Interface Details")
scripts_node.add("[purple]Get Interface Details")
tree.add("[blue]Components")
tree.add("[blue]Automation")

rprint(tree)