/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Rock_Paper_Scissors_Lizard_Spock.js                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/01/14 11:24:57 by pwolff            #+#    #+#             */
/*   Updated: 2024/01/14 11:25:14 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const N = parseInt(readline());

let tabPlayer = [];
for (let i = 0; i < N; i++) {
    
    var inputs = readline().split(' ');
    const NUMPLAYER = parseInt(inputs[0]);
    const SIGNPLAYER = inputs[1];
    tabPlayer.push([NUMPLAYER, SIGNPLAYER]);
}

console.error(tabPlayer);

// Write an answer using console.log()
// To debug: console.error('Debug messages...');


// Graph tabGraph de N x N rempli de 0 ***************************
let tabGraph = [];
// for (let y = 0; y < N; y++){
//     let temp = "";
//     for (let x = 0; x < N; x++){
//         temp += '0';
//     }
//     tabGraph.push(temp);
// }
// console.error("N : " + N);
// console.error(tabGraph);


function testCombat(player1, player2){
    if (player1[1] == 'R' && (player2[1] == 'L' || player2[1] == 'C')){
        return player1;
    }
    else if (player1[1] == 'P' && (player2[1] == 'R' || player2[1] == 'S')){
        return player1;
    }
    else if (player1[1] == 'C' && (player2[1] == 'P' || player2[1] == 'L')){
        return player1;
    }
    else if (player1[1] == 'L' && (player2[1] == 'P' || player2[1] == 'S')){
        return player1;
    }
    else if (player1[1] == 'S' && (player2[1] == 'C' || player2[1] == 'R')){
        return player1;
    }
    else if (player2[1] == 'R' && (player1[1] == 'L' || player1[1] == 'C')){
        return player2;
    }
    else if (player2[1] == 'P' && (player1[1] == 'R' || player1[1] == 'S')){
        return player2;
    }
    else if (player2[1] == 'C' && (player1[1] == 'P' || player1[1] == 'L')){
        return player2;
    }
    else if (player2[1] == 'L' && (player1[1] == 'P' || player1[1] == 'S')){
        return player2;
    }
    else if (player2[1] == 'S' && (player1[1] == 'C' || player1[1] == 'R')){
        return player2;
    }


    return player1[0] < player2[0] ? player1 : player2;
}




while (true){
  let newResult = [];  
  console.error(newResult); 

    for (let i = 0; i < tabPlayer.length; i += 2){
        let win = testCombat(tabPlayer[i], tabPlayer[i + 1]);
       // console.error("Combat : " + i + " " + tabPlayer[i] + " || " + tabPlayer[i + 1] + " Winner : " + win);

        newResult.push(win);
        x = (win[0] == tabPlayer[i][0] ? tabPlayer[i + 1][0] : tabPlayer[i][0]);
        console.error("Combat : " + i + " " + tabPlayer[i] + " || " + tabPlayer[i + 1] + " Winner : " + win + " x = " + x);
        let temp = [win[0], x];
        tabGraph.push(temp);

        // tabGraph[win[0]-1][x] = '1';
    }
   // console.error(newResult);
    tabPlayer = [].concat(newResult);
    console.error(tabPlayer);
    if (tabPlayer.length == 1){
        break;
    }
}

console.error(tabGraph);

let resultList = "";
for (let i = 0; i < tabGraph.length; i++){
    if (tabGraph[i][0] == tabPlayer[0][0]){
        resultList += tabGraph[i][1] + " ";
    }

}

let temp = "";
for (let i = 0; i < resultList.length - 1; i++){
    temp += resultList[i];
}
resultList = temp;

console.log(tabPlayer[0][0]);
console.log(resultList);
