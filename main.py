#morse code key
KEY = {'A':'▄ ▄▄▄','B':'▄▄▄ ▄ ▄ ▄','C':'▄▄▄ ▄ ▄▄▄ ▄','D':'▄▄▄ ▄ ▄','E':'▄','F':'▄ ▄ ▄▄▄ ▄',
       'G':'▄▄▄ ▄','H':'▄ ▄ ▄ ▄','I':'▄ ▄','J':'▄ ▄▄▄ ▄▄▄ ▄▄▄','K':'▄▄▄ ▄ ▄▄▄','L':'▄ ▄▄▄ ▄ ▄',
       'M':'▄▄▄ ▄▄▄','N':'▄▄▄ ▄','O':'▄▄▄ ▄▄▄ ▄▄▄','P':'▄ ▄▄▄ ▄▄▄ ▄', 'Q':'▄▄▄ ▄▄▄ ▄ ▄▄▄',
       'R':'▄ ▄▄▄ ▄','S':'▄ ▄ ▄','T':'▄▄▄','U':'▄ ▄ ▄▄▄','V':'▄ ▄ ▄ ▄▄▄','W':'▄ ▄▄▄ ▄▄▄',
       'X':'▄▄▄ ▄ ▄ ▄▄▄','Y':'▄▄▄ ▄ ▄▄▄ ▄▄▄','Z':'▄▄▄ ▄▄▄ ▄ ▄','1':'▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄',
       '2':'▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄','3':'▄ ▄ ▄ ▄▄▄ ▄▄▄','4':'▄ ▄ ▄ ▄ ▄▄▄','5':'▄ ▄ ▄ ▄ ▄',
       '6':'▄▄▄ ▄ ▄ ▄ ▄','7':'▄▄▄ ▄▄▄ ▄ ▄ ▄','8':'▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄','9':'▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄',
       '0':'▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄'}
power_on = True

while power_on:
    user_input = input("Type something to convert to Morse Code! Eg:SOS 😛: ")

    mose_code = ""
    try:
        #loop through the user input
        for char in user_input:
            mose_code+= KEY[char.upper()] + ' '
        print(f"Your Morse Code ➡️: {mose_code}")
    except KeyError:
        print("❌ Only characters and numbers are allowed ❌")

    bye = input("Type 'exit' to exit the program 👋: ")
    if bye == 'exit':
        power_on = False
        print("bye! 👋")