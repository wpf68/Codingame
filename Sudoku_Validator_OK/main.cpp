/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/06/16 10:28:20 by pwolff            #+#    #+#             */
/*   Updated: 2023/06/16 10:34:10 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

// using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

void    ft_Display(std::string tab[9])
{
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < tab[i].size(); j++)
        {
            std::cerr << tab[i].at(j);
            if (!((j + 1) % 3))
                std::cerr << " ";
        }
        std::cerr << std::endl;
        if (!((i + 1) % 3))
            std::cerr << std::endl;
    }
}

std::string    ft_ScreenSet(std::set<int> verif)
{

    int i = 49;
    for (std::set<int>::iterator it = verif.begin(); it != verif.end(); it++)
    {
        std::cerr << *it;
        if (*it != i++)
            return "false";

    }
    std::cerr << std::endl;

    return "true";
}

std::string ft_Test(std::string tab[9])
{
    std::set<int>   verif;
    std::string test = "true";

    verif.clear();
    for (int k = 0; k < 3; k++)
    {
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                std::cerr << ((tab[j + k * 3].at(0 + i * 3))) << std::endl;
                verif.insert((tab[j + k * 3].at(0 + i * 3)));
                std::cerr << ((tab[j + k * 3].at(1 + i * 3))) << std::endl;
                verif.insert((tab[j + k * 3].at(1 + i * 3)));
                std::cerr << ((tab[j + k * 3].at(2 + i * 3))) << std::endl;
                verif.insert((tab[j + k * 3].at(2 + i * 3)));

            }
            std::cerr << "Verif  bloque " << i + k * 3 << " : ";
            test = ft_ScreenSet(verif);
            if (test == "false")
                return test;
            verif.clear();


        }
    }

    return  test;
}

std::string ft_testRow(std::string tab[9])
{
    std::set<int>   verif;
    std::string test = "true";
    verif.clear();

    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
            verif.insert(tab[i].at(j));
        test = ft_ScreenSet(verif);
        if (test == "false")
            return test;
        verif.clear();
    }
    return test;
}

std::string ft_testColumn(std::string tab[9])
{
    std::set<int>   verif;
    std::string test = "true";
    verif.clear();

    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
            verif.insert(tab[j].at(i));
        test = ft_ScreenSet(verif);
        if (test == "false")
            return test;
        verif.clear();
    }
    return test;
}

int main()
{
    std::string tab[9] = {""};
    std::string test = "";

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            int n;
            std::cin >> n; std::cin.ignore();
            std::cerr << n;
            tab[i] += std::to_string(n);
        }
        std::cerr << std::endl;
    }
    std::cerr << std::endl;
    ft_Display(tab);
    test = ft_Test(tab);
    if (test == "true")
        test = ft_testRow(tab);
    if (test == "true")
        test = ft_testColumn(tab);

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    std::cout << test << std::endl;
}






// ******************************************************
// ******************************************************
// ******************************************************




// #include <iostream>
// #include <vector>

// int main()
// {
//     std::vector<std::vector<int>> sudoku = std::vector<std::vector<int>>(3 * 9, std::vector<int>(9, 0));
//     for (int i = 0; i < 9; ++i) {
//         for (int j = 0; j < 9; ++j) {
//             int n;
//             std::cin >> n; std::cin.ignore();

//             if(n < 1 || n > 9) {
//                 std::cout << "false" << std::endl;
//                 return 0;
//             }

//             // horizontal
//             sudoku[i][n-1]++;

//             // vertical
//             sudoku[9 + j][n-1]++;

//             // squares
//             sudoku[2*9 + (i/3)*3 + j/3][n-1]++;
//         }
//     }

//     for(const std::vector<int> & lineOrSquare : sudoku) {
//         for(const int & n : lineOrSquare) {
//             if(n != 1) {
//                 std::cout << "false" << std::endl;
//                 return 0;
//             }
//         }
//     }

//     std::cout << "true" << std::endl;
//     return 0;
// }