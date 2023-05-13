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

#include <cctype>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

bool        testPunctuation(char c);
std::string ft_singleSpaceBetweenWords(std::string intext);
std::string ft_noSpaceBeforePunctuation(std::string intext);
std::string ft_oneSpaceAfterPunctuation(std::string intext);
std::string ft_removeReapedPunctuation(std::string intext);
std::string ft_lowercaseLetters(std::string intext);

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
    result = ft_lowercaseLetters(result);

    std::cout << result << std::endl;
}

std::string ft_lowercaseLetters(std::string intext){
    std::string result = "";
    int c = intext.length();
    int i = 2;

    result.push_back(std::toupper(intext.at(0)));
    result.push_back(std::tolower(intext.at(1)));
    for (; i < c; i++)
    {
        if (intext.at(i - 2 ) == '.')
        {
            result.push_back(std::toupper(intext.at(i)));
        }
        else
        {
            result.push_back(std::tolower(intext.at(i)));
        }
    }


    std::cerr << "05 : " << result << std::endl;
    return result;
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


// ********************************************************

// #include <iostream>
// #include <string>
// #include <regex>

// using namespace std;

// int main()
// {
//     std::string x;
//     getline(cin, x);

//     cerr << "x = " << x << endl;

//     for( int i = 0; i < x.length(); i++ ) { x[i] = tolower( x[i] ); }
//     x = regex_replace (x, regex("[\\s]+"), " ");
//     x = regex_replace (x, regex("[ ]*,[ ]*"), ",");
//     x = regex_replace (x, regex("[ ]*\\.[ ]*"), ".");
//     x = regex_replace (x, regex(",+"), ", ");
//     x = regex_replace (x, regex("\\.+"), ". ");
//     x = regex_replace (x, regex("[\\s]+$"), "");

//     // upper case for start of sentence
//     x[0] = toupper( x[0] );
//     for( int i = 2; i < x.length(); i++ ) {
//         if( x[i-2] == '.' && x[i-1] == ' ' ) { 
//             x[i] = toupper( x[i] );
//         }
//     }
    
//     cout << x << endl;
// }

// ********************************************************



// #include <iostream>
// #include <string>
// #include <algorithm>
// #include <sstream>
// using namespace std;

// int main()
// {
//     string intext; getline(cin, intext);

//     ostringstream str;
//     bool isStart = true, isPunct = false, isSpace = false;
//     for (auto c : intext) {
//         if (isspace(c)) {
//             isSpace = true;
//             continue;
//         } else if (isalpha(c)) {
//             if (isPunct || isSpace) str << ' ';
//             c = isStart ? toupper(c) : tolower(c);
//             isStart = isPunct = isSpace = false;
//         } else if (ispunct(c)) {
//             if (isPunct) continue;
//             isStart = ('.' == c);
//             isPunct = true;
//             isSpace = false;
//         }
//         str << c;
//     }

//     cout << str.str() << endl;
// }

// ********************************************************


// #include <iostream>

// using namespace std;

// void replace(string& s, const string& s1, const string& s2, const bool& once=false) {
//     auto f = s.find(s1);
//     while(f != s.npos) {
//         s.replace(f, s1.length(), s2);
//         f = s.find(s1, once ? f+1 : 0);
//     }
// }

// void fix_case(string& s) {
//     string r;
//     bool punct(true);
//     for (char c:s) {
//         if (punct && c>='a' && c<='z') c+='A'-'a'; 
//         if (!punct && c>='A' && c<='Z') c-='A'-'a';
//         if (c!=' ') punct=false;
//         if (c=='.') punct=true;
//         r+=c;
//     }
//     s = r;
// }

// int main()
// {
//     string t;
//     getline(cin, t);
//     for (string p:{ ".", ",", ";" }) {
//         replace(t, " "+p, p);
//         replace(t, p+p, p);
//         replace(t, p, p+" ", true);
//     }
//     replace(t, "  ", " ");
//     fix_case(t);
//     if (t.back() == ' ') t.pop_back();
//     cout << t << endl;
// }



// ********************************************************


// #include <iostream>
// #include <string>
// #include <vector>
// #include <algorithm>
// #include <ctype.h>

// using namespace std;


// int main()
// {
//     string s;
//     getline(cin, s);
	
// 	for(int i=s.size()-1;i>=0;i--){
// 		if( i>0 && s[i] == ' ' && !isalpha(s[i-1]) ){
// 			s.erase( s.begin()+i );
// 		}
// 		else if( i<s.size()-1 && s[i] == ' ' && !isalpha(s[i+1]) ){
// 			s.erase( s.begin()+i );
// 		}
// 	}
	
// 	bool capsNeeded = true;	
// 	int i=0;
// 	while( i<s.size() ){
// 		if( isalpha(s[i]) ){
// 			if( capsNeeded ){
// 				s[i] = toupper(s[i]);
// 				capsNeeded = false;
// 			}
// 			else{
// 				s[i] = tolower(s[i]);
// 			}
// 			i++;
// 		}
// 		else if( s[i] != ' ' && i<s.size()-1 ){
// 			if( s[i+1] == s[i] ){
// 				s.erase( s.begin()+i );
// 			}
// 			else{
// 				s.insert( s.begin()+i+1, ' ');
// 				capsNeeded = s[i] == '.';
// 				i+=2;
// 			}
// 		}
// 		else{
// 			i++;
// 		}
// 	}
// 	cout << s << endl;
// }