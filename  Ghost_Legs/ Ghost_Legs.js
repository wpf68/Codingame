/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*    Ghost_Legs.js                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/11/30 07:12:08 by pwolff            #+#    #+#             */
/*   Updated: 2023/11/30 07:12:26 by pwolff           ###   ########.fr       */
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
