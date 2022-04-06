import os
import time
baseGit = "https://github.com/albuquerquealdry/"
arq = open("repositorys.txt")
repositorys = arq.readlines()
for repository in repositorys:
    x = repository
os.system(f"cd tmp && git clone {baseGit}{x}")
os.system(f"cd tmp/{x} && rm README.md")
os.system(f"cp ./files/README.md ./tmp/{x}")
os.system(f"""cd tmp/{x} && git add . && git commit -m "SCRIPT MIGRATION" && git push """)
os.system (f"cd tmp && rm -rf {x}")