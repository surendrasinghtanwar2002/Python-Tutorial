from colorama import Fore, Back, Style, init

# Initialize Colorama
init(autoreset=True)

# Print colored text
print(Fore.RED + 'This is red text')
print(Fore.GREEN + 'This is green text')
print(Fore.BLUE + 'This is blue text')

# Print colored background
print(Back.YELLOW + 'This has a yellow background')

# Reset style
print(Style.RESET_ALL + 'Back to normal text')