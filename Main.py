import webbrowser
import pickle


def first_time():
    try:
        prices = pickle.load(open("price_file.p", "rb"))

    except:
        print("File Created...")
        server = input("Put in your server name(all lowercase, include any dashes)\n"
                       "Two Pages will open. Use the information to answer the next questions")
        webbrowser.open_new_tab('https://theunderminejournal.com/#us/' + server + '/category/herbalism')
        webbrowser.open_new_tab('https://theunderminejournal.com/#us/' + server + '/category/alchemy')
        prices = {'Fjarn': '', 'Fox': '', 'Dream': '', 'Star': '', 'Aethril': '',
                  'Agi': '', 'Stam': '', 'Int': '', 'Str': '', 'Old': '', 'Whisper': ''}
        for key in prices:
            x = int(input("Type in the price of " + str(key)))
            prices[key] = x
        pickle.dump(prices, open('price_file.p', 'wb'))

        print("Program Starting...")
        main(prices)
    main(prices)


def main(prices):
    option = 'Z'
    while option != 'ZIBBITYZOO':
        print("--Text Menu--")
        print("A: Read off All Prices")
        print("B: Edit All Prices")
        print("C: What is best to sell?")
        print("D: Open the Undermine Journal")
        print("E: Exit")
        option = input("Which option would you like?")
        if option == 'A':
            for key,val in prices.items():
                print (key,val,'Gold')
        elif option == 'B':
            edit_all()
        elif option == 'C':
            flask_totals(prices)
        elif option == 'D':
            webbrowser.open_new_tab('https://theunderminejournal.com')
        elif option == 'E':
            print("Current Version: 0.1.0")
            quit()


def edit_all():
    print("File Created...")
    server = input("Put in your server name(all lowercase, include any dashes)\n"
                   "Two Pages will open. Use the information to answer the next questions")
    webbrowser.open_new_tab('https://theunderminejournal.com/#us/' + server + '/category/herbalism')
    webbrowser.open_new_tab('https://theunderminejournal.com/#us/' + server + '/category/alchemy')
    prices = {'Fjarn': '', 'Fox': '', 'Dream': '', 'Star': '', 'Aethril': '',
              'Agi': '', 'Stam': '', 'Int': '', 'Str': '', 'Old': '', 'Whisper': ''}
    for key in prices:
        x = int(input("Type in the price of " + str(key)))
        prices[key] = x
    pickle.dump(prices, open('price_file.p', 'wb'))
    main(prices)


def flask_totals(prices):
    agi_total = prices.get('Fjarn') * 10 + prices.get('Fox') * 10 + prices.get('Star') * 7
    int_total = prices.get('Fjarn') * 10 + prices.get('Dream') * 10 + prices.get('Star') * 7
    str_total = prices.get('Aethril') * 10 + prices.get('Fox') * 10 + prices.get('Star') * 7
    stam_total = prices.get('Aethril') * 10 + prices.get('Dream') * 10 + prices.get('Star') * 7
    old_total = prices.get('Star') + prices.get('Fjarn') * 2 + prices.get('Fox') * 2
    deadly_total = prices.get('Star') + prices.get('Fjarn') * 2 + prices.get('Dream') * 2
    if agi_total > prices.get('Agi'):
        print('Sell mats instead of Agi flasks.')
        print('Total profit =',agi_total * .9)
    if int_total > prices.get('Int'):
        print('Sell mats instead of Int flasks')
        print('Total Profit =', int_total *.9)
    if str_total > prices.get('Str'):
        print('Sell mats instead of Str flasks')
        print ('Total Profit =',str_total*.9)
    if stam_total > prices.get('Stam'):
        print('Sell mats instead of Stam flasks')
        print('Total Profit =', stam_total*.9)
    if old_total > prices.get('Old') * 1.3:
        print('Sell mats instead of Old War')
        print('Total Profit =', old_total*.9)
    if deadly_total > prices.get('Whisper') * 1.3:
        print('Sell Mats instead of Deadly Grace')
        print ('Total Profit=',deadly_total*.9)
    print('\n\n\n\n')
    print('TOTAL PROFIT IS YOUR PROFIT PER MATS NEEDED TO MAKE ONE CONSUMABLE. AH CUT INCLUDED')


first_time()
