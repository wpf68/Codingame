/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   EncryptionDecryptionOfEnigmaMachine.js             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/17 10:02:55 by pwolff            #+#    #+#             */
/*   Updated: 2023/12/17 10:39:34 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let tabRotor = [];



//const operation = "ENCODE"; //readline();
const operation = "DECODE"; //readline();
const pseudoRandomNumber = 4; //parseInt(readline());

// for (let i = 0; i < 3; i++) {
//     const rotor = readline();
//     tabRotor.push(rotor);
// }

tabRotor.push("BDFHJLCPRTXVZNYEIWGAKMUSQO");
tabRotor.push("AJDKSIRUXBLHWTMCQGZNPYFVOE");
tabRotor.push("EKMFLGDQVZNTOWYHXUSPAIBRCJ");

//const message = "AAA"; //readline();
const message = "KQF"; //readline();






console.error("operation : " + operation);
console.error("Pseudo nb : " + pseudoRandomNumber);
console.error("Tab Rotor : " + tabRotor);
console.error("Message : " + message);

// Write an answer using console.log()
// To debug: console.error('Debug messages...');


// cherche first letters

let result = "";
if (operation == "ENCODE"){
    let temp = "";
    for (let i = 0; i < message.length; i++){
        let indice = alpha.indexOf(message[i]) + i;
        temp += alpha[(indice + pseudoRandomNumber) % 26]
    }
    console.error("\n*******************************\n");

    result = temp;
    console.error("result : " + result);

    for (let i = 0; i < 3; i++){
        temp = "";
        for (let j = 0; j < result.length; j++){
            let indice = alpha.indexOf(result[j]);
            temp += tabRotor[i][indice];
        }
        result = temp;
        console.error(i + " result : " + result);
    }
}
else {
    result = message;
    let temp = "";
    for (let i = 2; i >= 0; i--){
        temp = "";
        for (let j = 0; j < result.length; j++){
            let indice = tabRotor[i].indexOf(result[j]);
            temp += alpha[indice];
        }
        result = temp;
        console.error(i + " result : " + result);
    }
    temp = "";
    for (let i = 0; i < result.length; i++){
        let indice = alpha.indexOf(result[i]);
        let index = (indice - pseudoRandomNumber - i) % 26;
        if (index < 0){
            index = 26 + index;
        }
        console.error(index);
        temp += alpha[index];
    }
    result = temp;
}

console.log(result);




// *****************************************************

// const mod = (n, m) => {
//     const remainder = n % m;
//     return Math.floor(remainder >= 0 ? remainder : remainder + m);
// };
// const operation = readline();
// const pseudoRandomNumber = +readline();
// const rotors = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ'];
// for (let i = 0; i < 3; i++) {
//     rotors.push(readline());
// }
// const message = readline();
// let result;
// if (operation === 'ENCODE') {
//     result = [...message].map((c, i) => {
//         let caesar = mod(rotors[0].indexOf(c) + pseudoRandomNumber + i, 26);
//         console.error(c, caesar);
//         for (let i = 1; i < 4; i++) {
//             caesar = rotors[0].indexOf(rotors[i][caesar]);
//         }
//         return rotors[0][caesar];
//     }).join('');
// } else {
//     result = [...message].map((c, i) => {
//         let caesar = rotors[3].indexOf(c);
//         for (let i = 2; i >= 0; i--) {
//             caesar = rotors[i].indexOf(rotors[0][caesar]);
//         }
//         const base = mod(caesar - pseudoRandomNumber - i, 26);
//         return rotors[0][base];
//     }).join('');
// }
// console.log(result);


// **********************************************************************



// const operation = readline();
// const pseudo = +readline();
// mod = (n, p) => {
//     if ( n < 0 )
//         n = p - Math.abs(n) % p;
//     return n % p;
// }
// const rotor = [];
// for (i=0;i<3;i++) {
//     rotor[i] = readline();
// }
// const message = readline().split("");
// if(operation==="ENCODE"){
//     for(i=0;i<message.length;i++){
//         message[i]=String.fromCharCode(mod((message[i].charCodeAt()-65+pseudo+i),26)+65);
//         for(j=0;j<rotor.length;j++){
//             message[i]=rotor[j][(message[i].charCodeAt()-65)%26];
//         }
//     }
// } else {
//     for(i=0;i<message.length;i++){
//         for(j=rotor.length-1;j>=0;j--){
//             message[i]=String.fromCharCode(rotor[j].indexOf(message[i])+65);
//         }
//         message[i]=String.fromCharCode(mod(message[i].charCodeAt() - (pseudo+i) - 65,26) + 65);
//     }
// }
// console.log(message.join(""));


// **********************************************************************

// const op = readline();
// const N = +readline();
// const rotors = Array(3).fill('').map(readline)
// let message = readline().split('');

// if (op === 'ENCODE') {
//     // Shift by N.
//     // 1) +/- 65: Map Unicode value to corresponding value of the alphabet.
//     // 2) n % 26: Handle overflow of the alphabet, i.e. ... > Y > Z > A > B ...
//     message = message.map((m, i) => String.fromCharCode((m.charCodeAt(0) - 65 + N + i) % 26 + 65))
//     // Apply rotors.
//     // - 65: Map Unicode value to corresponding value of the alphabet.
//     message = rotors.reduce((acc, r) => acc.map(m => r[m.charCodeAt(0) - 65]), message);
// } else {
//     // Apply rotors in reverse order.
//     // + 65: Map Unicode value to corresponding value of the alphabet.
//     message = rotors.reduceRight((acc, r) => acc.map(m => String.fromCharCode(r.indexOf(m) + 65)), message);
//     // Reverse-shift by N.
//     // 1) +/- 65: Map Unicode value to corresponding value of the alphabet.
//     // 2) (n % 26 + 26) % 26: Handle underflow of the alphabet, i.e. ... > B > A > Z > Y ...
//     message = message.map((m, i) => String.fromCharCode(((m.charCodeAt(0) - 65 - N - i) % 26 + 26) % 26 + 65));
// }

// print(message.join(''))