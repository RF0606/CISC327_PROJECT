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
    for i in tranReader: # read transaction.csv
        if not i:
            continue
        if i[0] == "selling": # process selling transaction
            #get info
            user_email = i[1]
            ticket_name = i[2]
            price = i[3]
            quantity = i[4]
            # append the selling info to ticketReader list
            ticketReader.append([ticket_name, price, quantity, user_email])





def buy_process():
    for i in tranReader:
        if not i:
            continue
        if i[0] == 'buying':
            user_email = i[1]
            ticket_name = i[2]
            price = eval(i[3])
            buyquantity = eval(i[4])
            owneremail = ''
            for j in ticketReader: # look for the ticket of this owner
                if not j:
                    continue
                if ticket_name == j[0]:
                    quantity = eval(j[2])
                    if buyquantity > quantity:
                        print('Maximum purchase quantity exceeded')
                        continue
                    if buyquantity <= quantity:
                        totalquantity = quantity - buyquantity
                        j[2] = totalquantity
                        owneremail = j[3]
            for j in accReader:
                if not j:
                    continue
                if user_email == j[0]:
                    balance = eval(j[3])
                    total_price = price * buyquantity * 1.35 * 1.05
                    balance = balance - total_price
                    j[3] = balance
            for j in accReader:
                if not j:
                    continue
                if owneremail == j[0]:
                    balance = eval(j[3])
                    total_earning = price * buyquantity
                    balance = balance + total_earning
                    j[3] = balance


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
                if not j:
                    continue
                if ticket_name == j[0] and user_email == j[3]:
                    j[1] = price            # modify the info
                    j[2] = quantity


if __name__ == "__main__":
    main()



