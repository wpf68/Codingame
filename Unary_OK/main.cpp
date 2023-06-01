/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/30 17:17:43 by pwolff            #+#    #+#             */
/*   Updated: 2023/05/30 17:17:43 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


std::string toBinary(int n)
{
    std::string r = "";
    while (n != 0){
        r += ( n % 2 == 0 ? "0" : "1" );
        n /= 2;
    }
    while (r.size() < 7)
        r += "0";
    std::reverse(r.begin(), r.end());
    return r;

}

std::string ft_count(char bin, int i, std::string result)
{
    std::string count = "";
    while(i < result.size() && result.at(i) == bin)
    {
        // std::cerr << "i = " << i << std::endl;
        count += "0";
        i++;
    }
    return count;
}

int main()
{
    std::string result = "";
    std::string unary = "";
    std::string temp = "";

    std::string message;
    getline(std::cin, message);

    int i;
    int test = 0;

    i = 0;
    while(i < message.size())
    {
        test = char(message.at(i));
        result += toBinary(test);
        i++;
    }
    std::cerr << "-" << message << "-" << std::endl;
    std::cerr << "-" << result << "-" << std::endl;


    i = 0;
    while(i < result.size())
    {
        if (result.at(i) == '1')
        {
            unary += "0 ";   
        }
        else
        {
            unary += "00 ";   
        }

        temp = ft_count(result.at(i), i, result);
        unary += temp;
        i += temp.size();
        if (i < result.size())
            unary += " ";
        temp = "";
    }
    std::cout << unary << std::endl;
}