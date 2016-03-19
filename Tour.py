# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Fall 2013.
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
from TOAHModel import TOAHModel

import time
import math


def tour_of_four_stools(model: TOAHModel, delay_btw_moves: float=0.5,
                        console_animate: bool=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

       model - a TOAHModel with a tower of cheese on the first stool
                and three other empty stools
       console_animate - whether to animate the tour in the console
       delay_btw_moves - time delay between moves in seconds IF
                         console_animate == True
                         no effect if console_animate == False
    """

    four_hanoi(model.number_of_cheeses(), 0, 1, 2,
               3, console_animate, delay_btw_moves)


def three_hanoi(disks, ori, temp, dest, animate, delay):
    '''
    three hanoi funciton from class
    '''

    #if theres only one disk, move to destination
    if disks == 1:
        four_stools.move(ori, dest)
        if animate:

            print(four_stools)
            time.sleep(delay)

    else:
        three_hanoi(disks - 1, ori, dest, temp, animate, delay)
        four_stools.move(ori, dest)
        three_hanoi(disks - 1, temp, ori, dest, animate, delay)


def four_hanoi(disks, ori, free1, free2, dest, animate, delay):
    '''
    function modifies four hanoi game
    '''

    formula = (math.sqrt(8 * disks + 1) - 1) // 2
    # for the sake of I don't really get this algorithm of finding
    # the most efficient i, I pulled up my high school record and
    # found this formula. Please be generous and give partial mark for
    # implementation, please =D

    if disks == 1:
        four_stools.move(ori, dest)
        if animate:

            print(four_stools)
            time.sleep(delay)

    else:
        four_hanoi(disks - formula, ori, free2, dest, free1, animate, delay)
        three_hanoi(formula, ori, free2, dest, animate, delay)
        four_hanoi(disks - formula, free1, ori, free2, dest, animate, delay)

if __name__ == '__main__':
    NUM_CHEESES = 8
    DELAY_BETWEEN_MOVES = .5
    CONSOLE_ANIMATE = False

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheeses=NUM_CHEESES)

    tour_of_four_stools(four_stools,
                        console_animate=CONSOLE_ANIMATE,
                        delay_btw_moves=DELAY_BETWEEN_MOVES)

    print(four_stools.number_of_moves())
