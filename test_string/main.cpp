/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/07 09:08:31 by pwolff            #+#    #+#             */
/*   Updated: 2023/03/07 10:47:34 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string>
#include <iostream>

int main()
{
    std::string name;
    int         nb;

    name = "1234567";

    for (std::string::iterator it = name.begin(); it != name.end(); it++)
        std::cout << *it;

    std::cout << std::endl;
    std::cout << std::endl;

    for (int i = 0; name[i]; i++)
        std::cout << name[i];

    std::cout << std::endl;
    std::cout << std::endl;

    for (size_t i = 0; i < name.size(); i++)
        std::cout << name.at(i);

    std::cout << std::endl;
    std::cout << std::endl;

    // suppression caractere par caractere

    while (true)
    {
        if (name.size() == 1)
            break;
        std::cin >> nb;
        std::cin.ignore();
        if (nb < 0 || nb > 9)
        {
            std::cout << "Error Value" << std::endl;
            continue;
        }
        
        size_t pos = name.find(nb + 48);
        if (pos == std::string::npos)
            std::cout << "No Value" << std::endl;
        else
        {
            std::cout << static_cast<char>(nb + 48) << " : " << pos << std::endl;
            name.erase(pos, 1);
        }
        std::cout << name << std::endl; 

    }
    
    std::cout << "dernier caractere : " << name << std::endl;

    return 0;
}