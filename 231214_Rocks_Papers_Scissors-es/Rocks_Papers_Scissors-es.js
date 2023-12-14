/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Rocks_Papers_Scissors-es.js                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/14 08:53:30 by pwolff            #+#    #+#             */
/*   Updated: 2023/12/14 08:54:14 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const n = parseInt(readline());
const tabPlayer = [];

console.error("n : " + n);
for (let i = 0; i < n; i++) {
    //const a = readline();
    tabPlayer.push(readline());
    //console.error(i + " : " + a);
}



// ** test tabPlayer

for (let i = 0; i < n; i++){
    console.error(i + " : " + tabPlayer[i]);
}

// tabPlayer[1] = "***********";

// for (let i = 0; i < n; i++){
//     console.error(i + " : " + tabPlayer[i]);
// }

// Write an answer using console.log()
// To debug: console.error('Debug messages...');




let winnerArms = "";
let winnerNb = 0;
let winnerPos = -1;

for (let i = 0; i < n; i++){
    let play = "";
    let win = 0;
    switch (tabPlayer[i]){
        case "Rock" :
            play = "Paper";
            break;
        case "Paper" :
            play = "Scissors";
            break;
        default :
            play = "Rock"  
    }
    win++; 
    

    for (let j = 0; j < n - 1; j++){
        if (play == "Paper"){
            console.error("i = " + i + " j = " + (j + i + 1) % n);
            if (tabPlayer[(j + i + 1) % n] == "Rock"){
                win++;
                continue; 
            }
            else if(play == tabPlayer[(j + i + 1) % n]){
                continue;
            }
            else {
                break;
            }
        }
        else if (play == "Scissors"){
            console.error("i = " + i + " j = " + (j + i + 1) % n);
            if (tabPlayer[(j + i + 1) % n] == "Paper"){
                win++;
                continue; 
            }
            else if(play == tabPlayer[(j + i + 1) % n]){
                continue;
            }
            else {
                break;
            }
        }
        else if (play == "Rock"){
            console.error("i = " + i + " j = " + (j + i + 1) % n);
            if (tabPlayer[(j + i + 1) % n] == "Scissors"){
                win++;
                continue; 
            }
            else if(play == tabPlayer[(j + i + 1) % n]){
                continue;
            }
            else {
                break;
            }
        }



    }
    console.error("Player [" + i + "] : " + tabPlayer[i] + " ==> " + play + " win : " + win);
    if (win > winnerNb){
        winnerArms = play;
        winnerNb = win;
        winnerPos = i;
    }

}




console.log(winnerArms);
console.log(winnerPos);



// ***********************


// const loses={Rock:"Paper", Scissors:"Rock", Paper:"Scissors"};
// const n = parseInt(readline()), arr=new Array(n);
// for (let i = 0; i < n; i++) arr[i]=readline();
// let maxwins={move: "n/a", wins:0, pos:-1};
// for (let i = 0; i < n; i++) {
//     let mymove=loses[arr[i]], mywins=1;
//     for (var j=i+1 ; j<(i+n) && arr[j%n]!=loses[mymove]; j++)
//         if (loses[arr[j%n]]==mymove) mywins++;
//     if (mywins>maxwins.wins) maxwins={move: mymove, wins: mywins, pos: i};
// }
// console.log(maxwins.move);
// console.log(maxwins.pos);
