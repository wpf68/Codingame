/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*    Logic_gates_.js                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/11/27 08:29:46 by pwolff            #+#    #+#             */
/*   Updated: 2023/11/27 08:41:37 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const n = parseInt(readline());
const m = parseInt(readline());
console.error("n = " + n);
console.error("m = " + m);
let tableCode = [];
let testLogique = [];


for (let i = 0; i < n; i++) {
    var inputs = readline().split(' ');
    tableCode.push(inputs);
    const inputName = inputs[0];
    const inputSignal = inputs[1];
    //console.error(i + " inputs = " + inputs);
    //console.error(i + " inputName = " + inputName);
    //console.error(i + " inputSignal = " + inputSignal);
}

function displayTableCode (tableCode){
    for (let i = 0; i < tableCode.length; i++){
        console.error(i + " inputs = " + tableCode[i]);
    }
}

function test(){
    console.log('*************************');
    for (let i = 0; i < val.length; i++){
        console.log(val.at(i));
        val.replace(val[i], 'l');
    }
    console.log(val);
    console.log('*************************');
}


function binaire (tableCode){
    for (let i = 0; i < tableCode.length; i++){
        let temp = "";
        //console.error(temp + " : " + temp.length + typeof(temp));
        for (let j = 0; j < tableCode[i][1].length; j++){
            if (tableCode[i][1][j] == '-'){
                temp += '1';
            }
            else if (tableCode[i][1][j] == '_') {
               temp += '0'; 
            }
        }
        tableCode[i][1] = temp;
        //console.error(temp + " : " + temp.length);
    }
}

//test();
displayTableCode(tableCode);
binaire(tableCode);
displayTableCode(tableCode);

for (let i = 0; i < m; i++) {
    var inputs = readline().split(' ');
    testLogique.push(inputs);
    const outputName = inputs[0];
    const type = inputs[1];
    const inputName1 = inputs[2];
    const inputName2 = inputs[3];
    //console.error(i + " Test inputs = " + inputs);
}

displayTableCode(testLogique);

function stringTest(inputTest){
    let result = "";
    console.error("input Test = " + inputTest);
    for (let i = 0; i < tableCode.length; i++){
        if (inputTest == tableCode[i][0]){
            result = tableCode[i][1];
        }
    }

    return result;
}

function testAND(name, inputA, inputB){
    let result = name + " ";

    for (let i = 0; i < inputA.length; i++){
        if (+inputA[i] && +inputB[i]){
            result += '-';
        }
        else {
            result += '_';
        }
    }
    return result;
}

function testOR(name, inputA, inputB){
    let result = name + " ";

    for (let i = 0; i < inputA.length; i++){
        if (+inputA[i] || +inputB[i]){
            result += '-';
        }
        else {
            result += '_';
        }
    }
    return result;
}

function testXOR(name, inputA, inputB){
    let result = name + " ";

    for (let i = 0; i < inputA.length; i++){
        if (+inputA[i] ^ +inputB[i]){
            result += '-';
        }
        else {
            result += '_';
        }
    }
    return result;
}

function testNAND(name, inputA, inputB){
    let result = name + " ";

    for (let i = 0; i < inputA.length; i++){
        if (+inputA[i] &&  +inputB[i]){
            result += '_';
        }
        else {
            result += '-';
        }
    }
    return result;
}

function testNOR(name, inputA, inputB){
    let result = name + " ";

    for (let i = 0; i < inputA.length; i++){
        if (+inputA[i] || +inputB[i]){
            result += '_';
        }
        else {
            result += '-';
        }
    }
    return result;
}

function testNXOR(name, inputA, inputB){
    let result = name + " ";

    for (let i = 0; i < inputA.length; i++){
        if (+inputA[i] ^ +inputB[i]){
            result += '_';
        }
        else {
            result += '-';
        }
    }
    return result;
}


for (let i = 0; i < m; i++) {
    let inputA = stringTest(testLogique[i][2]);
    let inputB = stringTest(testLogique[i][3]);

    let result = "";

    console.error('Input A = ' + inputA);
    console.error('Input B = ' + inputB);

    if (testLogique[i][1] == 'AND'){
        result = testAND(testLogique[i][0], inputA, inputB);
    }
    else if (testLogique[i][1] == 'OR'){
        result = testOR(testLogique[i][0], inputA, inputB);
    }
    else if (testLogique[i][1] == 'XOR'){
        result = testXOR(testLogique[i][0], inputA, inputB);
    }
    else if (testLogique[i][1] == 'NAND'){
        result = testNAND(testLogique[i][0], inputA, inputB);
    }
    else if (testLogique[i][1] == 'NOR'){
        result = testNOR(testLogique[i][0], inputA, inputB);
    }
    else if (testLogique[i][1] == 'NXOR'){
        result = testNXOR(testLogique[i][0], inputA, inputB);
    }
    // Write an answer using console.log()
    // To debug: console.error('Debug messages...');

    console.log(result);
}






// ******************************************************************************************

// let sToV = new Map([['_', 0], ['-', 1]]);
// let vToS = new Map([[0, '_'], [1, '-'],[false, '_'], [true, '-']]);
// let nToS = new Map();

// const AND  = (v1, v2) => v1.map((v, idx) => v && v2[idx])
// const OR   = (v1, v2) => v1.map((v, idx) => v || v2[idx])
// const XOR  = (v1, v2) => v1.map((v, idx) => v ^ v2[idx])
// const NAND = (v1, v2) => v1.map((v, idx) => !(v && v2[idx]))
// const NOR  = (v1, v2) => v1.map((v, idx) => !(v || v2[idx]))
// const NXOR = (v1, v2) => v1.map((v, idx) => !(v ^ v2[idx]))

// let ops = new Map(Object.entries({AND, OR, XOR, NAND, NOR, NXOR}));

// const nIn = parseInt(readline()), nOut = parseInt(readline());
// [...Array(nIn)].forEach(_ => {
//     let [name, signal] = readline().split(' ');
//     let v = signal.split('').map(x => sToV.get(x));
//     nToS.set(name, v);
// });

// let result = [...Array(nOut)].map(_ => {
//     const [n, op, n1, n2] = readline().split(' ');
//     let fn = ops.get(op), v1=nToS.get(n1), v2=nToS.get(n2);
//     let r = fn(v1,v2).map(x => vToS.get(x)).join('');
//     return `${n} ${r}`;
// });

// print(result.join('\n'))
