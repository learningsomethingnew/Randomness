                            ##############################################################
                            # File last modified on: 04/11/2016
                            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                            ##############################################################

                            from random import randint, choice


                            class MontyHall:
                                def __init__(self):
                                    # track the wins and loses to report out at end of sim.
                                    self.wins = 0
                                    self.lossers = 0

                                    self.auto_door_swap = 0

                                def game_loop_with_player(self):
                                    self.reset_game()
                                    print("Winning door: ", self.winning_door)
                                    self.player_door_selection = int(input("Which door would you "
                                                                  "like to select?\n >>>"))

                                    self.starting_door_list.remove(self.player_door_selection)
                                    print("Door list with player choice removed: ", self.starting_door_list)

                                    zonk_door = self.choose_zonk_door()
                                    self.player_selection_list.remove(zonk_door)

                                    print("Door {} is a ZONK!".format(zonk_door))

                                    self.player_swap_input = int(input("Do you want to swap or stay? "
                                                                  "(1) to swap or (2) to stay.\n>>>"))

                                    if self.player_swap_input == 1:
                                        self.player_selection_list.remove(self.player_door_selection)
                                        self.player_door_selection = self.player_selection_list[0]


                                    if self.winning_door == self.player_door_selection:
                                        self.wins += 1
                                        print("You Won!")
                                    else:
                                        self.lossers += 1
                                        print("You Lose")

                                    self.show_win_loss_ratio()

                                def game_loop_automation(self, a_swap):
                                    self.reset_game()

                                    #print("Winning door: ", self.winning_door)

                                    self.player_door_selection = self.get_rand_int()
                                    #print("automation choice for door: ", self.player_door_selection)

                                    self.starting_door_list.remove(self.player_door_selection)
                                    #print("Door list with player choice removed: ", self.starting_door_list)

                                    zonk_door = self.choose_zonk_door()
                                    self.player_selection_list.remove(zonk_door)
                                    #print("Door {} is a ZONK!".format(zonk_door))

                                    self.player_swap_input = self.get_swap_choice(a_swap)

                                    if self.player_swap_input == 1:
                                        self.auto_door_swap +=1
                                        self.player_selection_list.remove(self.player_door_selection)
                                        self.player_door_selection = self.player_selection_list[0]

                                    if self.winning_door == self.player_door_selection:
                                        self.wins += 1
                                        #print("You Won!")
                                    else:
                                        self.lossers += 1
                                        #print("You Lose")

                                    # self.show_win_loss_ratio()

                                """ Chooses whether to stay with the door selection(1), swap(2), or randomly choose(3)"""
                                def get_swap_choice(self, val):
                                    if val == 1:
                                        return 1
                                    elif val == 2:
                                        return 2
                                    else:
                                        return randint(1,2)


                                """When prompted, returns a rand int from n values"""
                                def get_rand_int(self):
                                    return randint(1, 3)

                                """Shows win/loss ratio"""
                                def show_win_loss_ratio(self):
                                    print("Wins: ", self.wins)
                                    print("Lossers: ", self.lossers)
                                    print("Win ratio: ", self.wins/(self.wins + self.lossers))
                                    print("Swapped doors = ", self.auto_door_swap)

                                """Remove one zonk door option"""
                                def choose_zonk_door(self):
                                    if self.winning_door in self.starting_door_list:
                                        self.starting_door_list.remove(self.winning_door)
                                        # print("Door list with winning door removed (if applicable): ",
                                        #       self.starting_door_list)
                                    zonk = choice(self.starting_door_list)
                                    return zonk

                                def go_again(self):
                                    self.again = input("\nWould you like to go again? [y/N] \n")
                                    if self.again.lower() == 'y':
                                        return True

                                """Closes the doors and rests the winning door"""
                                def reset_game(self):
                                    self.starting_door_list = [1, 2, 3]
                                    self.player_selection_list = [1, 2, 3]
                                    self.winning_door = self.get_rand_int()

                                def reset_wins_and_lossers(self):
                                    self.wins = 0
                                    self.lossers = 0
                                    self.auto_door_swap = 0

                                def main(self):

                                    for i in range(1000):
                                        print("Loop Process ", i)
                                        self.game_loop_automation(1)
                                    print("\nSwap:")
                                    self.show_win_loss_ratio()
                                    self.reset_wins_and_lossers()

                                    for i in range(1000):
                                        self.game_loop_automation(2)
                                    print("\nStay:")
                                    self.show_win_loss_ratio()
                                    self.reset_wins_and_lossers()

                                    for i in range(1000):
                                        self.game_loop_automation(3)
                                    print("\nRandom:")
                                    self.show_win_loss_ratio()

                                #ask player if they want to play again




                            if __name__ == '__main__':
                                f = MontyHall()
                                f.main()



                            #########################################################################################
                            #                                      Old Code
                            #########################################################################################
