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

std::vector<std::string>    ft_trie_tab(std::vector<std::string> tab, int change_count){

    std::string temp;
    int         test = 1;

    while(test){
        test = 0;
        for (int i = 0; i < change_count - 1; i++){
            if (ft_number(tab.at(i)) < ft_number(tab.at(i + 1))) {
                temp = tab.at(i);
                tab.at(i) = tab.at(i + 1);
                tab.at(i + 1) = temp;
                test = 1;
            }
        }
    }


        for (int i = 0; i < change_count - 1; i++){
            if (ft_number(tab.at(i)) == ft_number(tab.at(i + 1))) {
                temp = tab.at(i);
                tab.at(i) = tab.at(i + 1);
                tab.at(i + 1) = temp;
            }
        }



    return tab;
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

    // ************   Trie du Tab  ***********
    tab = ft_trie_tab(tab, change_count);
    for (int i = 0; i < change_count; i++) {
        std::cerr << i << " - " << tab.at(i) << std::endl;
    }



    for (int i = 0; i < change_count; i++){
        int number = ft_number(tab.at(i));

        s = ft_push_s(s, tab.at(i), number);
    }



    std::cerr << "\n*****  Resut *****\n" << std::endl;
    //  ************  Taitement \n  ************
    for (int i = 0; i < s.size(); i++){
        if (s.at(i) == '\\'){
            std::cerr << std::endl;
            i++;
        }
        else
            std::cerr << s.at(i);
    }


    //  ***********  tests  ***********


    std::cerr << "\n*******  test  ********\n\n";
    std::cout << "void main()" << std::endl;
    std::cout << "{" << std::endl;
    std::cout << "  Console.WriteLine(\"Hello World\");" << std::endl;
    std::cout << "}" << std::endl;

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    // cout << "He said that I'm not good enough for the job. To which I replied \"Your lose!\"." << endl;
    // cout << "answer2" << endl;
    // cout << "answer3" << endl;
    //std::cout << s << std::endl;
}