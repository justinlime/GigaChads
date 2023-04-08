from os import listdir

directory = "gigachads"
files = [i for i in listdir(directory)]

filenames = ",\n    ".join(files)
gigalist = f"""$a
  [
    {filenames}
  ]
$b""".replace("$a", "{").replace("$b", "}")

with open("gigalist.json", "w") as f:
    f.write(gigalist)
