"""

introduction to object creation and manipulation

using prettytable to create a table and color table to created theme based table
its creating the object and setting different values to the object
"""

from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

#table = PrettyTable()
table = ColorTable(theme=Themes.OCEAN)

# add row by row
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])

# You can add data one column at a time as well.
table.add_column("City name",
["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
1554769])
table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
869.4])

table.align = "l"
table.align["City name"] = "r"
table.align["Annual Rainfall"] = "c"

table.sortby ="Population"
print(table)