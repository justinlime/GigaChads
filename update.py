from os import os

directory = "gigachads"
filenames = i[:len(directory) + 1] for i in os.listdir(directory)

gigalist = f"""\{
  [
    {f'{i},\n' for i in in filenames}
  ]
\}"""

with open("gigalist.json", "w") as f:
    f.write(gigalist)
