import csv


accFile = open('accounts.csv', 'r')
ticketFile = open('tickets.csv', 'r')
new_accFile = open('updated_accounts.csv', 'w+')
new_ticketFile = open('updated_tickets.csv', 'w+')
tranFile = open('transaction.csv', 'r')
accReader = list(csv.reader(accFile))
ticketReader = list(csv.reader(ticketFile))
accWriter = csv.writer(new_accFile)
ticketWriter = csv.writer(new_ticketFile)
tranReader = csv.reader(tranFile)


def main():
    register_process()
    sell_process()
    buy_process()
    update_process()
    accWriter.writerows(accReader)
    ticketWriter.writerows(ticketReader)


def register_process():
    pass


def sell_process():
    pass


def buy_process():
    pass


def update_process():
    for i in tranReader:                    # read over transactions
        if not i:
            continue
        if i[0] == 'updating':              # process updating only
            user_email = i[1]               # read transaction info
            ticket_name = i[2]
            price = i[3]
            quantity = i[4]
            for j in ticketReader:          # look for the ticket of this owner
                if ticket_name == j[0] and user_email == j[3]:
                    j[1] = price            # modify the info
                    j[2] = quantity


if __name__ == "__main__":
    main()



