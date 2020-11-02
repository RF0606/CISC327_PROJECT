import csv
import sys
import os

status = False
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
    print('landing')


def R2():
    print('register')


def R3():
    print('login')


def R4():
    print('sell')


def R5():
    print('buy')


def R6():
    print('update')


def R7():
    print('logout')


def R8():
    print('exit')
