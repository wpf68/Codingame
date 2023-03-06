/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/06 18:24:24 by pwolff            #+#    #+#             */
/*   Updated: 2023/03/06 18:24:24 by pwolff           ###   ########.fr       */
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
 **/

int main()
{
    int hauteur_surface;
    int temp = -1;

    int surface_n; // the number of points used to draw the surface of Mars.
    cin >> surface_n; cin.ignore();
    for (int i = 0; i < surface_n; i++) {
        int land_x; // X coordinate of a surface point. (0 to 6999)
        int land_y; // Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
        cin >> land_x >> land_y; cin.ignore();
        if (temp == land_y)
            hauteur_surface = land_y;
        temp = land_y;
    }

    // game loop
    while (1) {
        int x;
        int y;
        int h_speed; // the horizontal speed (in m/s), can be negative.
        int v_speed; // the vertical speed (in m/s), can be negative.
        int fuel; // the quantity of remaining fuel in liters.
        int rotate; // the rotation angle in degrees (-90 to 90).
        int power; // the thrust power (0 to 4).
        cin >> x >> y >> h_speed >> v_speed >> fuel >> rotate >> power; cin.ignore();

        rotate = 0;
        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;

        if (y - hauteur_surface > 1000 && v_speed > -40)
            power = 0;
        else
        {
            if (v_speed <= -15)
                power = 4;
            else if (v_speed <= -10)
                power = 3;
            else if (v_speed <= -5)
                power = 2;
            else if (v_speed <= -1)
                power = 1;
            else
                power = 0;

        }
        
        
        // 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
        cout << rotate << " " << power << endl;
    }
}