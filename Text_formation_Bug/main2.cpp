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

bool        testPunctuation(char c);
std::string ft_singleSpaceBetweenWords(std::string intext);
std::string ft_noSpaceBeforePunctuation(std::string intext);
std::string ft_oneSpaceAfterPunctuation(std::string intext);
std::string ft_removeReapedPunctuation(std::string intext);

int main()
{
    std::string intext;
    std::string result;

    getline(std::cin, intext);

   // intext = "one ,    two, , ,,three   zeee.  ";


    std::cerr << "00 : " << intext << "\n" << std::endl;
    result = ft_singleSpaceBetweenWords(intext);
    result = ft_noSpaceBeforePunctuation(result);
    result = ft_removeReapedPunctuation(result);

    result = ft_oneSpaceAfterPunctuation(result);
    std::cout << result << std::endl;
}

std::string ft_removeReapedPunctuation(std::string intext){
    std::string result = "";
    int c = intext.length() - 1;
    int i = 0;

    for (; i < c; i++)
    {
        if (testPunctuation(intext.at(i)) && !testPunctuation(intext.at(i + 1)))
        {
            result.push_back(intext.at(i));
        }
        else if (!testPunctuation(intext.at(i)))
        {
            result.push_back(intext.at(i));
        }
    }
    result.push_back(intext.at(c));
    std::cerr << "03 : " << result << std::endl;
    return result;

}

std::string ft_oneSpaceAfterPunctuation(std::string intext){
    std::string result = "";
    int c = intext.length() - 1;
    int i = 0;

    for (; i < c; i++)
    {
        result.push_back(intext.at(i));
        if (testPunctuation(intext.at(i)) && intext.at(i + 1) != ' ')
        {
            result.push_back(' ');
        }
    }
    result.push_back(intext.at(c));
    std::cerr << "04 : " << result << std::endl;
    return result;
}



std::string ft_noSpaceBeforePunctuation(std::string intext){
    std::string result = "";
    int c = intext.length() - 1;
    int i = 0;

    for (; i < c; i++)
    {
        if (intext.at(i) == ' ' && !testPunctuation(intext.at(i + 1)))
        {
            result.push_back(intext.at(i));
        }
        else if (intext.at(i) != ' ')
        {
            result.push_back(intext.at(i));
        }
    }
    result.push_back(intext.at(c));
    std::cerr << "02 : " << result << std::endl;
    return result;
}

std::string ft_singleSpaceBetweenWords(std::string intext){
    std::string result = "";
    int c = intext.length();
    int i = 0;

    // suppression des space en début de chaine
    while (intext.at(i) == ' ')
    {
        i++;
    }

    // suppression des space au milieu de chaine
    if (i == 0)
    {
        result.push_back(intext.at(i));
        i++;
    }
    for (; i < c; i++)
    {
        if ((intext.at(i) == ' ' & intext.at(i - 1) == ' '))
        {
           
        }
        else
        {
           result.push_back(intext.at(i)); 
        }
        //std::cerr << intext.at(i) << std::endl;
    }

    // supression des space en fin de chaine
    i = result.length() - 1;
    intext = "";
    while (result.at(i) == ' ')
    {
        i--;
    }
    for (; i >= 0; i--)
    {
        intext.push_back(result.at(i));
    }

    // remise en ordre la string
    result = "";
    i = intext.length() - 1;
    for (; i >= 0; i--)
    {
        result.push_back(intext.at(i));
    }
    std::cerr << "01 : " << result << std::endl;
    return result;
}

bool    testPunctuation(char c)
{
    if ( (c >= '0' && c <= '9') || (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || c == ' ')
    {
        return (false);
    }
    return (true);
}