/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Asteroids_OK.js                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/01/21 09:28:19 by pwolff            #+#    #+#             */
/*   Updated: 2024/01/21 09:36:48 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

var inputs = readline().split(' ');
const W = parseInt(inputs[0]);
const H = parseInt(inputs[1]);
const T1 = parseInt(inputs[2]);
const T2 = parseInt(inputs[3]);
const T3 = parseInt(inputs[4]);

let firstPictureRow = [];
let secondPictureRow = [];

// let string = "abcdefghijklmnopqrstuvxyz";
// string = string.substring(0, W);

let Tx = [];
for (let i = 0; i < H; i++){
    let temp = "";
    for (let j = 0; j < W; j++){
        temp += '.';
    }
    //Tx.push(string);
    Tx.push(temp);
}



for (let i = 0; i < H; i++) {
    var inputs = readline().split(' ');
    firstPictureRow.push(inputs[0]);
    secondPictureRow.push(inputs[1]);
}


console.error(W + ' ' + H + " " + T1 + " " + T2 + " " + T3);
// console.error(firstPictureRow + secondPictureRow);
// console.error(secondPictureRow);

for (let i = 0; i < firstPictureRow.length; i++){
    console.error(firstPictureRow[i] + " " + secondPictureRow[i] + " " + Tx[i]);
}


function searchAstro(astro){
    for (let y = 0; y < H; y++){
        for (let x = 0; x < W; x++){
            if (astro == secondPictureRow[y][x]){
                //console.error(astro + " T2" + " x : " + x + " y : " + y);
                return [x, y];
            }
        }
    }
}




for (let y = 0; y < H; y++){
    for (let x = 0; x < W; x++){
        if (firstPictureRow[y][x] != '.'){
            let astro = firstPictureRow[y][x];

            // test  *******
            // if (astro != 'K'){
            //     continue;
            // }
            // ***************


            let astroT2 = searchAstro(astro);

            console.error(astro + " T1" + " x : " + x + " y : " + y);
            console.error(astro + " T2" + " x : " + astroT2[0] + " y : " + astroT2[1]);

            let vector = [(astroT2[0] - x) / (T2 - T1), (astroT2[1] - y) / (T2 - T1)];
            console.error("vector " + astro + " x : " + vector[0] + " y : " + vector[1]);



            let X = (x + (vector[0] * (T3 - T1))); //  % (W);
            let Y = (y + (vector[1] * (T3 - T1))); //  % (H);

            console.error(astro + " XY" + " x : " + X + " y : " + Y );

            if (X < 0 || Y < 0 || X > W || Y > H){
                continue;
            }

            X = Math.floor(x + (vector[0] * (T3 - T1))); //  % (W);
            Y = Math.floor(y + (vector[1] * (T3 - T1))); //  % (H);


            let astroT3 = [X, Y];
            console.error(astro + " T3" + " x : " + astroT3[0] + " y : " + astroT3[1]);

            //Tx[astroT3[1]] = Tx[astroT3[1]].replace(Tx[y][astroT3[0]], astro);

            let tempTab = [];
            for (let k = 0; k < H; k++){
                if (Y != k){
                    tempTab.push(Tx[k]);
                }
                else {
                    let tempString = "";
                    for (let l = 0; l < W; l++){
                        if (X != l){
                            tempString += Tx[k][l];
                        }
                        else {



                            if (Tx[k][l] == '.'){
                                tempString += astro;
                            }
                            else if (astro < Tx[k][l]){
                                tempString += astro;
                            }
                            else{
                                tempString += Tx[k][l];
                            }                            
                        }
                    }
                    tempTab.push(tempString);
                }
            }
            Tx = tempTab;







        //     Tx[astroT3[1]] = Tx[astroT3[1]].replace(string[astroT3[0]], astro);
        //    if (Tx[astroT3[1]][astroT3[0]] != astro){
        //         console.error(" ******* " + astro + " ++++++++ Tx : " + Tx[astroT3[1]][astroT3[0]]);
        //         if (astro < Tx[astroT3[1]][astroT3[0]]){
        //             Tx[astroT3[1]] = Tx[astroT3[1]].replace(Tx[astroT3[1]][astroT3[0]], astro);
        //         }
        //    }





          // else{
              //  console.error(" ////////" + astro + " ++++++++ Tx : " + Tx[astroT3[1]][astroT3[0]]);
          // }

        }
    }
}

// for (let i = 0; i < H; i++){
//     for (let y = 0; y < W; y++){
//         Tx[i] = Tx[i].replace(string[y], '.');

//     }
    

// }


for (let i = 0; i < H; i++){
    console.log(Tx[i]);
}

// Write an answer using console.log()
// To debug: console.error('Debug messages...');

//console.log('answer');


// *******************************************************************************************


// const [W, H, T1, T2, T3] = readline().split(' ').map(Number), asteroids = [], pic2 = [];
// for (let y = 0; y < H; y++) {
//     const row = readline().replace(/\s/g, '');
//     const matches = row.slice(0, W).matchAll(/\w/g);
//     for (const match of matches)
//         asteroids.push([match[0], match.index, y]);
//     pic2[y] = row.slice(W);
// }
// const pic3 = [...Array(H)].map(_ => '.'.repeat(W).split(''));
// for (const [label, x1, y1] of asteroids) {
//     const [x2, y2] = pic2.map((row, y) => [row.indexOf(label), y]).find(pos => pos[0] !== -1);
//     const x3 = Math.floor(x1 + (T3 - T1) * (x2 - x1) / (T2 - T1));
//     const y3 = Math.floor(y1 + (T3 - T1) * (y2 - y1) / (T2 - T1));
//     if (x3 >= 0 && x3 < W && y3 >= 0 && y3 < H && (pic3[y3][x3] == '.' || label < pic3[y3][x3]))
//         pic3[y3][x3] = label;
// }
// console.log(pic3.map(row => row.join('')).join('\n'));