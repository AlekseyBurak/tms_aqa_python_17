small = 0
big = 0
while big != 4:
    choice = input(f"What should we do?\n"
                   f"fill the small - press 1\n"
                   f"fill the big - press 2\n"
                   )
    if choice == "2":
        small = 0
        big = 5
        print(f'in small {small}L, in big {big}L')
        choice = input(f"What should we do?\n"
                       f"fill the small - press 1\n"
                       f"from big to small - press 4\n"
                       f"make big empty - press 6\n"
                       )
        while choice != "4":
            print(f'Bad way! Think better!\n'
                  f'in small {small}L, in big {big}L')
            choice = input(f"What should we do?\n"
                           f"fill the small - press 1\n"
                           f"from big to small - press 4\n"
                           f"make big empty - press 6\n"
                           )
        if choice == "4":
            small = 3
            big = 2
            print(f'in small {small}L, in big {big}L')
            choice = input(f"What should we do?\n"
                           f"fill the big - press 2\n"
                           f"from small to big - press 3\n"
                           f"make small empty - press 5\n"
                           f"make big empty - press 6\n"
                           )
            while choice != "5":
                print(f'Bad way! Think better!\n'
                      f'in small {small}L, in big {big}L')
                choice = input(f"What should we do?\n"
                               f"fill the big - press 2\n"
                               f"from small to big - press 3\n"
                               f"make small empty - press 5\n"
                               f"make big empty - press 6\n"
                               )
            if choice == "5":
                small = 0
                big = 2
                print(f'in small {small}L, in big {big}L')
                choice = input(f"What should we do?\n"
                               f"fill the small - press 1\n"
                               f"fill the big - press 2\n"
                               f"from big to small - press 4\n"
                               f"make small empty - press 5\n"
                               f"make big empty - press 6\n"
                               )
                while choice != "4":
                    print(f'Bad way! Think better!\n'
                          f'in small {small}L, in big {big}L')
                    choice = input(f"What should we do?\n"
                                   f"fill the small - press 1\n"
                                   f"fill the big - press 2\n"
                                   f"from big to small - press 4\n"
                                   f"make small empty - press 5\n"
                                   f"make big empty - press 6\n"
                                   )
                if choice == "4":
                    small = 2
                    big = 0
                    print(f'in small {small}L, in big {big}L')
                    choice = input(f"What should we do?\n"
                                   f"fill the small - press 1\n"
                                   f"fill the big - press 2\n"
                                   f"from small to big - press 3\n"
                                   f"make small empty - press 5\n"
                                   f"make big empty - press 6\n"
                                   )
                    while choice != "2":
                        print(f'Bad way! Think better!\n'
                              f'in small {small}L, in big {big}L')
                        choice = input(f"What should we do?\n"
                                       f"fill the small - press 1\n"
                                       f"fill the big - press 2\n"
                                       f"from small to big - press 3\n"
                                       f"make small empty - press 5\n"
                                       f"make big empty - press 6\n")
                    if choice == "2":
                        small = 2
                        big = 5
                        print(f'in small {small}L, in big {big}L')
                        choice = input(f"What should we do?\n"
                                       f"fill the small - press 1\n"
                                       f"from big to small - press 4\n"
                                       f"make small empty - press 5\n"
                                       f"make big empty - press 6\n"
                                       )
                        while choice != "4":
                            print(f'Bad way! Think better!\n'
                                  f'in small {small}L, in big {big}L')
                            choice = input(f"What should we do?\n"
                                           f"fill the small - press 1\n"
                                           f"from big to small - press 4\n"
                                           f"make small empty - press 5\n"
                                           f"make big empty - press 6\n"
                                           )
                        if choice == "4":
                            small = 3
                            big = 4
                            print(f'in small {small}L, in big {big}L')
    elif choice == "1":
        small = 3
        big = 0
        print(f'in small {small}L, in big {big}L')
        choice = input(f"What should we do?\n"
                       f"fill the big - press 2\n"
                       f"from small to big - press 3\n"
                       f"make small empty - press 5\n"
                       )
        while choice != "3":
            print(f'Bad way! Think better!\n'
                  f'in small {small}L, in big {big}L')
            choice = input(f"What should we do?\n"
                           f"fill the big - press 2\n"
                           f"from small to big - press 3\n"
                           f"make small empty - press 5\n"
                           )
        if choice == "3":
            small = 0
            big = 3
            print(f'in small {small}L, in big {big}L')
            choice = input(f"What should we do?\n"
                           f"fill the small - press 1\n"
                           f"from big to small - press 4\n"
                           f"make big empty - press 6\n"
                           )
            while choice != "1":
                print(f'Bad way! Think better!\n'
                      f'in small {small}L, in big {big}L')
                choice = input(f"What should we do?\n"
                               f"fill the small - press 1\n"
                               f"from big to small - press 4\n"
                               f"make big empty - press 6\n"
                               )
            if choice == "1":
                small = 3
                big = 3
                print(f'in small {small}L, in big {big}L')
                choice = input(f"What should we do?\n"
                               f"fill the big - press 2\n"
                               f"from small to big - press 3\n"
                               f"make small empty - press 5\n"
                               f"make big empty - press 6\n"
                               )
                while choice != "3":
                    print(f'Bad way! Think better!\n'
                          f'in small {small}L, in big {big}L')
                    choice = input(f"What should we do?\n"
                                   f"fill the big - press 2\n"
                                   f"from small to big - press 3\n"
                                   f"make small empty - press 5\n"
                                   f"make big empty - press 6\n"
                                   )
                if choice == "3":
                    small = 1
                    big = 5
                    print(f'in small {small}L, in big {big}L')
                    choice = input(f"What should we do?\n"
                                   f"fill the small - press 1\n"
                                   f"from big to small - press 4\n"
                                   f"make small empty - press 5\n"
                                   f"make big empty - press 6\n"
                                   )
                    while choice != "6":
                        print(f'Bad way! Think better!\n'
                              f'in small {small}L, in big {big}L')
                        choice = input(f"What should we do?\n"
                                       f"fill the small - press 1\n"
                                       f"from big to small - press 4\n"
                                       f"make small empty - press 5\n"
                                       f"make big empty - press 6\n"
                                       )
                    if choice == "6":
                        small = 1
                        big = 0
                        print(f'in small {small}L, in big {big}L')
                        choice = input(f"What should we do?\n"
                                       f"fill the small - press 1\n"
                                       f"from small to big - press 3\n"
                                       f"from big to small - press 4\n"
                                       f"make small empty - press 5\n"
                                       f"make big empty - press 6\n"
                                       )
                        while choice != "3":
                            print(f'Bad way! Think better!\n'
                                  f'in small {small}L, in big {big}L')
                            choice = input(f"What should we do?\n"
                                           f"fill the small - press 1\n"
                                           f"fill the big - press 2\n"
                                           f"from small to big - press 3\n"
                                           f"from big to small - press 4\n"
                                           f"make small empty - press 5\n"
                                           f"make big empty - press 6\n"
                                           )
                        if choice == "3":
                            small = 0
                            big = 1
                            print(f'in small {small}L, in big {big}L')
                            choice = input(f"What should we do?\n"
                                           f"fill the small - press 1\n"
                                           f"fill the big - press 2\n"
                                           f"from big to small - press 4\n"
                                           f"make big empty - press 6\n"
                                           )
                            while choice != "1":
                                print(f'Bad way! Think better!\n'
                                      f'in small {small}L, in big {big}L')
                                choice = input(f"What should we do?\n"
                                               f"fill the small - press 1\n"
                                               f"fill the big - press 2\n"
                                               f"from big to small - press 4\n"
                                               f"make big empty - press 6\n"
                                               )
                            if choice == "1":
                                small = 3
                                big = 1
                                print(f'in small {small}L, in big {big}L')
                                choice = input(f"What should we do?\n"
                                               f"fill the big - press 2\n"
                                               f"from small to big - press 3\n"
                                               f"make small empty - press 5\n"
                                               f"make big empty - press 6\n"
                                               )
                                while choice != "3":
                                    print(f'Bad way! Think better!\n'
                                          f'in small {small}L, in big {big}L')
                                    choice = input(f"What should we do?\n"
                                                   f"fill the big - press 2\n"
                                                   f"from small to big - press 3\n"
                                                   f"make small empty - press 5\n"
                                                   f"make big empty - press 6\n"
                                                   )
                                if choice == "3":
                                    small = 0
                                    big = 4
                                    print(f'in small {small}L, in big {big}L')

print("+++++++++++++\n"
      "You receive 4L of water\n"
      "+++++++++++++")


