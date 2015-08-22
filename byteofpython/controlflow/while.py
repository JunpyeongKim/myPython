# while.py
# 9.2. The while Statement
# - http://www.swaroopch.com/notes/python/#_the_while_statement

number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer : '))

    if guess == number:
        print 'Congratulations, you guessed it.'
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print 'No. it is a little higher than that.'
    else:
        print 'No. it is a little lower than that.'
# an option clause.
# - is always executed unless you break out of the loop with a break statement.
else:
    print 'The while loop is over.'
    # Do anything else you want to do here
