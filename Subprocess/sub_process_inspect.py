from subprocess import Popen,PIPE

process = Popen(['cat','txt_file.txt'],stdout = PIPE,stderr = PIPE)

stdout,stderr = process.communicate()

print(stdout.decode())  # Will return in byte format 
print(process.returncode)

