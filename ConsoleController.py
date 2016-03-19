# Copyright 2014 Dustin Wehr
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2014.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see .
"""
ConsoleController: User interface for manually solving Anne Hoy's problems
from the console.

move: Apply one move to the given model, and print any error message
to the console.
"""

from TOAHModel import TOAHModel, Cheese, IllegalMoveError


def move(model: TOAHModel, origin: int, dest: int):
    '''
    Module method to apply one move to the given model, and print any
    error message to the console.

    model - the TOAHModel that you want to modify
    origin - the stool number (indexing from 0!) of the cheese you want
             to move
    dest - the stool number that you want to move the top cheese
            on stool origin onto.
    '''

    model.move(origin, dest)
    print(model)


class ConsoleController:

    def __init__(self: 'ConsoleController',
                 number_of_cheeses: int, number_of_stools: int):
        """
        Initialize a new 'ConsoleController'.

        number_of_cheeses - number of cheese to tower on the first stool
        number_of_stools - number of stools
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        self._model = model

    def play_loop(self: 'ConsoleController'):
        '''
        Console-based game.
        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        '''

        user_input = '1'

        while user_input != '':
            #adding a try does not stops the function where there are
            #validations
            try:
                print("What would your next move be? Enter '' to exit")
                user_input = input('')
                input_token = user_input.split(',')
                sake_of_less_space == input_token[0].isdigit()
                #check if the input is validated
                if not sake_of_less_space or not input_token[1].isdigit():
                    print('Invalid input, must be (int,int) please try again!')

                else:
                    move(self._model, int(input_token[0]), int(input_token[1]))
                    print('=' * 40)

            except IllegalMoveError:
                print('Invalid input')

if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.
    print('=' * 40)
    print('Welcome to game of TOAH')
    print("Please enter the # of cheese and # of stools in format")

    print("number of cheese, number of stools' (i.e: 3,2)")
    user_ipt = input('')
    input_token = user_ipt.split(',')

    while not input_token[0].isdigit() and not input_token[0].isdigit():
        print('Invalid input, must be (int,int), please try again!')
        print("Please enter the # of cheese and number of stools in format")
        print("number of cheese, number of stools' (i.e: 3,2)")
        user_ipt = input('')

        input_token = user_ipt.split(',')

    game = ConsoleController(int(input_token[0]), int(input_token[1]))
    print('=' * 40)
    print("Enter the moves in origin,dest format, i.e 0,1")
    game.play_loop()
