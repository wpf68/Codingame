/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Reverse_Minesweeper.cpp                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/24 08:10:42 by pwolff            #+#    #+#             */
/*   Updated: 2023/08/02 10:54:29 by pwolff           ###   ########.fr       */
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

void    ft_display(std::string &map, int w, int h){
    for (int y = 0; y < h; y++){
        for (int x = 0; x < w; x++){
            std::cerr << map.at(y * w + x);
        }
        std::cerr << std::endl;
    }
    std::cerr << std::endl;
}

void    ft_displayResult(std::string &map, int w, int h){
    for (int y = 0; y < h; y++){
        for (int x = 0; x < w; x++){
            std::cout << map.at(y * w + x);
        }
        std::cout << std::endl;
    }
}


int    ft_test(std::string &map, int x, int y, int w, int h){
    int count = 0;
    if (map.at(y * w + x) == 'x')
        return count;
    if (y > 0){
        if (map.at((y - 1) * w + x) == 'x')
            count++;
        if (x > 0 && map.at((y - 1) * w + x - 1) == 'x')
            count++;
        if (x < (w - 1) && map.at((y - 1) * w + x + 1) == 'x')
            count++;
    }
    if (y < (h - 1)){
        if (map.at((y + 1) * w + x) == 'x')
            count++;
        if (x > 0 && map.at((y + 1) * w + x - 1) == 'x')
            count++;
        if (x < (w - 1) && map.at((y + 1) * w + x + 1) == 'x')
            count++;
    }
    if (x > 0 && map.at(y * w + x - 1) == 'x')
        count++;
    if (x < (w - 1) && map.at(y * w + x + 1) == 'x')
        count++;

    return count;
}


void    ft_clearX(std::string &map, int w, int h){
    
    // for (int y = 0; y < h; y++){
    //     for (int x = 0; x < w; x++){
    //         if (map.at(y * w + x) == 'x')
    //             map.at(y * w + x) = '.';
    //     }
    // }

    size_t  pos;
    std::string str = ".";
    while ((pos = map.find('x')) != std::string::npos)
        map.replace(pos, 1 , str);
}


int main()
{
    int w;
    cin >> w; cin.ignore();
    int h;
    cin >> h; cin.ignore();

    std::string map = "";
    
    for (int i = 0; i < h; i++) {
        string line = "";
        getline(cin, line);
        map += line;
    }

    ft_display(map, w, h);

    for (int y = 0; y < h; y++){
        for (int x = 0; x < w; x++){
            int result = ft_test(map, x, y, w, h);
            if (result){
                map.at(y * w + x) = 48 + result;
            }
        }
    }

    ft_display(map, w, h);
    ft_clearX(map, w, h);
    ft_displayResult(map, w, h);
}