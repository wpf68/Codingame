/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main2_bug_sur_dernier_test.cpp                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/14 10:35:57 by pwolff            #+#    #+#             */
/*   Updated: 2023/05/14 10:36:16 by pwolff           ###   ########.fr       */
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



std::string ft_display(std::string data[30], int l, int h);
std::string ft_putChar(std::string datas[30], std::string t, int l, int h);


int main()
{
    int l;
    std::cin >> l; std::cin.ignore();
    int h;
    std::cin >> h; std::cin.ignore();
    std::string t;
    getline(std::cin, t);

    //t = "Pascal";

    std::string datas[30];
    std::string result= "";
    int len = t.length();

    std::cerr << "L : " << l << " H : " << h << std::endl;
    std::cerr << t << "\n" << std::endl;
    for (int i = 0; i < h; i++) {
        std::string row;
        getline(std::cin, row);
        //std::cerr << "h : " << i << " :: " <<  row << std::endl;
        datas[i] = row;
    }

    // std::cerr << "\n*** Test Datas OK ***\n" << std::endl;
    // for (int i = 0; i < h; i++)
    // {
    //     std::cerr << "Datas[" << i << "] = " << datas[i] << std::endl;
    // }
    // std::cerr << std::endl;


    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    result = ft_display(datas, l, h);
    //std::cerr << "\n" << result << "\n" << std::endl;
    std::string *resultPointer;

    result = "";

    result = ft_putChar(datas, t, l, h);


    std::cerr << "\n  ******** \n" << result << "   ********** \n" << std::endl;


    std::cout << result << std::endl;
}

std::string ft_putChar(std::string datas[30], std::string t, int l, int h){
    std::string resultfinal = "";
    std::string result[30];
    int         pos;
    char        c;
    for (int k = 0; k < t.length(); k++)
    {
        c = t.at(k);
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
                result[i].push_back(datas[i].at(j));
                //std::cerr << "i = " << i << " j = " << j << "result = " << result[i] << std::endl;
            }

        }

    }

    //std::cerr << "\n ** Resullt ** \n" << std::endl;
    for(int i = 0; i < h; i++)
    {
        resultfinal += result[i] + "\n";
        //std::cerr << result[i] << std::endl;

    }

    return resultfinal;
}


std::string ft_display(std::string data[30], int l, int h){
    std::string result;
    int i = 0;
    int j = 0;
    int len = data[0].length() / (h - 1);
    std::cerr << len << std::endl;

    for (i = 0; i < h; i++)
    {
        for (j = 0; j < len * l; j++)
        {
            result += data[i].at(j);
        }
        result += "\n";
        //std::cerr << "\n" << result << "\n" << std::endl;

    }
    

    return result;
}