import os
import subprocess


def file_size():
    process = subprocess.Popen('du -sh', shell=True, stdout=subprocess.PIPE)
    output = str(process.stdout.read())
    parsed_output = "".join([s for s in output if s.isdigit() or s == "M"])
    return f"The file size before compression: {parsed_output}"


def public_html_backup_creation():
    current_dir = os.getcwd()
    sub_dirs = next(os.walk('..'))[1]

    if "public_html" in sub_dirs:
        command = os.system(f"zip -r backup.zip {current_dir} >/dev/null 2>&1")

        print("Backup successfully created: backup.zip")


def search_replace(s1, r1):
    command = os.system(f"wp search-replace '{s1}' '{r1}' --all-tables --precise --recurse-objects")
    return "Process completed successfully. "


def css_search_replace(s2, r2):
    command = os.system(f"egrep -lRZ '{search}' . | xargs -0 -l sed -i -e 's/{s2}/{r2}/g' *.css ")


def db_backup_creation():
    command = os.system("wp db export backup.sql")


def cache_flush():
    command = os.system("wp cache flush --skip-plugins --skip-themes; wp sg purge --skip-themes; wp rewrite flush --skip-plugins --skip-themes; wp transient delete --expired --skip-plugins --skip-themes; rm -rf wp-content/cache/*; rm -rf ~/.opcache/*")
    return "Cache flushed successfully. "


print("Initiating search and replace...")

u_input1 = input("Would you like to create a database backup? - Yes / No\n")

if u_input1 == "Yes":
    db_backup_creation()
elif u_input1 == "No":
    print("No backup would be crated. Proceeding with the S&R... ")
else:
    print("Invalid input, backup would not be created! ")

print(file_size())
f_backup_input = input(
    "Would you like to create a backup of the public_html folder? - Yes / No\n"
    ).lower()

if f_backup_input == "yes" or f_backup_input == "y" or f_backup_input == "ye":
    public_html_backup_creation()
else: 
    print("Backup would not be created")

search = input("Search for (URL): ")
replace = input("Replace with (URL): ")

print(search_replace(search, replace))

user_input = input("Would you like to also replace links in the .CSS files? - Yes / No\n")

if user_input == "Yes":
    print("Loading... ")
    css_search_replace(search, replace)
    print("Process completed successfully. ")
elif user_input == "No":
    print("Closing the script. Bye-bye! ")
else:
    user_input = input("Invalid input. Please restart the script. ")

user_input = input("Would you like to flush all caching? - Yes / No\n")

if user_input == "Yes":
    print("Loading... ")
    cache_flush()
elif user_input == "No":
    print("Cache would not be flushed. \nClosing script...")
else:
    print("Invalid input, please restart the script. ")


os.system("rm -f sandr.py")

print("You are all set! ")
