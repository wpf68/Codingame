/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   MIME_Type.js                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/09/28 10:56:22 by pwolff            #+#    #+#             */
/*   Updated: 2023/09/28 10:56:42 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const N = parseInt(readline()); // Number of elements which make up the association table.
const Q = parseInt(readline()); // Number Q of file names to be analyzed.

console.error("Nombre N d’éléments composant la table d'association :", {N});
console.error("Nombre Q de noms de fichiers à analyser              :", {Q});

let table = [];
let result = [];
let fichier = [];

console.error();
for (let i = 0; i < N; i++) {
    var inputs = readline().split(' ');
    const EXT = inputs[0]; // file extension
    const MT = inputs[1]; // MIME type.
    // console.error("Table ", i, ' : ',EXT, MT);
    table.push(EXT.toLocaleUpperCase());
    table.push(MT);
    // console.error("--", table);

}

for (let i = 0; i < N; i++)
{
    //table[i * 2] = table[i * 2].toUpperCase();
    console.error(table[i * 2], table[i * 2 +1]);

}


console.error();
for (let i = 0; i < Q; i++) {
    const FNAME = readline(); // One file name per line.
    // console.error("Fichier ", i, ' : ',FNAME);
    fichier.push(FNAME.toLocaleUpperCase());            
}
            
let test = 1;            
for (let i = 0; i < Q; i++) {
    console.error(fichier[i]);
    for (let j = 0; j < N; j++)
    {
        // if (fichier[i] === table[j * 2]){
        if (fichier[i].indexOf('.' + table[j * 2]) == fichier[i].length - table[j * 2].length - 1 && fichier[i].length > table[j * 2].length){
            result.push(table[j * 2 + 1]);
            test = 0;
            break;
        }
    }
    if (test){
        result.push('UNKNOWN');
    }
    test = 1;

}





console.error('=========================');


for (let i = 0; i < Q; i++)
{
    console.log(result[i]);

}
// Write an answer using console.log()
// To debug: console.error('Debug messages...');


// For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
// console.log('UNKNOWN');
