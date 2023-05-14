/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main1.cpp                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/14 09:17:42 by pwolff            #+#    #+#             */
/*   Updated: 2023/05/14 10:36:21 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

//using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/



std::string ft_display(std::string data, int len, int l, int h);
std::string ft_putChar(std::string datas, char c, int l, int h);


int main()
{
    int l;
    std::cin >> l; std::cin.ignore();
    int h;
    std::cin >> h; std::cin.ignore();
    std::string t;
    getline(std::cin, t);

    t = "ac";

    std::string datas = "";
    std::string result= "";
    int len = t.length();

    std::cerr << "L : " << l << " H : " << h << std::endl;
    std::cerr << t << "\n" << std::endl;
    for (int i = 0; i < h; i++) {
        std::string row;
        getline(std::cin, row);
        std::cerr << "h : " << i << " :: " <<  row << std::endl;
        datas += row;
    }
    std::cerr << "\n" << datas << "\n" << std::endl;
    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    // result = ft_display(datas, 27, l, h);
    // std::cerr << "\n" << result << "\n" << std::endl;



    
    for (int i = 0; i < len; i++)
    {
        result += ft_putChar(datas, t.at(i), l, h);
        std::cerr << "\nCode\n" << result << "\n" << std::endl;
        
    }
    std::string final[h];
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < l; j++)
        {
            for (int k = 0; k < len; k++)
            {
                final[i].push_back(result.at(j * k)); 
            }
        }
    }
    result = "";
    for (int i = 0; i < h; i++)
    {
        result += final[i];
    }
    std::cerr << "\nCode 2\n" << result << "\n" << std::endl;
    result = ft_display(result, len, l, h);
    std::cerr << "\n" << result << "\n" << std::endl;



    std::cout << "### \n#   \n##  \n#   \n### " << std::endl;
}

std::string ft_putChar(std::string datas, char c, int l, int h){
    std::string result = "";
    int         pos;
    if (c >= 'a' && c <= 'z')
    {
        pos = c - 'a';
    }
    else if (c >= 'A' && c <= 'Z')
    {
        pos = c - 'A';
    }
    else 
    {
        pos = 26;
    }

    //std::cerr << "\npos = " << pos << "\n" << std::endl;

    for (int i = 0; i < h; i++)
    {
        for (int j = pos * l; j < pos * l + l; j++)
        {
            result += datas.at(i * 27 * l + j);
            //std::cerr << "i = " << i << " j = " << j << "result = " << result << std::endl;
        }

    }


    return result;
}


std::string ft_display(std::string data, int len, int l, int h){
    std::string result;
    int i = 0;
    int j = 0;

    for (i = 0; i < h; i++)
    {
        for (j = 0; j < len * l; j++)
        {
            result += data.at(i * len * l + j);
        }
        result += "\n";
        std::cerr << "\n" << result << "\n" << std::endl;

    }
    

    return result;
}