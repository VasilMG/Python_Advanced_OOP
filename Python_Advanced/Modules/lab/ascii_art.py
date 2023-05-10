from pyfiglet import figlet_format
# from termcolor import colord 



def print_art(msg):
    art_message = figlet_format(msg)
    print(art_message)

print_art('Python 3.8')



