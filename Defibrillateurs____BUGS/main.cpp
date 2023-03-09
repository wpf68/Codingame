/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/08 16:12:48 by pwolff            #+#    #+#             */
/*   Updated: 2023/03/08 16:12:48 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#include <cmath>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    string lon;
    cin >> lon; cin.ignore();
    string lat;
    cin >> lat; cin.ignore();
    int n;
    cin >> n; cin.ignore();

    // std::cout << "--------------------------------------------\n";
    // std::cout << "long : " << lon << " lat : " << lat << " nb : " << n << std::endl;
    // std::cout << "--------------------------------------------\n";

    float                           dist = -1.0;
    std::vector<string>::iterator   itdist;
    size_t                          i;

    i = lon.find(',');
    if (i != std::string::npos)
        lon.replace(i, 1, ".");
    float   xA = std::stof(lon);

    i = lat.find(',');
    if (i != std::string::npos)
        lat.replace(i, 1, ".");
    float   yA = std::stof(lat);

    // std::cout << "long : " << lon << " lat : " << lat << std::endl;
    // std::cout << "long : " << xA << " lat : " << yA << std::endl;
    // std::cout << "--------------------------------------------\n";

    vector<string>  datas;

    for (int i = 0; i < n; i++) {
        string defib;
        getline(cin, defib);
        datas.push_back(defib);
    }

    // for(std::vector<string>::iterator it = datas.begin(); it != datas.end(); it++)
    //     std::cout << n-- << " // " << *it << std::endl;
        
    // return 0; // ----------
    float   xB, yB, x, y, d;

    for(std::vector<string>::iterator it = datas.begin(); it != datas.end(); it++)
    {
        std::string temp = it->substr(it->find(";;") + 2);
        std::string temp2 = temp.substr(temp.find(";") + 1);
        temp.erase(temp.find(";"));

        //std::cout << temp << " -- " << temp2 << std::endl;
        
        i = temp.find(',');
       // if (i != std::string::npos)
            temp.replace(i, 1, ".");
        float   xB = std::stof(temp);

        i = temp2.find(',');
        //if (i != std::string::npos)
            temp2.replace(i, 1, ".");
        float   yB = std::stof(temp2);

        //std::cout << xB << " -- " << yB << std::endl;

        x = (xB - xA) * cos((yA + yB) / 2); 
        y = (yB - yA);
        d = sqrt(x * x + y * y) * 6371;

        if (dist < 0 || d < dist)
        {
            dist = d;
            itdist = it;
        }

        //std::cout << "d = " << d << " dist = " << dist << " it : " << *it << " itdist : " << *itdist << std::endl;

    }
    i = itdist->find(";");
    std::string temp = itdist->substr(i + 1);
    std::string temp2 = temp.substr(temp.find(";") + 1);
    temp.erase(temp.find(";"));

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << temp << endl;
}