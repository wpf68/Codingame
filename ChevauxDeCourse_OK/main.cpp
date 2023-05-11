/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/11 09:15:26 by pwolff            #+#    #+#             */
/*   Updated: 2023/05/11 09:15:26 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#include <set>  //  probléme car pas de doublons ==> ecart ne peut donc pas être à 0
#include <list>

int main()
{
    int             n;
    std::list<int>  puissance;
    int             ecart = -1;

    std::cin >> n; std::cin.ignore();
    for (int i = 0; i < n; i++) {
        int pi;
        std::cin >> pi; std::cin.ignore();
        puissance.push_back(pi);
    }
    puissance.sort();

    std::list<int>::iterator it = puissance.begin();
    int encours = *it;
    it++;
    for (; it != puissance.end();  it++)
    {
        int temp = *it - encours;
        encours = *it;
        if (temp < ecart || ecart == -1)
        {
            ecart = temp;
        }
    }
    std::cout << ecart << std::endl;
}