/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Tile_a_Floor.js                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/01/06 07:30:33 by pwolff            #+#    #+#             */
/*   Updated: 2024/01/06 07:42:25 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const N = parseInt(readline());
let tab01 = [];

function display(tab){
    for(let i = 0; i < tab.length; i++){
        console.error(tab[i]);
    }
}

function displayFinal(tab){
    for(let i = 0; i < tab.length; i++){
        console.log(tab[i]);
    }
}


function symetrie01(ROW){
    let temp = ROW;
    for (let i = ROW.length - 2; i >= 0; i--){
        if (ROW[i] == '['){
            temp += ']';
        }
        else if (ROW[i] == ']'){
            temp += '[';
        }
        else if (ROW[i] == '\\'){
            temp += '/';
        }
        else if (ROW[i] == '/'){
            temp += '\\';
        }
        else if (ROW[i] == '('){
            temp += ')';
        }
        else if (ROW[i] == ')'){
            temp += '(';
        }
        else if (ROW[i] == '{'){
            temp += '}';
        }
        else if (ROW[i] == '}'){
            temp += '{';
        }
        else if (ROW[i] == '<'){
            temp += '>';
        }
        else if (ROW[i] == '>'){
            temp += '<';
        }
        else {
            temp += ROW[i]
        }
        
    }
    return temp;
}

function symetrie01Down(tab){
    let temp = tab;
    for(let i = tab.length - 2; i >= 0; i--){
        let temp2 = "";
        for (let j = 0; j < tab[i].length; j++){
            if (tab[i][j] == 'A'){
                temp2 += 'V';
            }
            else if (tab[i][j] == 'V'){
                temp2 += 'A';
            }
            else if (tab[i][j] == '/'){
                temp2 += '\\';
            }
            else if (tab[i][j] == '\\'){
                temp2 += '/';
            }
            else if (tab[i][j] == 'u'){
                temp2 += 'n';
            }
            else if (tab[i][j] == 'n'){
                temp2 += 'u';
            }
            else if (tab[i][j] == 'W'){
                temp2 += 'M';
            }
            else if (tab[i][j] == 'M'){
                temp2 += 'W';
            }
            else if (tab[i][j] == 'w'){
                temp2 += 'm';
            }
            else if (tab[i][j] == 'm'){
                temp2 += 'w';
            }
            else if (tab[i][j] == 'v'){
                temp2 += '^';
            }
            else if (tab[i][j] == '^'){
                temp2 += 'v';
            }
            else{
                temp2 += tab[i][j];
            }
            
        }
        temp.push(temp2);
    }
    return temp;
}



console.error("N : " + N);
for (let i = 0; i < N; i++) {
    const ROW = readline();
    console.error("ROW [" + i + "] : " + ROW + "----");
    tab01.push(symetrie01(ROW));
}
console.error(tab01);
display(tab01);
console.error ("\n****** tab 01 ****\n");

tab01 = symetrie01Down(tab01);
display(tab01);

let tab02 = [];

for(let i = 0; i < tab01.length; i++){
    let temp = "";
    for (let j = tab01[i].length - 1; j >= 0; j--){
        if (tab01[i][j] == ']'){
            temp += '[';
        }
        else if (tab01[i][j] == '['){
            temp += ']';
        }
        else if (tab01[i][j] == '\\'){
            temp += '/';
        }
        else if (tab01[i][j] == '/'){
            temp += '\\';
        }
        else if (tab01[i][j] == '('){
            temp += ')';
        }
        else if (tab01[i][j] == ')'){
            temp += '(';
        }
        else if (tab01[i][j] == '{'){
            temp += '}';
        }
        else if (tab01[i][j] == '}'){
            temp += '{';
        }
        else if (tab01[i][j] == '<'){
            temp += '>';
        }
        else if (tab01[i][j] == '>'){
            temp += '<';
        }
        else {
            temp += tab01[i][j];
        }
        
    }
    tab02.push(temp);
}
console.error ("\n***** tab 02 *****\n");
display(tab02);

// Write an answer using console.log()
// To debug: console.error('Debug messages...');

//console.log('TileFloor');

let tab03 = [];

for (let i = tab01.length - 1; i >= 0; i--){
    let temp = "";
    for (let j = 0; j < tab01[i].length; j++){
        if (tab01[i][j] == 'A'){
            temp += 'V';
        }
        else if (tab01[i][j] == 'V'){
            temp += 'A';
        }
        else if (tab01[i][j] == '\\'){
            temp += '/';
        }
        else if (tab01[i][j] == '/'){
            temp += '\\';
        }
        else if (tab01[i][j] == 'u'){
            temp += 'n';
        }
        else if (tab01[i][j] == 'n'){
            temp += 'u';
        }
        else if (tab01[i][j] == 'W'){
            temp += 'M';
        }
        else if (tab01[i][j] == 'M'){
            temp += 'W';
        }
        else if (tab01[i][j] == 'w'){
            temp += 'm';
        }
        else if (tab01[i][j] == 'm'){
            temp += 'w';
        }
        else if (tab01[i][j] == 'v'){
            temp += '^';
        }
        else if (tab01[i][j] == '^'){
            temp += 'v';
        }
        else {
            temp += tab01[i][j];
        }
        
    }
    tab03.push(temp);
}

console.error ("\n***** tab03 *****\n");
display(tab03);

let tab04 = [];

for(let i = 0; i < tab03.length; i++){
    let temp = "";
    for (let j = tab03[i].length - 1; j >= 0; j--){
        if (tab03[i][j] == ']'){
            temp += '[';
        }
        else if (tab03[i][j] == '['){
            temp += ']';
        }
        else if (tab03[i][j] == '/'){
            temp += '\\';
        }
        else if (tab03[i][j] == '\\'){
            temp += '/';
        }
        else if (tab03[i][j] == '('){
            temp += ')';
        }
        else if (tab03[i][j] == ')'){
            temp += '(';
        }
        else if (tab03[i][j] == '{'){
            temp += '}';
        }
        else if (tab03[i][j] == '}'){
            temp += '{';
        }
        else if (tab03[i][j] == '<'){
            temp += '>';
        }
        else if (tab03[i][j] == '>'){
            temp += '<';
        }
        else {
            temp += tab03[i][j];
        }
    }
    tab04.push(temp);
}
console.error ("\n***** tab 04 *****\n");
display(tab04);

let tabFinal = [];

function ligne(){
    let temp = '+';
    for (let i = 0; i < tab01[0].length; i++){
        temp += '-'
    }
    temp += '+';
    for (let i = 0; i < tab01[0].length; i++){
        temp += '-'
    }
    temp += '+';
    return temp;
}


tabFinal.push(ligne());

for (let i = 0; i < tab01.length; i++){
    let temp = '|' + tab01[i] + '|' + tab02[i] + '|';
    tabFinal.push(temp);
}

tabFinal.push(ligne());

for (let i = 0; i < tab03.length; i++){
    let temp = '|' + tab03[i] + '|' + tab04[i] + '|';
    tabFinal.push(temp);
}

tabFinal.push(ligne());

console.error ("\n***** tabFinal *****\n");
displayFinal(tabFinal);



// ***************************************************************************************

// Array.prototype.inv=function (a,b) {return this.map(x=>x==a?b:x==b?a:x);}

// const N = parseInt(readline()), f=[];
// for (let i = 0; i < N; i++) {
//     const ROW = readline();
//     f.push(ROW + [...ROW].reverse()
//         .inv('(',')').inv('{','}').inv('[',']')
//         .inv('<','>').inv('/','\\').join('').substr(1));
// }
// for (let i = f.length-2 ; i>=0 ; i--) f.push([...f[i]]
//     .inv('^','v').inv('A','V').inv('w','m')
//     .inv('W','M').inv('u','n').inv('/','\\').join(''));
// const line = "+".padEnd(f[0].length,'-')+"-+-"+"+".padStart(f[0].length,'-');
// console.log(line);
// for (let r of f) console.log(`|${r}|${r}|`)
// console.log(line);
// for (let r of f) console.log(`|${r}|${r}|`)
// console.log(line);


// ***************************************************************************************

// class Mirror {

//     a;
//     b;

//     constructor(a,b) {
//         this.a = a;
//         this.b = b;
//     }

//     get(source) {
//         var index = this.a.indexOf(source);
//         if(index>-1) return this.b[index];

//         index = this.b.indexOf(source);
//         if(index>-1) return this.a[index];

//         return source;
//     }
// }

// var LEFT_RIGHT = new Mirror('({[</',')}]>\\');
// var TOP_BOTTOM = new Mirror('^AwWu/','vVmMn\\');


// var TILE = [];

// const N = parseInt(readline());
// var maxI = N*2-2;
// for (let i = 0; i < N; i++) {
//     var ROW = readline();
//     ROW += [...ROW.substring(0,ROW.length-1)].map(c=>LEFT_RIGHT.get(c)).reverse().join('');
//     TILE[i] = ('|'+ROW).repeat(2)+'|';
//     TILE[maxI-i] = ('|'+[...ROW].map(c=>TOP_BOTTOM.get(c)).join('')).repeat(2)+'|';
// }

// var borderH = ('+'+'-'.repeat(maxI+1)).repeat(2)+'+';

// console.log(borderH);
// console.log(TILE.join('\n'));
// console.log(borderH);
// console.log(TILE.join('\n'));
// console.log(borderH);


// ***************************************************************************************
