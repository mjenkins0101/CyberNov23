import os
import subprocess

# Define the bash commands as variables
whoami_command = "whoami"
ip_a_command = "ip a"
lshw_command = "lshw -short"

# Print description of each command
print("Running 'whoami' command:")
# Use os.system() for basic execution
os.system(whoami_command)

print("\nRunning 'ip a' command:")
# Use subprocess.run() for more flexibility
subprocess.run(ip_a_command, shell=True)

print("\nRunning 'lshw -short' command:")
# Use subprocess.Popen() for even more control
process = subprocess.Popen(lshw_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
print(stdout.decode())

# Note: The above code assumes that you are using a Unix-based system (e.g., Linux or macOS) where these commands are available in the terminal.
