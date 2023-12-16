/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Card_Counting_when_easily_distracted.js            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/16 09:57:44 by pwolff            #+#    #+#             */
/*   Updated: 2023/12/16 10:05:48 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const streamOfConsciousness = readline();
const bustThreshold = parseInt(readline());

let deck = "AAAA22223333444455556666777788889999TTTTJJJJQQQQKKKK";

// Write an answer using console.log()
// To debug: console.error('Debug messages...');

console.error(streamOfConsciousness);
console.error(bustThreshold);


// ***  TESTS ****
    // console.error("Deck : " + deck);
    // let temp = deck.replace("3","");
    // deck = temp;
    // console.error("Deck : " + deck);
    // temp = deck.replace("K","");
    // deck = temp;
    // console.error("Deck : " + deck);
// *******************************

let visual = streamOfConsciousness.split(".");
//console.error(visual);

// *** verif streamOfConsciousness ***
for (let test of visual){
    //console.error(test);
    let verifTest = 1;
    for (let i = 0; i < test.length; i++){
        //console.error(" - " + test[i]);
        let a = test[i];
        if (!(a == "A" || a == "2" || a == "3" || a == "4" || a == "5" || a == "6" || a == "7" 
        || a == "8" || a == "9" || a == "T" || a == "J" || a == "Q" || a == "K" )){
            verifTest = 0;
            break;
        }
    }
    if (verifTest){
        console.error(test);
        let temp = "";
        for (let i = 0; i < test.length; i++){
            temp = deck.replace(test[i], "");
            deck = temp;
        }
    }
    

}
console.error("Deck : " + deck);

let nb = 0;
for (let i = 0; i < deck.length; i++){
    if (+deck[i] >= 2 && +deck[i] <= 9){
        if (+deck[i] < bustThreshold){
            nb++;
        }

    }
    else if (deck[i] == "A"){
        if (1 < bustThreshold){
            nb++;
        }
    }
    else {
        if (10 < bustThreshold){
            nb++;
        }
    }
}

console.error("nb : " + nb);


let pourc = (nb / deck.length) * 100;

console.error("pourc : " + pourc);
console.log((Math.round(pourc)) + "%" );


















// **********************************************************************************


/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
// const N_CARDS = 52;
// const streamOfConsciousness = readline().split('.');
// const bustThreshold = parseInt(readline());

// const cardSeries = streamOfConsciousness.filter((s) => /^[2-9KQJTA]+$/.test(s)).join('');

// let n_cards_below;

// let total = 0, below = 0;
// cardSeries.split('').forEach(c => {
//     total++;

//     let value;
//     switch(c){
//         case 'K':
//         case 'Q':
//         case 'J':
//         case 'T':
//             value = 10;
//             break;
//         case 'A':
//             value = 1;
//             break;
//         default:
//             value = parseInt(c);
//             break;
//     }

//     if(value < bustThreshold) below++;
// });


// if(bustThreshold <= 0) n_cards_below = 0
// else if(bustThreshold <= 10 ) n_cards_below = 4 *(bustThreshold-1)
// else n_cards_below = total

// console.warn(cardSeries)
// console.log(Math.round(100 * (n_cards_below - below)/(N_CARDS - total)) + '%');



// **********************************************************************************

// const streamOfConsciousness = readline();
// const bustThreshold = parseInt(readline());

// var validCardsLeft = bustThreshold * 4 - 4
// var totalCardsLeft = 52

// for (const thought of streamOfConsciousness.split(".")) {
//     if (/[^A2-9TJQK]/.exec(thought)) continue
//     for (const card of thought.split("")) {
//         totalCardsLeft -= 1

//         const cardValue = card === "A" ? 1 : "TJKQ".includes(card) ? 10 : parseInt(card)
//         if (cardValue < bustThreshold) validCardsLeft -= 1
//     }
// }

// console.log(`${Math.round(validCardsLeft / totalCardsLeft * 100)}%`);
