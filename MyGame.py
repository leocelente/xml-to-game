points = 0
done = False
while not done:
    r = input("You are in the Kitchen. What do you  wanna investigate?\n  [1]-Trashcan\n  [2]-Closet\n  [3]-Tiago\n  [4]-Fridge\n  [5]-Sink\n  [6]- Go Back ")
    if r == '1':#c
        while not done:
            r = input("You are in the Trashcan. What you want to do?\n  [1]-Grab Candie\n  [2]- Go Back ")
            if r == '1':#d
                r = input("What Now?\n  [1]-Check if it has the transgenic symbol\&\n  [2]- Go Back ")
                while not done:
                    if r == '1':#e
                        r = input("OK.\n  [1]- Go Back ")
                        points += 100
                        done = True
                    elif r == '2':#e-
                        done = True
                done = False
            elif r == '2':#d-
                done = True
        done = False
    elif r == '2':#c
        while not done:
            r = input("You are in the Closet. What you want to do?\n  [1]-Look Around\n  [2]- Go Back ")
            if r == '1':#d
                r = input("What Now?\n  [1]-Ok. nothing here\n  [2]- Go Back ")
                while not done:
                    if r == '1':#e
                        r = input("OK.\n  [1]- Go Back ")
                        done = True
                    elif r == '2':#e-
                        done = True
                done = False
            elif r == '2':#d-
                done = True
        done = False
    elif r == '3':#c
        while not done:
            r = input("You are in the Tiago. What you want to do?\n  [1]-Fale com ele\n  [2]- Go Back ")
            if r == '1':#d
                r = input("What Now?\n  [1]-Parabens\&\n  [2]- Go Back ")
                while not done:
                    if r == '1':#e
                        r = input("OK.\n  [1]- Go Back ")
                        points += 100
                        done = True
                    elif r == '2':#e-
                        done = True
                done = False
            elif r == '2':#d-
                done = True
        done = False
    elif r == '4':#c
        while not done:
            r = input("You are in the Fridge. What you want to do?\n  [1]-Grab Juice Bottle\n  [2]-Drink Water\n  [3]-Eat Apples\n  [4]- Go Back ")
            if r == '1':#d
                r = input("What Now?\n  [1]-Check if it's empty\n  [2]-Check if it has the transgenic symbol\&\n  [3]-Ok. now you're not thirsty\n  [4]- Go Back ")
                while not done:
                    if r == '1':#e
                        r = input("OK.\n  [1]- Go Back ")
                        done = True
                    elif r == '2':#e
                        r = input("OK.\n  [1]- Go Back ")
                        points += 100
                        done = True
                    elif r == '3':#e
                        r = input("OK.\n  [1]- Go Back ")
                        done = True
                    elif r == '4':#e-
                        done = True
                done = False
            elif r == '2':#d
                r = input("What Now?\n  [1]-Ok. now you're not thirsty\n  [2]- Go Back ")
                while not done:
                    if r == '1':#e
                        r = input("OK.\n  [1]- Go Back ")
                        done = True
                    elif r == '2':#e-
                        done = True
                done = False
            elif r == '3':#d
                r = input("What Now?\n  [1]-Ok. now you're not hungry\n  [2]- Go Back ")
                while not done:
                    if r == '1':#e
                        r = input("OK.\n  [1]- Go Back ")
                        done = True
                    elif r == '2':#e-
                        done = True
                done = False
            elif r == '4':#d-
                done = True
        done = False
    elif r == '5':#c
        while not done:
            r = input("You are in the Sink. What you want to do?\n  [1]-Look Around\n  [2]- Go Back ")
            if r == '1':#d
                r = input("What Now?\n  [1]-Ok. nothing here!\n  [2]- Go Back ")
                while not done:
                    if r == '1':#e
                        r = input("OK.\n  [1]- Go Back ")
                        done = True
                    elif r == '2':#e-
                        done = True
                done = False
            elif r == '2':#d-
                done = True
        done = False
    elif r == '6':#c-
        done = True
print("You Made:" + str(points) + " points")