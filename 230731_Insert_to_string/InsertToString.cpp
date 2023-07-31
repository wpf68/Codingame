/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   InsertToString.cpp                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/31 10:38:22 by pwolff            #+#    #+#             */
/*   Updated: 2023/07/31 10:38:22 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <cstddef>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int ft_number(std::string tab){
    int number = 0;
    std::string temp = "";

    std::size_t i = tab.find('|');
    i++;

    while (tab.at(i) != '|'){
        temp.push_back(tab.at(i));
        i++;
    }
    number = std::stoi(temp);
    //std::cerr << "number : " << number << std::endl; 
    return number;
}

std::string ft_push_s(std::string s, std::string tab, int number){
    std::string temp = "";
    std::string newS = "";
    std::size_t i = tab.rfind('|');
    i++;

    while (i < tab.size()){
        temp.push_back(tab.at(i));
        i++;
    }
    std::cerr << "temp : " << temp << std::endl; 

    i = s.size();
    for (int j = 0; j < number; j++){
        newS.push_back(s.at(j));
    }
    newS += temp;
    for (int j = number; j < i; j++){
        newS.push_back(s.at(j));
    }

    std::cerr << "newS : " << newS << std::endl; 



    return  newS;
}

int main()
{
    std::vector<std::string>    tab;

    string s;
    getline(cin, s);
    int change_count;
    cin >> change_count; cin.ignore();

    std::cerr << s << " - " << change_count << std::endl;

    for (int i = 0; i < change_count; i++) {
        string raw_change;
        getline(cin, raw_change);

        tab.push_back(raw_change);
        std::cerr << i << " - " << tab.at(i) << std::endl;
    }

    for (int i = 0; i < change_count; i++){
        int number = ft_number(tab.at(i));

        s = ft_push_s(s, tab.at(i), number);

    }

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << "void main()" << endl;
    cout << "answer2" << endl;
    cout << "answer3" << endl;
}