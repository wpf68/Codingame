/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/24 14:56:24 by pwolff            #+#    #+#             */
/*   Updated: 2023/05/24 14:56:24 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int ft_nDaysToYear(std::string monthEnd, int leapYear)
{
    std::string month[] = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
    int         nbDays[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int i = 0;
    int nDays = 0;

    while (true)
    {
        if (monthEnd == month[i])
        {
            return nDays;
        }
        //std::cerr << "i = " << i << " :: " << leapYear << std::endl;
        if (month[i] == "Feb" && leapYear)
        {
            nDays += nbDays[i] + 1;
        }
        else
        {
            nDays += nbDays[i];
        }

        i++;
        if (i > 12)
            break;
    }
    return -1;

}


int main()
{

    int         nbJoursDebut = 0;
    int         nbJoursFin = 0;
    std::string dayResult = "";
    std::string days[] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};

    int leap_year;
    std::cin >> leap_year; std::cin.ignore();
    std::string source_day_of_week;
    std::string source_month;
    int source_day_of_month;
    std::cin >> source_day_of_week >> source_month >> source_day_of_month; std::cin.ignore();
    std::string target_month;
    int target_day_of_month;
    std::cin >> target_month >> target_day_of_month; std::cin.ignore();

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    // tests
    // source_day_of_month = 13;
    // source_month = "Sep";

    // target_day_of_month = 12;
    // target_month = "Sep";
    //





    std::cerr << "Année Bisextile : " <<  (leap_year) << std::endl; 
    std::cerr <<  source_day_of_week << " \t" << source_day_of_month << " " << source_month << std::endl;
    std::cerr <<  " ? \t\t" << target_day_of_month << " " << target_month << "\n" << std::endl;

    nbJoursDebut = ft_nDaysToYear(source_month, (leap_year));
    if (nbJoursDebut == -1)
    {
        std::cerr << "Error nbJoursDebut" << std::endl;
        exit(-1);
    }
    nbJoursDebut += source_day_of_month;

    nbJoursFin = ft_nDaysToYear(target_month, (leap_year));
    if (nbJoursFin == -1)
    {
        std::cerr << "Error nbJoursFin" << std::endl;
        exit(-1);
    }
    nbJoursFin += target_day_of_month;

    std::cerr << nbJoursDebut << " Jours début" << std::endl;
    std::cerr << nbJoursFin << " Jours fin\n" << std::endl;

    int i = 0;
    int nbResult = 0;
    while (true)
    {
        if (source_day_of_week == days[i])
        {
            break;
        }
        i++;
    }

    if (nbJoursFin - nbJoursDebut >= 0)
    {
        nbResult = (nbJoursFin - nbJoursDebut) % 7;
        dayResult = days[(i + nbResult) % 7];
    }
    else 
    {
        nbResult = (nbJoursDebut - nbJoursFin) % 7;
        if (i - nbResult >= 0)
        {
            dayResult = days[(i - nbResult) % 7];
        }
        else
        {
            dayResult = days[(i - nbResult + 7) % 7];
        }
    }


    std::cout << dayResult << std::endl;
}