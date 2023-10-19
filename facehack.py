try:
    import requests, json, re, os, random, binascii 
    from rich import print
    from rich.console import Console
    from requests.exceptions import RequestException
except (Exception, KeyboardInterrupt) as a:
    exit(str(a))

       
def banner():
    os.system(
        'cls' if os.name == 'nt' else 'clear'
    )
    print("""
[bold white]  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣶⣶⣿⣷⣆⠀⠀⠀⠀
[bold white]  ⠀⠀⠀⢀⣤⣤⣶⣶⣾⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⡆⠀ ⠀     [bold red]__                __        
[bold white]  ⠀⢀⣴⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠀⠀⠀⣿⣿⣿⣿⣷⠀ ⠀⠀   [bold red]/ /_  ____  ____  / /__     
[bold white]  ⣠⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⢤⣶⣾⠿⢿⣿⣿⣿⣿⣇  ⠀⠀ [bold red]/ __ \/ __ \/ __ \/ //_/
[bold white]  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠈⠉⠀⠀⠀⣿⣿⣿⣿⣿⡆   [bold red]/ /_/ / /_/ / /_/ / ,< 
[bold white]  ⢸⣿⣿⣿⣏⣿⣿⣿⣿⣿⣷⠀⠀⢠⣤⣶⣿⣿⣿⣿⣿⣿⣿⡀ [bold red]/_.___/\____/\____/_/|_| [bold white]v1.0.2        
[bold white]  ⠀⢿⣿⣿⣿⡸⣿⣿⣿⣿⣿⣇⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣧     
[bold white]  ⠀⠸⣿⣿⣿⣷⢹⣿⣿⣿⣿⣿⣄⣀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿   [bold yellow]© [bold green]2023[bold white] code by whoiskangprof?
[bold white]  ⠀⠀⢻⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿     Advance tool for hacking an
[bold white]  ⠀⠀⠘⣿⣿⣿⣿⠘⠻⠿⢛⣛⣭⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿     facebook hacking 🔐 ([bold yellow]BETA[bold white])
[bold white]  ⠀⠀⠀⢹⣿⣿⠏⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋
[bold white]  ⠀⠀⠀⠈⣿⠏⠀⣰⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠀⠀⠀⠀⠀   [bold yellow]®[bold white] Payload by @iqbalmh18
[bold white]  ⠀⠀⠀⠀⠀⠀⢠⡿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
  """)
              
def terminal_size():
    if int(re.search('columns=(\d+),', str(os.get_terminal_size())).group(1)) < 60:
        Console(width = 60)
        print("[bold red]Your terminal is over size, try pinching the terminal a little!!")
        exit()
         
if __name__ == '__main__':
    try:
        terminal_size()
        banner()
        print("\n\n [bold white]Sorry, this tool is still in the development stage [bold yellow]BETA\n [bold white]see you 👋")
    except (KeyboardInterrupt):
        exit()           