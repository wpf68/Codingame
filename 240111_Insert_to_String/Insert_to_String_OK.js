/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Insert_to_String_OK.js                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/01/14 09:14:18 by pwolff            #+#    #+#             */
/*   Updated: 2024/01/14 09:25:26 by pwolff           ###   ########.fr       */
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

let tabRawChange = [];
for (let i = 0; i < changeCount; i++) {
    const rawChange = readline();
    tabRawChange.push(rawChange);

}

function modifF(rawChange, k){

    let tabK = 0;

    for(let i = 0; k > 0; i++){
        if (s[i] == '\n'){
            k--;
        }
        console.error(" -- " + s + " --");
        console.error(" -------- i -------- " + i);
        tabK = i + 1;
    }   

    console.error("rawChange : " + rawChange);
    let val = parseInt(rawChange.slice(rawChange.indexOf('|') + 1)) + tabK;
    console.error("val : " + val);
    let temp = s.substring(0, val);
    let string = rawChange.slice(rawChange.lastIndexOf('|') + 1);
    temp += string + s.substring(val);

    s = temp.replaceAll("\\n", '\n');
    console.error("New s : " + s + '\n');
}


console.error("tabRawChange : \n" + tabRawChange + "\n *************** \n");


for(let k = sizeNiveaux; k >= 0; k--){

    console.error("**** K ***** : " + k);
    for (let j = sizeS; j >= 0; j--){
        console.error("**** j ***** : " + j);
        for (let i = 0; i < changeCount; i++) {
            console.error("**** i ***** : " + i);

            if (parseInt(tabRawChange[i].slice(tabRawChange[i].indexOf('|') + 1)) == j &&
            parseInt(tabRawChange[i]) == k){
                console.error("**** Match ***********");
                modifF(tabRawChange[i], k);
            }
        }
    }

}


console.log(s);



// ***************************

// const s = readline().split('\\n');
// const changeCount = parseInt(readline());

// Array
//     .from({length: changeCount}, _ => {
//         const [row, col, change] = readline().split('|');
//         return {row: Number(row), col: Number(col), change :change.replaceAll('\\n','\n')};
//     })
//     .sort((a, b) => (a.row === b.row) ? (b.col - a.col) : (b.row - a.row))
//     .forEach(({row, col, change}) => s[row] = s[row].slice(0, col) + change + s[row].slice(col));

// s.forEach((it) => console.log(it));






// ******************************************


// let r = readline,
//     str = r().split('\\n');

// [...Array(+r())].map(_ => r().split('|')).sort((a, b) => b[0]-a[0] || b[1]-a[1]).forEach(([r, c, t]) => {
//     str[r] = str[r].slice(0, +c) + t.replace(/\\n/g, '\n') + str[r].slice(+c);
// });

// console.log(str.join('\n'));
