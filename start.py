#To Solve Telebot Suspension problem by @xD_Shashank
import os 
import subprocess
from logging import DEBUG, INFO, basicConfig, getLogger, warning
basicConfig(format="𝐓𝐇𝐄 𝐒𝐇𝐀𝐒𝐇𝐀𝐍𝐊 [%(levelname) ✘ ⫸ 5s/%(asctime)s] ⫷ %(name)s: ⛝ %(message)s ⛝", level=INFO)
LOGS = getLogger("Helper")
os.system("git clone https://github.com/theshashankk/DARKCOBRA darkcobra")
os.chdir("darkcobra")
process = subprocess.Popen(
        ["python3", "-m", "userbot"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,)
out, er = process.communicate()
if er:
    LOGS.warning(er.decode())
print("::::::::::::::")
if out:
    LOGS.info(out.decode())
