/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*    Ghost_Legs.js                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/11/30 07:12:08 by pwolff            #+#    #+#             */
/*   Updated: 2023/11/30 07:30:54 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

var inputs = readline().split(' ');
const W = parseInt(inputs[0]);
const H = parseInt(inputs[1]);

console.error("W : " + W + " H : " + H);

let tab = [];

for (let i = 0; i < H; i++) {
    const line = readline();
    tab.push(line);
}
console.error(tab);

let origine = tab[0].split("  ");
let answer = tab[H - 1].split("  ");

console.error("oriine = " + origine);
console.error("answer = " + answer);

for (let i = 0; i < origine.length; i++){
    let colonne = i;
    for (let j = 1; j < H - 1; j++){
        if (tab[j][colonne * 3 + 1] == '-'){
            colonne += 1;
        }
        else if (j && tab[j][colonne * 3 - 1] == '-'){
            colonne -= 1;
        }
    }
    console.log(origine[i] + answer[colonne]);
}




// **********************************************  puma17 *****************************

// r = readline; [w,h]=r().split(' ').map(x=>+x);
// l = [...Array(h)].map(x=>r().split(''));

// for (i=0; i<w; i+=3) {
//     for (y=1,x=i; y<h-1; y++)
//         x += (x<w-1 && l[y][x+1]=='-')*3 - (x>0 && l[y][x-1]=='-')*3;
//     print(l[0][i]+l[h-1][x]);
// }







// **********************************************  beekeeperkeeper ***********************

// let [, h] = readline().split(' ');
// let [top, ...rungs] = [...Array(--h)].map(readline);
// let bottom = readline().split("  ");

// rungs.reverse().forEach(val => 
//     val.split('|').forEach((v, i) => {
//         if (v === "--") [bottom[i - 1], bottom[i]] = [bottom[i], bottom[i - 1]];
//     })
// );

// print(top.split("  ").map((val, i) => val + bottom[i]).join('\n'));