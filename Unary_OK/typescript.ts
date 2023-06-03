/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   typescript.ts                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/06/03 08:43:39 by pwolff            #+#    #+#             */
/*   Updated: 2023/06/03 08:44:14 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const MESSAGE: string = readline();

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

 let     codeBinaire = "";
 let     temp = "";
 let     Unary = "";
 
 // Write an answer using console.log()
 // To debug: console.error('Debug messages...');
 
 for (let i = 0; i < MESSAGE.length; i++)
 {
     let codeAscii = MESSAGE.charCodeAt(i);
     temp = codeAscii.toString(2);
     while (temp.length < 7){
         temp = "0" + temp;
     }

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