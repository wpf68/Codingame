/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   RetroTypewriterArt.js                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/08 08:36:03 by pwolff            #+#    #+#             */
/*   Updated: 2023/12/08 08:43:57 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const T = readline();

// Write an answer using console.log()
// To debug: console.error('Debug messages...');


let tabAb = [" ", "\\", "'", "\n"];
let tabKey = ["sp", "bS", "sQ", "nl"];

// ************* test *************
//console.error("**" + tabAb[3] + "**");


console.error(T);

let tabT = T.split(' ');

// ***********   test tabT ******************
// for(let i = 0; i < tabT.length; i++){
//     console.error(i + " : " + tabT[i]);
// }

function testTabKey(tab){
    val = false;

    if (tab.length < 2){
        return false;
    }
    let key = tab[tab.length - 2] + tab[tab.length - 1];

    //console.error(tab + " : " + key);
    let found = tabKey.findIndex((element) => element == key);
    //console.log(found + " : **" + tabAb[found] + "**");
    if (found != -1){
        return tabAb[found];
    }
    return val;
}




let result = "";

for (let i = 0; i < tabT.length; i++){
    if (val = testTabKey(tabT[i])){
        let temp = tabT[i];
        let num = "";
        for(let j = 0; j < temp.length - 2; j++){
            num += temp[j];
        }
        if (num == ""){
            result += val;
        }
        else {
            for(let j = 0; j < +num; j++){
                result += val;
            }
        }

    }
    else {
        let temp = tabT[i];
        let char = temp[temp.length - 1];
        let num = "";
        for(let j = 0; j < temp.length - 1; j++){
            num += temp[j];
        }
        //console.error(num + " " + char);

        for(let j = 0; j < +num; j++){
            result += char;
        }
    }
}


console.log(result);



/// *******************************************

// const T = readline().split(' ');

// const answer = [];
// for (let chunk of T) {
//     let num = parseInt(chunk, 10);
//     num = isNaN(num) ? 1 : num;
//     let char = '';
//     switch (true) {
//         case chunk.endsWith('sp'): char = ' '; break;
//         case chunk.endsWith('bS'): char = '\\'; break;
//         case chunk.endsWith('sQ'): char = '\''; break;
//         case chunk.endsWith('nl'): char = '\n'; break;
//         case /\d$/.test(chunk): char = chunk[chunk.length - 1]; num = Math.floor(num / 10); break;
//         default:
//             char = chunk[chunk.length - 1];
//     }
//     answer.push(char.repeat(num));
// }

// console.log(answer.join(''));


// **********************************************


// const replacements = {sp: ' ', bS: '\\', sQ: "'", nl: "\n"};
// console.log(readline().split(' ').map((item) => {
//     let [_, times, symbol] = item.match(/^(\d*)(sp|bS|sQ|nl|.)$/);
//     return (replacements[symbol] ?? symbol).repeat(times || 1);
// }).join(''));


// ************************************************


// readline().split(/ ?nl ?/).forEach(r => {
//     console.log(r.split(' ').reduce((row, chunk) => {
//         let c = chunk.replace(/..$/g, x => ({sp:` `, bS:`\\`, sQ:`'`})[x] || x);
//         return row + c.slice(-1).repeat(+c.slice(0, -1));
//     }, ''));
// });



// *******************************************************

// const s = readline();
// console.error(s);
// const code = {sp:' ', bS:'\\', sQ:"'", nl:'\n'};
// let r = ''
// for (let w of s.split(' ')) {
//     let [_,n,m] = w.match(/^(\d*)(sp|bS|sQ|nl|.)$/);
//     r += (code[m] ?? m).repeat(n || 1);
// }

// console.log(r);