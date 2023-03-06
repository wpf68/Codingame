/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/06 18:03:29 by pwolff            #+#    #+#             */
/*   Updated: 2023/03/06 18:03:29 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

int main()
{
    int light_x; // the X position of the light of power
    int light_y; // the Y position of the light of power
    int initial_tx; // Thor's starting X position
    int initial_ty; // Thor's starting Y position
    cin >> light_x >> light_y >> initial_tx >> initial_ty; cin.ignore();

    // game loop
    while (1) {
        int remaining_turns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remaining_turns; cin.ignore();

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;


        // A single line providing the move to be made: N NE E SE S SW W or NW

        if (initial_tx == light_x)
        {
            if (initial_ty < light_y)
            {
                initial_ty++;
                cout << "S" << endl;
            }
            else
            {
                initial_ty--;
                cout << "N" << endl;
            }
        }
        else if (initial_ty == light_y)
        {
            if (initial_tx < light_x)
            {
                initial_tx++;
                cout << "E" << endl;
            }
            else
            {
                initial_tx--;
                cout << "W" << endl;
            }
        }
        else if (initial_tx < light_x)
        {
            if (initial_ty < light_y)
            {
                initial_tx++;
                initial_ty++;
                cout << "SE" << endl;
            }
            else
            {
                initial_tx++;
                initial_ty--;
                cout << "NE" << endl;
            }

        }
        else if (initial_tx > light_x)
        {
            if (initial_ty < light_y)
            {
                initial_tx--;
                initial_ty++;
                cout << "SW" << endl;
            }
            else
            {
                initial_tx--;
                initial_ty--;
                cout << "NW" << endl;
            }

        }
      //  cout << "SE" << endl;
    }
}