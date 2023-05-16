/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main2.cpp                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/12 19:14:32 by pwolff            #+#    #+#             */
/*   Updated: 2023/05/12 19:14:32 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

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
    std::string datas[30];
    std::string result= "";
    int len = t.length();

    for (int i = 0; i < h; i++) {
        std::string row;
        getline(std::cin, row);
        datas[i] = row;
    }
    result = "";
    result = ft_putChar(datas, t, l, h);
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
            pos = c - 'a';
        else if (c >= 'A' && c <= 'Z')
            pos = c - 'A';
        else 
            pos = 26;
        for (int i = 0; i < h; i++)
            for (int j = pos * l; j < pos * l + l; j++)
                result[i].push_back(datas[i].at(j));
    }
    for(int i = 0; i < h; i++)
        resultfinal += result[i] + "\n";

    return resultfinal;
}

// std::string ft_display(std::string data[30], int l, int h){
//     std::string result;
//     int i = 0;
//     int j = 0;

//     for (i = 0; i < h; i++)
//     {
//         for (j = 0; j < 27 * l; j++)
//         {
//             result += data[i].at(j);
//         }
//         result += "\n";
//     }
//     return result;
// }







// ****************************************************************************





// #include <iostream>
// #include <string>
// #include <vector>
// #include <algorithm>

// using namespace std;

// /**
//  * Auto-generated code below aims at helping you parse
//  * the standard input according to the problem statement.
//  **/

 
// int main()
// {
//     int L;
//     cin >> L; cin.ignore();
//     int H;
//     cin >> H; cin.ignore();
//     string T;
//     getline(cin, T);
//     string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

//     for (int i = 0; i < H; i++) {
//         string ROW;
//         getline(cin, ROW);

//         for (char t : T){
            
//             int index = alphabet.find(toupper(t));
   
//             if (index >= 0) {
//                 cout << ROW.substr(L * index, L);
//             } else {
//                 cout << ROW.substr(ROW.length()-L, L);
//             }
            
//         }
//         cout << endl;
//     }


// }