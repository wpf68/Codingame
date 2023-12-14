/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*    abcdefghijklmnopqrstuvwxyz.js                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/10 08:43:31 by pwolff            #+#    #+#             */
/*   Updated: 2023/12/10 08:43:47 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const n = parseInt(readline());
let tab = "";
let result = "";
for (let i = 0; i < n; i++) {
    const m = readline();
    tab += m + "\n";
}

function initResult(){
    for (let i = 0; i < n; i++){
        for (let j = 0; j < n; j++){
            result += "-";
        }
        if (i != n - 1){
            result += "\n";
        }
    }
}

initResult();


console.error(n);
console.error(tab);
console.error(result);
console.error();

let x = 0;
let y = 0;
const alpha = "abcdefghijklmnopqrstuvwxyz";
let index = 0;

while (true){
    
    //console.error (tab[y * (n + 1) + x] + " - x : " + x + " - Y : " + y);
    if (tab[y * (n + 1) + x] == alpha[index]){
        let temp = "";
        //console.error ("** " + tab[y * (n + 1) + x] + " - x : " + x + " - Y : " + y);
        //result[y * (n + 1) + x] = alpha[index];
        //console.error(result[y * (n + 1) + x]);


        for (let i = 0; i < n; i++){
            for (let j = 0; j < n; j++){
                if (i == y && j == x){
                    temp += alpha[index];
                }
                else {
                    temp += result[i * (n + 1) + j];
                }
                
            }
            if (i != n - 1){
                temp += "\n";
            }
        }
        //result = "";
        result = temp;
        //console.log("result \n" + result);
        //console.log("temp \n" + temp);

        if (index < alpha.length - 1){
            index++;
            if (x < n - 1 && tab[y * (n + 1) + x + 1] == alpha[index]){
                x++;
                continue;
            }
            else if (x > 0 && tab[y * (n + 1) + x - 1] == alpha[index]){
                x--;
                continue
            }
            else if (y > 0 && tab[(y - 1) * (n + 1) + x] == alpha[index]){
                y--;
                continue;
            }
            else if (y < n - 1 && tab[(y + 1) * (n + 1) + x] == alpha[index]){
                y++;
                continue;
            }
            else {
                let returnIndex = result.indexOf("a");
                console.error("**  " + returnIndex);
                y = Math.trunc(returnIndex / (n + 1));
                x = returnIndex - y * (n + 1);
                console.error("x : " + x + " y : " + y);
                if (x < n - 1){
                    x++;
                    result = "";
                    initResult();
                    index = 0;
                    console.error("------ x : " + x + " y : " + y);
                    continue;
                }
                else {
                    x = 0;
                    y++;
                    result = "";
                    initResult();
                    index = 0;
                    console.error("++++++++ x : " + x + " y : " + y);
                    continue;
                }
                   
            }



        }
        else {
            break;
        }

    }
    if (x < n - 1){
        x++;
        //console.error (" - x : " + x + " - Y : " + y);
        continue
    }
    else {
        x = 0;
    }
    if (y < n - 1){
        y++;
    }
    else {
        break;
    }
}

// Write an answer using console.log()
// To debug: console.error('Debug messages...');



console.log(result);


// **********************************************************************

// var [o, g, f] = [
//     ...[...Array(+readline())].reduce(
//         (p, _, i) => p[1].push(
//             [...readline()].map(
//                 (e, j) => (e !== 'a' || p[0].push([i, j])) && e.charCodeAt()
//             )
//         ) && p, [[], []]
//     ), (y, x, a = []) => a.push(`${y} ${x}`) && g[y][x] === 122 ? a : [
//         [y - 1, x], [y + 1, x],
//         [y, x - 1], [y, x + 1]
//     ].reduce(
//         (p, [Y, X]) => g[Y]?.[X] - 1 !== g[y][x] ? p : f(Y, X, [...a]), null
//     )
// ];

// var t = o.reduce((p, [y, x]) => p || f(y, x), null);

// console.log(
//     g.map(
//         (e, i) => e.map(
//             (f, j) => t.includes(`${i} ${j}`) ? String.fromCharCode(f) : '-'
//         ).join('')
//     ).join('\n')
// );