/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Insert_to_String_Level_2.js                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/01/11 08:50:03 by pwolff            #+#    #+#             */
/*   Updated: 2024/01/11 08:50:42 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

let s = readline();
s = s.replaceAll("\\n", '\n');
let sizeNiveaux = 0;

for(let i = 0; i < s.length; i++){
    if (s[i] == '\n'){
        sizeNiveaux++;
    }
}

console.error("sizeNiveaux : \n" + sizeNiveaux + "\n ************* \n");


let sizeS = s.length;


console.error("s : \n" + s + "\n ************* \n");

const changeCount = parseInt(readline());
console.error("changeCount : " + changeCount + "\n ****************** \n");
//tab = 0;
let tabRawChange = [];
for (let i = 0; i < changeCount; i++) {
    const rawChange = readline();
    tabRawChange.push(rawChange);

}


function modifF(rawChange){
    //const rawChange = readline();
    console.error("rawChange : " + rawChange);
    let val = parseInt(rawChange.slice(rawChange.indexOf('|') + 1)); // + tab;
    console.error("val : " + val);
    let temp = s.substring(0, val);
    let string = rawChange.slice(rawChange.lastIndexOf('|') + 1);
    temp += string + s.substring(val);
    string = string.replaceAll("\\n", '\n');
    s = temp.replaceAll("\\n", '\n');
    console.error("New s : " + s + '\n');
}




console.error("tabRawChange : \n" + tabRawChange + "\n *************** \n");


for(let k = sizeNiveaux; k >= 0; k--){


    for (let j = sizeS; j >= 0; j--){
        for (let i = 0; i < changeCount; i++) {
            if (parseInt(tabRawChange[i].slice(tabRawChange[i].indexOf('|') + 1)) == j){
                modifF(tabRawChange[i]);
            }
        }
    }

}




//return true


// for (let i = 0; i < changeCount; i++) {
//     //console.error("tab : " + tab);
//     const rawChange = readline();
//     console.error("rawChange : " + rawChange);
//     let val = parseInt(rawChange.slice(rawChange.indexOf('|') + 1)); // + tab;
//     console.error("val : " + val);
//     let temp = s.substring(0, val);
//     //console.error("temp : " + temp);
//     //console.error("--" + rawChange.slice(rawChange.lastIndexOf('|') + 1) + "--");
//     let string = rawChange.slice(rawChange.lastIndexOf('|') + 1);
//     temp += string + s.substring(val);

//     //s = temp;
//     string = string.replaceAll("\\n", '\n');
//     //tab += string.length;
//     s = temp.replaceAll("\\n", '\n');
//     console.error("New s : " + s + '\n');

// }



// Write an answer using console.log()
// To debug: console.error('Debug messages...');

console.log(s);
