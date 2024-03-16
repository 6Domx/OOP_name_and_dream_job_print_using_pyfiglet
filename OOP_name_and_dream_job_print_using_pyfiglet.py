# Psuedocode 
# 1. Create a program
# 2. It should print your name
# 3. It should print your dream job
# 4. Use fancy text designs

import pyfiglet

your_name = input("What is your name?: ")
dream_job = input("What is your dream job?: ")

your_name_print = pyfiglet.figlet_format(your_name, font = "5lineoblique")
dream_job_print = pyfiglet.figlet_format(dream_job, font = "bubble" )

print(your_name_print)
print(dream_job_print)
