from subprocess import run, PIPE, CalledProcessError
import shlex
from glob import glob

#  cmd = 'spam "big deal" "red robin" 123'
files = '*.txt'

cmd = "netstat -an"
file_list = glob(files)
cmd_words = shlex.split(cmd)

# windows
run(cmd_words)
print('-' * 60)

try:
    process = run(cmd_words, stdout=PIPE)
except CalledProcessError as err:
    print(err)
else:
    output = process.stdout.decode()  # decode into Python string
    lines = output.splitlines()
    for line in lines:
        if "ESTAB" in line:
            print(line)