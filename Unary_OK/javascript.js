/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   javascript.js                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/06/01 09:23:57 by pwolff            #+#    #+#             */
/*   Updated: 2023/06/01 09:32:38 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// Write an answer using console.log()
// To debug: console.error('Debug messages...');


const MESSAGE = readline();
let     codeBinaire = "";
let     temp = "";
let     Unary = "";

for (let i = 0; i < MESSAGE.length; i++)
{
    let codeAscii = MESSAGE.charCodeAt(i);
    temp = codeAscii.toString(2);
    while (temp.length < 7){
        temp = "0" + temp;
    }
    // console.error(temp);
    codeBinaire += temp;
    
}
console.error(codeBinaire);
let i = 0;
while (i < codeBinaire.length){
    temp = "";
    if (codeBinaire[i] === '1')
        Unary += '0 ';
    else
        Unary += '00 ';
    
    let j = i;
    while (j < codeBinaire.length && codeBinaire[i] === codeBinaire[j]){
        temp += "0";
        j++;
    }
    i = j;
    Unary += temp;
    if (i < codeBinaire.length)
        Unary += ' ';
}


console.log(Unary);




// **********************************

// var MESSAGE = readline().match(/./g);

// var result = 
// MESSAGE.map(c => ("00000000" + c.charCodeAt().toString(2)).slice(-7))
// .join('')
// .match(/([1]+|[0]+)/g)
// .map(e => (e.charAt(0) == 1 ? '0 ' : '00 ') + '0'.repeat(e.length))
// .join(' ');

// print(result);


// **********************************