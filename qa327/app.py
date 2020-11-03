import csv
import sys
import os
import time

status = False
user_name = 'test_name'
user_email = 'test@test.com'
user_password = '123asd'
balance = 100

userFile = open('user.csv', 'a+')
ticketFile = open('ticket.csv', 'a+')
tranFile = open('transaction.csv', 'a+')
userReader = csv.reader(userFile)
userWriter = csv.writer(userFile)
ticketReader = csv.reader(ticketFile)
ticketWriter = csv.writer(ticketFile)
tranReader = csv.reader(tranFile)
tranWriter = csv.writer(tranFile)


def main():
    # """ An example program of frontend that does
    # R1 program only accepts 'login' as key
    # R2 print valid_account_list_file's content
    # R3 write 'hmm i am a transaction.' to the transaction_summary_file
    # """
    print('Welcome the Queens ticket trade machine')
    R1()
    #
    # # for simplicity
    # # you can use argparse for sure
    # valid_account_list_file = sys.argv[1]
    # transaction_summary_file = sys.argv[2]
    #
    # # R1:
    # user_input = input('what is the key?\n')
    # if(user_input == 'login'):
    #     print('here is the content')
    #     with open(valid_account_list_file) as rf:
    #         print(rf.read())
    #     print('writing transactions...')
    #     with open(transaction_summary_file, 'w') as wf:
    #         wf.write('hmm i am a transaction.')
    #         exit
    # else:
    #     print('omg wrong key')


def R1():
    if status:
        print('Your Balance:', balance)
        input1 = input('Type your choice:\nsell  buy  update  logout\n')
        if input1 == 'sell':
            R4()
        elif input1 == 'buy':
            R5()
        elif input1 == 'update':
            R6()
        elif input1 == 'logout':
            R7()
        else:
            print('Invalid command.')
            R1()
    if not status:
        input1 = input('Type your choice:\nregister  login  exit\n')
        if input1 == 'register':
            R2()
        elif input1 == 'login':
            R3()
        elif input1 == 'exit':
            R8()
        else:
            print('Invalid command.')
            R1()


def R2():
    print('register')


def R3():
    print('login')


def R4():
    print('Selling session started successfully!')
    try:
        ticket_name, price, quantity, date = input('Please type ticket name, price, quantity, date:').split(',')
    except:
        print('Please retype!\nThe number of inputs should be 4.')
        R4()
    if not (check_ticket_name(ticket_name) and check_price(price) and check_quantity_sell(quantity) and check_date(
            date)):
        R4()
    price = eval(price)
    price = round(price, 2)
    tranWriter.writerow(['sell', user_name, ticket_name, price, quantity, date])
    print('Selling transaction was created successfully.')
    R1()


def R5():
    print('Buying session started successfully!')
    try:
        ticket_name, quantity = input('Please type ticket name, quantity:').split(',')
    except:
        print('Please retype!\nThe number of inputs should be 2.')
        R5()
    for i in ticketReader:
        if ticket_name == ticketReader[i][0]:
            price = ticketReader[i][1]
            aval_quantity = ticketReader[i][2]
    if not(check_ticket_name(ticket_name) and check_quantity_buy(price, quantity, aval_quantity)):
        R5()
    price = eval(price)
    price = round(price, 2)
    tranWriter.writerow(['sell', user_name, ticket_name, price, quantity])
    print('Buying transaction was created successfully.')
    R1()


def R6():
    print('Updating session started successfully!')
    try:
        ticket_name, price, quantity, date = input('Please type ticket name, price, quantity, date:').split(',')
    except:
        print('Please retype!\nThe number of inputs should be 4.')
        R6()
    if not (check_ticket_name(ticket_name) and check_price(price) and check_quantity_sell(quantity) and check_date(
            date)):
        R6()
    price = eval(price)
    price = round(price, 2)
    tranWriter.writerow(['sell', user_name, ticket_name, price, quantity])
    print('Updating transaction was created successfully.')
    R1()


def R7():
    print('logout')


def R8():
    userFile.close()
    ticketFile.close()
    tranFile.close()
    exit(0)


# 48-57 65-90 97-122
def check_ticket_name(ticket_name):
    if not (ticket_name.isalnum() or ticket_name.isspace()):
        print('Selling transaction was created unsuccessfully.\nPlease retype!\nTicket name should be '
              'alphanumeric-only.')
        return False
    if not (ticket_name[0].isspace() or ticket_name[len(ticket_name) - 1].isspace):
        print('Selling transaction was created unsuccessfully.\nPlease retype!\nSpace allowed only if it is not the '
              'first or the last character.')
        return False
    elif len(ticket_name) > 60:
        print('Selling transaction was created unsuccessfully.\nPlease retype!\nThe ticket name should be no longer '
              'than 60 characters.')
        return False
    return True


def check_price(price):
    if not (price.isdigit()):
        print('Selling transaction was created unsuccessfully.\nPlease retype!\nThe ticket price should be numeric.')
        return False
    price = eval(price)
    if not (10 <= price <= 100):
        print('Selling transaction was created unsuccessfully.\nPlease retype!\nThe ticket price should be of range ['
              '10, 100].')
        return False
    return True


def check_quantity_sell(quantity):
    quantity = eval(quantity)
    if not (isinstance(quantity, int)):
        print('Selling transaction was created unsuccessfully.\nPlease retype!\nThe ticket quantity should be an '
              'integer.')
        return False
    if not (0 < quantity <= 100):
        print('Selling transaction was created unsuccessfully.\nPlease retype!\nThe quantity of the tickets has to be '
              'more than 0, and less than or equal to 100.')
        return False
    return True


def check_date(date):
    try:
        time.strptime(date, "%Y%m%d")
        return True
    except:
        print('Selling transaction was created unsuccessfully.\nPlease retype!\nDate must be given in the format '
              'YYYYMMDD.')
        return False


def check_quantity_buy(price, quantity, aval_quantity):
    quantity = eval(quantity)
    aval_quantity = eval(aval_quantity)
    if not (isinstance(quantity, int)):
        print('Selling transaction was created unsuccessfully.\nPlease retype!\nThe ticket quantity should be an '
              'integer.')
        return False
    if not (0 < quantity <= aval_quantity):
        print('Selling transaction was created unsuccessfully.\nPlease retype!\nThe quantity of the tickets has to be '
              'more than 0, and less than or equal to the available quantity.')
        return False
    elif not (balance >= price * quantity * 1.35 *1.05):
        print('Selling transaction was created unsuccessfully.\nPlease retype!\nYour balance is insufficient.')
        return False
    return True
