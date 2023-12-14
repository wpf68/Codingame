/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Ghost_Legs.cpp                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/02 08:42:47 by pwolff            #+#    #+#             */
/*   Updated: 2023/12/02 08:44:34 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int w;
    int h;
    
    vector<string> tab;

    cin >> w >> h; cin.ignore();

    for (int i = 0; i < h; i++) {
        string line;
        getline(cin, line);
        tab.push_back(line);
    }

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;
    cerr << "W : " << w <<  " H : " << h << endl;

    for(int i = 0; i < h; i++){
        cerr << tab[i] << endl;
    }
    

    string origine = "";
    for (int i = 0; i < w; i += 3){
        origine += tab[0][i];
    }

    string answer = "";
    for (int i = 0; i < w; i += 3){
        answer += tab[h - 1][i];
    }
   // let answer = tab[H - 1].split("  ");

    cerr << "origine = " << origine << endl;
    cerr << "answer  = " << answer << endl;
    // console.error("answer = " + answer);

    for (int i = 0; i < origine.length(); i++){
        int colonne = i;
        for (int j = 1; j < h - 1; j++){
            if (tab[j][colonne * 3 + 1] == '-'){
                colonne += 1;
            }
            else if (j && tab[j][colonne * 3 - 1] == '-'){
                colonne -= 1;
            }
        }
        cout << origine[i] << answer[colonne] << endl;
    }

    //cout << "answer" << endl;
}
