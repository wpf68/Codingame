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

int main()
{
    string lon;
    cin >> lon; cin.ignore();
    string lat;
    cin >> lat; cin.ignore();
    int n;
    cin >> n; cin.ignore();

    float                           dist = -1.0;
    string                          itdist;
    size_t                          i;

    i = lon.find(',');
    if (i != std::string::npos)
        lon.replace(i, 1, ".");
    float   xA = std::stof(lon);

    i = lat.find(',');
    if (i != std::string::npos)
        lat.replace(i, 1, ".");
    float   yA = std::stof(lat);

    array<string, 6>  entree;
    vector<array<string,6>>  data;

    for (int i = 0; i < n; i++) {
        string defib;
        size_t  pos;
        
        int at = 0;
        getline(cin, defib);

        for (int j = 5; j > -1; j--)
        {
            pos = defib.rfind(";");
            entree[j] =  defib.substr(pos + 1);
            defib = defib.substr(0, pos);
        }
        data.push_back(entree);
    }

    float   xB, yB, x, y, d;

    for(std::vector<array<string,6>>::iterator it = data.begin(); it != data.end(); it++)
    {
        i = it->at(4).find(',');
        if (i != std::string::npos)
        {
            it->at(4).replace(i, 1, ".");
        }
        float   xB = std::stof(it->at(4));

        i = it->at(5).find(',');
        if (i != std::string::npos)
        {
            it->at(5).replace(i, 1, ".");
        }
        float   yB = std::stof(it->at(5));

        x = (xB - xA) * cos((yA + yB) / 2); 
        y = (yB - yA);
        d = sqrt(x * x + y * y) * 6371;

        if (dist < 0 || d < dist)
        {
            dist = d;
            itdist = it->at(1);
        }

    }
    cout << itdist << endl;
}