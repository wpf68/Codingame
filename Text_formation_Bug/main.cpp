/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/11 14:34:21 by pwolff            #+#    #+#             */
/*   Updated: 2023/05/11 14:34:21 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

//using namespace std;

bool    testPunctuation(char c)
{
    if ( (c >= '0' && c <= '9') || (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || c == ' ')
    {
        return (false);
    }

    return (true);
}

    // Test repeat puncruation **************************************************
    std::string ft_testRepeatPunctuation(std::string intext) {
        int i = 0, c = intext.length();
        std::string solution = "";

        if (!testPunctuation(intext.at(0)))
        {
            solution = intext.at(0);

        }

        for (i = 1; i < c; i++)
        {
            if (testPunctuation(intext.at(i)))
            {
                if (!testPunctuation(intext.at(i - 1)))
                {
                    solution += intext.at(i);
                }
            }
            else
            {
                solution += intext.at(i);
            }
        }
        
        std::cerr << "repeat punctuation\n" <<  solution << std::endl;
        return solution;
    }

    // Test le ' ' en trop **************************************************
    std::string ft_testSpace(std::string intext) {
        int i = 0, c = intext.length();
        std::string solution = "";

        solution = intext.at(0);

        for (i = 1; i < c; i++)
        {
            if (intext.at(i) == ' ')
            {
                if (i != 0 && intext.at(i - 1) != ' ' && !testPunctuation(intext.at(i + 1)))
                {
                    solution += intext.at(i);
                }
            }
            else
            {
                solution += intext.at(i);
            }   
        }
        
        std::cerr << "Space\n" <<  solution << std::endl;
        return solution;
    }


    //  Test les minuscule ==> majuscule   **************************************
    std::string ft_testMinToMaj(std::string intext) {
        int i = 0, c = intext.length();
        std::string solution = "";

        for (i = 0; i < c; i++)
        {
            if ((intext.at(i) >= 'a' && intext.at(i) <= 'z') )
            {
                if (i == 0 || (i >= 2 && intext.at(i - 1) == '.'))
                {
                    solution += (char)(intext.at(i) - 32);
                }
                else 
                {
                    solution += intext.at(i);
                }
            }
            else
            {
                solution += intext.at(i);
            }
        }
        
        std::cerr << "Minuscule ==> Majuscule\n" <<  solution << std::endl;
        return solution;
    }


    //  Test les majuscule ==> minuscule   **************************************
    std::string ft_testMajToMin(std::string intext) {
        int i = 0, c = intext.length();
        std::string solution = "";

        solution = intext.at(0);

        for (i = 1; i < c; i++)
        {
            if ((intext.at(i) >= 'A' && intext.at(i) <= 'Z') )
            {
                if ((intext.at(i - 2) != '.'))
                {
                    solution += (char)(intext.at(i) + 32);
                }
                else 
                {
                    solution += intext.at(i);
                }
            }
            else
            {
                solution += intext.at(i);
            }
        }
        
        std::cerr << "Majuscule ==> Minuscule\n" <<  solution << std::endl;
        return solution;
    }



    //  Test les espace après punctuation   **************************************
    std::string ft_testSpaceAfterPunct(std::string intext) {
        int i = 0, c = intext.length();
        std::string solution = "";

        solution = intext.at(0);

        for (i = 1; i < c; i++)
        {
            if ((intext.at(i) >= 'A' && intext.at(i) <= 'Z') || (intext.at(i) >= 'a' && intext.at(i) <= 'z'))
            {
                if (testPunctuation(intext.at(i - 1)))
                {
                    solution += " ";
                    solution += (char)(intext.at(i));
                }
                else 
                {
                    solution += intext.at(i);
                }
            }
            else
            {
                solution += intext.at(i);
            }
        }
        
        std::cerr << "Space after punctuation\n" <<  solution << std::endl;
        return solution;
    }


    //  Test Majuscule after point   **************************************
    std::string ft_testMajAfterPoint(std::string intext) {
        int i = 0, c = intext.length();
        std::string solution = "";

        for (i = 0; i < c; i++)
        {
            if ( i > 2 && intext.at(i) >= 'a' && intext.at(i) <= 'z')
            {
                if (intext.at(i - 2) == '.')
                {
                    solution += (char)(intext.at(i) - 32);
                }
                else 
                {
                    solution += intext.at(i);
                }
            }
            else
            {
                solution += intext.at(i);
            }
        }
        
        std::cerr << "Majuscule after point\n" <<  solution << std::endl;
        return solution;
    }


        //  Clear Space  **************************************
    std::string ft_clearSpace(std::string intext) {
        int i = 0, c = intext.length();
        std::string solution = "";

        for (i = 0; i < c; i++)
        {
            if (intext.at(i) != ' ')
            {
                solution += intext.at(i);
            }
            else if (!(testPunctuation(intext.at(i + 1))))
            {
                solution += intext.at(i);
            }
        }
        
        std::cerr << "Clear Space\n" <<  solution << std::endl;
        return solution;
    }

int main()
{
    std::string intext = "";
    std::string solution = "";
    getline(std::cin, intext);
    


    std::cerr << "Original\n" <<  intext << std::endl;


    intext = ft_clearSpace(intext);
    intext = ft_testSpace(intext);
    intext = ft_testRepeatPunctuation(intext);

    intext = ft_testMinToMaj(intext);
    intext = ft_testSpaceAfterPunct(intext);
    intext = ft_testMajToMin(intext);
    intext = ft_testMajAfterPoint(intext);

    std::cout << intext << std::endl;
}