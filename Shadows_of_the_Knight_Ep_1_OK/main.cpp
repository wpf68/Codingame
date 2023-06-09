/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/06/07 08:28:37 by pwolff            #+#    #+#             */
/*   Updated: 2023/06/09 10:01:36 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#include <cstdlib>

// using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

struct  Hero{
    int x;
    int y;
    int grille_HautGaucheX;
    int grille_HautGaucheY;
    int grille_BasDroiteX;
    int grille_BasDroiteY;

    int w;
    int h;
    int x0;
    int y0;

    int xBomb;
    int yBomb;
};

std::string zWake = "+";
std::string zClean = "0";
std::string pBatman = "B";
std::string pBomb = "X";


std::string ft_display(struct Hero &Batman)
{
    std::string grille = "";
    for (int i = 0; i < Batman.h; i++)
    {
        for (int j = 0; j < Batman.w; j++)
        {
            grille += zClean;
        }
        grille += "\n";
    }
    grille += "\n";

   // std::cerr << grille << std::endl;

    for (int i = Batman.grille_HautGaucheY; i <= Batman.grille_BasDroiteY; i++)
    {
        for (int j = Batman.grille_HautGaucheX; j <= Batman.grille_BasDroiteX; j++)
        {
            grille.at(i * (Batman.w + 1) + j) = zWake.at(0);
        }
    }
            //std::cerr << "*****  test ********" << std::endl;

    //std::cerr << grille << std::endl;
    


    grille.at(Batman.y0 * (Batman.w + 1) + Batman.x0) = pBatman.at(0);
    grille.at(Batman.yBomb * (Batman.w +1) + Batman.xBomb) = pBomb.at(0);
    return grille;
};



int main()
{
    srand((unsigned int)time(0));
    int coeffX = 0;
    int coeffY = 0;

    int w = 10; // width of the building.
    int h = 10; // height of the building.
    // std::cin >> w >> h; std::cin.ignore();

    std::cerr << "tab x -w- : " << w << " tab y -h- : " << h << std::endl;

    int n = 10; // maximum number of turns before game over.
    // std::cin >> n; std::cin.ignore();

    std::cerr << "Nombre de sauts -n- : " << n << std::endl;

    int x0 = w - 1;
    int y0 = 0;
    // std::cin >> x0 >> y0; std::cin.ignore();

    std::cerr << "pos x0: " << x0 << " pos y0 : " << y0 << std::endl;



    struct Hero Batman;
    Batman.x = x0;
    Batman.y = y0;
    Batman.grille_HautGaucheX = 0;
    Batman.grille_HautGaucheY = 0;
    Batman.grille_BasDroiteX = w - 1;
    Batman.grille_BasDroiteY = h - 1;

    Batman.w = w;
    Batman.h = h;

    //for (int i = 0; i < 10; i++) // test rand
    {
        Batman.xBomb = rand() % w;
        Batman.yBomb = rand() % h;


        std::cerr << "pos xBomb: " << Batman.xBomb << " pos yBomb : " << Batman.yBomb << std::endl;
    }

    x0 = rand() % w;
    y0 = rand() % h;
    // game loop
    while (1) {

        // Test
        //while (true)
        // {
        //     std::cerr << "Batman X - Y ?" << std::endl;
        //     std::cin >> x0 >> y0; std::cin.ignore();
        //     if (x0 < w && y0 < h && x0 >= 0 && y0 >= 0)
        //         break;
        // }
        // *****


        if (x0 == Batman.xBomb && y0 == Batman.yBomb)
        {
            std::cerr << "MATCH !!!!" << std::endl;
            break;
        }


        Batman.x0 = x0;
        Batman.y0 = y0;
       // std::cerr << ft_display(Batman) << std::endl;
        std::cerr << ft_display(Batman) << std::endl;
        std::string bomb_dir; // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
        
        std::cerr << "Direction bombe (U - UR - UL - D - DR - DL - R - L) ? \n" << std::endl;
        
        std::cin >> bomb_dir; std::cin.ignore();

        std::cerr << "Direction bombe : " << bomb_dir << std::endl;


        // test
            // Batman.grille_HautGaucheX = 0;
            // Batman.grille_HautGaucheY = 6;
            // Batman.grille_BasDroiteX = 2 ;
            // Batman.grille_BasDroiteY = 9 ;
            // std::cerr << ft_display(Batman) << std::endl;

        // *******

        if (bomb_dir == "U")
        {
            std::cerr << "-- U --" << std::endl;
            Batman.grille_HautGaucheX = x0;
            Batman.grille_BasDroiteX = x0;
            Batman.grille_BasDroiteY = y0 - 1;
        }
        else if (bomb_dir == "D")
        {
            std::cerr << "-- D --" << std::endl;
            Batman.grille_HautGaucheX = x0;
            Batman.grille_HautGaucheY = y0 + 1;
            Batman.grille_BasDroiteX = x0;
        }
        else if (bomb_dir == "R")
        {
            std::cerr << "-- R --" << std::endl;
            Batman.grille_HautGaucheX = x0 + 1;
            Batman.grille_HautGaucheY = y0;
            Batman.grille_BasDroiteY = y0;
        }
        else if (bomb_dir == "L")
        {
            std::cerr << "-- L --" << std::endl;
            Batman.grille_HautGaucheY = y0;
            Batman.grille_BasDroiteY = y0;
            Batman.grille_BasDroiteX = x0 - 1;
        }
        else if (bomb_dir == "UR")
        {
            std::cerr << "-- UR --" << std::endl;
            Batman.grille_HautGaucheX = x0 + 1;
            Batman.grille_BasDroiteY = y0 - 1;
        }
        else if (bomb_dir == "UL")
        {
            std::cerr << "-- UL --" << std::endl;
            Batman.grille_BasDroiteX = x0 - 1;
            Batman.grille_BasDroiteY = y0 - 1;
        }
        else if (bomb_dir == "DL")
        {
            std::cerr << "-- DL --" << std::endl;
            Batman.grille_HautGaucheY = y0 + 1;
            Batman.grille_BasDroiteX = x0 - 1;
        }
        else if (bomb_dir == "DR")
        {
            std::cerr << "-- DR --" << std::endl;
            Batman.grille_HautGaucheY = y0 + 1;
            Batman.grille_HautGaucheX = x0 + 1;
        }



        std::cerr << "Haut Gauche [" << Batman.grille_HautGaucheX << "," << Batman.grille_HautGaucheY << "]"
                << " Bas Droit [" << Batman.grille_BasDroiteX << "," << Batman.grille_BasDroiteY << "]" << std::endl;

        if (x0 < Batman.grille_HautGaucheX)
            coeffX = 1;
        else
            coeffX = -1;
        if (y0 < Batman.grille_HautGaucheY)
            coeffY = 1;
        else
            coeffY = -1;

        if (Batman.grille_HautGaucheX == Batman.grille_BasDroiteX && Batman.grille_HautGaucheY == Batman.grille_BasDroiteY)
        {
            x0 = Batman.grille_BasDroiteX;
            y0 = Batman.grille_BasDroiteY;
        }
        else
        {
            x0 = x0 + (coeffX * (Batman.grille_BasDroiteX - Batman.grille_HautGaucheX + 1) / 2) + coeffX;
            if (x0 < 0 || x0 >= w)
                x0 = x0 - coeffX;
            y0 = y0 + (coeffY * (Batman.grille_BasDroiteY - Batman.grille_HautGaucheY + 1) / 2) + coeffY;
            if (y0 < 0 || y0 >= h)
                y0 = y0 - coeffY;
        }

        // int i = 0;
        // while (i < bomb_dir.length())
        // {
        //     switch(bomb_dir[i])
        //     {
        //         case 'U':
        //             std::cerr << "-- U --" << std::endl;
        //             if (Batman.grille_BasDroiteY == -1)
        //             {
        //                 Batman.grille_HautGaucheY = 0;
        //             }
        //             Batman.grille_BasDroiteY = y0 - 1;
        //             break;
        //         case 'R':
        //             std::cerr << "-- R --" << std::endl;
        //             break;
        //         case 'D':
        //             std::cerr << "-- D --" << std::endl;
        //             if (Batman.grille_BasDroiteY == -1)
        //             {
        //                 Batman.grille_BasDroiteY = 0;
        //             }
        //             Batman.grille_BasDroiteY = y0 - 1;

        //             break;
        //         case 'L':
        //             std::cerr << "-- F --" << std::endl;
        //             break;
        //         default :
        //             std::cerr << "-- ERROR --" << std::endl;

        //     }
        //     i++;


        // }

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;


        // the location of the next window Batman should jump to.
        std::cout << "0 0" << std::endl;
    }
}