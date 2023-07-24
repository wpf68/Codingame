#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

void    ft_display(int w, int h, unsigned char *grille){
    for (int y = 0; y < h; y++){
        for (int x = 0; x < w; x++){
            std::cerr << grille[y * w + x];
        }
        std::cerr << std::endl;
    }
    std::cerr << std::endl;
}


int main()
{
    int w;
    int h;
    int count_x;
    int count_y;

    cin >> w >> h >> count_x >> count_y; cin.ignore();

    w++;
    h += 2;


    unsigned char    grille[(h * w)];
    int     colonnes[count_x];
    int     lignes[count_y + 2];

    for (int y = 0; y < h; y++){
        for (int x = 0; x < w; x++){
            grille[y * w + x] = '0';
        }
    }

    ft_display(w, h, grille);

    for (int i = 0; i < count_x; i++) {
        int x;
        cin >> x; cin.ignore();
        colonnes[i] = x;
    }

    lignes[0] = 0;
    lignes[count_y + 1] = h;
    for (int i = 0; i < count_y; i++) {
        int y;
        cin >> y; cin.ignore();
        lignes[i + 1] = ++y;
    }

    for (int i = 0; i < count_y + 2; i++){
        for (int j = 0; j < w; j++){
            std::cout << "lignes [" << i << "] = " << lignes[i] << std::endl;
            grille[lignes[i] * w + j] = '_';
        }
    }
    ft_display(w, h, grille);

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << "0" << endl;
}