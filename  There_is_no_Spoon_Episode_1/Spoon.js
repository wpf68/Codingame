/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Spoon.js                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/07 08:44:49 by pwolff            #+#    #+#             */
/*   Updated: 2023/07/07 08:50:42 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Don't let the machines win. You are humanity's last hope...
 **/

const width = parseInt(readline()); // the number of cells on the X axis
const height = parseInt(readline()); // the number of cells on the Y axis

let tab = new Array(height);

// console.error(`Largeur x = ${width}`);
// console.error(`Hauteur Y = ${height}`);

// function displayTab(){
//     console.error("\n********************");
//     console.error("***      tab     ***");
//     console.error("********************\n");
//     for (let i = 0; i < height; i++){
//         console.error(tab[i]);
//     }
//     console.error("");
// }

for (let i = 0; i < height; i++) {
    const line = readline(); // width characters, each either 0 or .
    // console.error(`Readline ${i} = ${line}`);
    tab[i] = line;
}

function    testNoeud(result, x, y){
    let test = 1;
    for (i = x + 1; i < tab[y].length; i++){
        if (tab[y][i] === '0'){
            result += ` ${i} ${y}`;
            test = 0;
            break;
        }
    }
    if (test)
        result += ` -1 -1`;
    test = 1;
    for (i = y + 1; i < height; i++){
        if (tab[i][x] === '0'){
            result += ` ${x} ${i}`;
            test = 0;
            break;
        }
    }
    if (test)
        result += ` -1 -1`;
    return result;
}

// displayTab();

for (let y = 0; y < height; y++){
    let result = "";
    for (let x = 0; x < tab[y].length; x++){
        if (tab[y][x] === '0'){
            result = `${x} ${y}`;
            result = testNoeud(result, x, y);
            console.log(result);
        }
    }
}

// Write an action using console.log()
// To debug: console.error('Debug messages...');


// Three coordinates: a node, its right neighbor, its bottom neighbor


// ****************************************
// ****************************************
// ****************************************

// const width = +readline();
// const height = +readline();
// const grid = new Array(height).fill().map(e => readline().split('').map(c => c === '0')); //[y][x]
// const processedCoords = {};

// const computeNode = (x, y) => {
//     if (!processedCoords[`${x} ${y}`] && grid[y][x]) {
//         // Getting the closest right neighbor...
//         let i = 1;
//         while(x + i < grid[y].length && !grid[y][x + i]) {i++;}
//         const posX = x + i >= grid[y].length ? '-1 -1' : `${x + i} ${y}`;

//         // Getting the closest bottom neighbor...
//         let j = 1;
//         while(y + j < grid.length && !grid[y + j][x]) {j++;}
//         const posY = y + j >= grid.length ? '-1 -1' : `${x} ${y + j}`;

//         print(`${x} ${y} ${posX} ${posY}`);
//         processedCoords[`${x} ${y}`] = true;
//     }
// }

// grid.map((lines, y) => lines.map((element, x) => computeNode(x, y)));