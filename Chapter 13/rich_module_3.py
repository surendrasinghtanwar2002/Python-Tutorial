                                                ## How to use Tree in Rich ##
from rich.tree import Tree
from rich import print as rprint

tree = Tree("Family Tree")          ##This is the head of the tree
tree.add("Father")
tree.add("Mother")
tree.add("Brother").add("Sister").add("Elder Sister")
tree.add("[green]Sister").add("[red]Sister [blue]Husband").add("[blue]Sister Son")

rprint(tree)

