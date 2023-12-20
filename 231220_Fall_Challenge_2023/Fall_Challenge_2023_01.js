/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Fall_Challenge_2023_01.js                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/20 08:13:43 by pwolff            #+#    #+#             */
/*   Updated: 2023/12/20 08:14:10 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Score points by scanning valuable fish faster than your opponent.
 **/
let tabCreatures = [];



const creatureCount = parseInt(readline());
for (let i = 0; i < creatureCount; i++) {
    var inputs = readline().split(' ');
    // const creatureId = parseInt(inputs[0]);
    // const color = parseInt(inputs[1]);
    // const type = parseInt(inputs[2]);

    let creature = {
        creatureId : parseInt(inputs[0]),
        color : parseInt(inputs[1]),
        type : parseInt(inputs[2])
    }
    tabCreatures.push(creature);
}


console.error("Nb creatures : " + creatureCount);

function displayTab(){
    for (let i = 0; i < tabCreatures.length; i++){
        console.error("Creature [" + i + "] \n - ID :" +  tabCreatures[i].creatureId +
        "\n - COLOR : " + tabCreatures[i].color + "\n - TYPE : " + tabCreatures[i].type + "\n") ;

    }
}
//displayTab();

// test splice

// tabCreatures.splice(2,1);
// for (let i = 0; i < tabCreatures.length; i++){
//     console.error("Creature [" + i + "] \n - ID :" +  tabCreatures[i].creatureId +
//     "\n - COLOR : " + tabCreatures[i].color + "\n - TYPE : " + tabCreatures[i].type + "\n") ;

// }



// game loop
while (true) {
    const myScore = parseInt(readline());
    const foeScore = parseInt(readline());

    console.error("Mon Score : " + myScore + " *** Adverse : " + foeScore);

    const myScanCount = parseInt(readline());
    for (let i = 0; i < myScanCount; i++) {
        const creatureId = parseInt(readline());
        console.error(" - MyScan[" + i + "] : creatureID = " + creatureId);
        for (let j = 0; j < tabCreatures.length; j++){
            if (tabCreatures[j].creatureId == creatureId){
                tabCreatures.splice(j,1);
                break;
            }
        }
    }

    //displayTab();

    const foeScanCount = parseInt(readline());
    for (let i = 0; i < foeScanCount; i++) {
        const creatureId = parseInt(readline());
        console.error(" - AdversaireScan[" + i + "] : creatureID = " + creatureId);
    }
    const myDroneCount = parseInt(readline());
    let tabDrones = [];
    for (let i = 0; i < myDroneCount; i++) {
        var inputs = readline().split(' ');
        let drone = {
            droneId : parseInt(inputs[0]),
            droneX : parseInt(inputs[1]),
            droneY : parseInt(inputs[2]),
            emergency : parseInt(inputs[3]),
            battery : parseInt(inputs[4])
        }
        tabDrones.push(drone);


        // const droneId = parseInt(inputs[0]);
        // const droneX = parseInt(inputs[1]);
        // const droneY = parseInt(inputs[2]);
        // const emergency = parseInt(inputs[3]);
        // const battery = parseInt(inputs[4]);

        // console.error("MyDrone[" + i + "][" + droneId + "] - X : " + droneX +
        // " - Y : " + droneY + " - Emergency : " + emergency + " - Batterry : " + battery);
    }
    const foeDroneCount = parseInt(readline());
    for (let i = 0; i < foeDroneCount; i++) {
        var inputs = readline().split(' ');
        const droneId = parseInt(inputs[0]);
        const droneX = parseInt(inputs[1]);
        const droneY = parseInt(inputs[2]);
        const emergency = parseInt(inputs[3]);
        const battery = parseInt(inputs[4]);

        // console.error("AdverseDrone[" + i + "][" + droneId + "] - X : " + droneX +
        // " - Y : " + droneY + " - Emergency : " + emergency + " - Batterry : " + battery);
    }
    const droneScanCount = parseInt(readline());
    for (let i = 0; i < droneScanCount; i++) {
        var inputs = readline().split(' ');
        const droneId = parseInt(inputs[0]);
        const creatureId = parseInt(inputs[1]);
    }
    const visibleCreatureCount = parseInt(readline());
    let tabCreaturePos = [];

    for (let i = 0; i < visibleCreatureCount; i++) {
        var inputs = readline().split(' ');
        let creature = {
            creatureId : parseInt(inputs[0]),
            creatureX : parseInt(inputs[1]),
            creatureY : parseInt(inputs[2]),
            creatureVx : parseInt(inputs[3]),
            creatureVy : parseInt(inputs[4])
        }
        tabCreaturePos.push(creature);
        // const creatureId = parseInt(inputs[0]);
        // const creatureX = parseInt(inputs[1]);
        // const creatureY = parseInt(inputs[2]);
        // const creatureVx = parseInt(inputs[3]);
        // const creatureVy = parseInt(inputs[4]);
    }

    // cherche creature la plus proche *****************************************************//

    let idCreatureProche = -1;
    let distance = 40000;
    for (let i = 0; i < tabCreatures.length; i++){
        for (let j = 0; j < tabCreaturePos.length; j++){
            if (tabCreatures[i].creatureId == tabCreaturePos[j].creatureId){
                let distDroneCreature = Math.sqrt((tabCreaturePos[j].creatureX - tabDrones[0].droneX) ** 2 + (tabCreaturePos[j].creatureY - tabDrones[0].droneY) ** 2);
                if (distDroneCreature < distance){
                    distance = distDroneCreature;
                    idCreatureProche = j;
                }
                break;
            }
        }
    }
    let x = tabCreaturePos[idCreatureProche].creatureX;
    let y = tabCreaturePos[idCreatureProche].creatureY;
    // let x = 5000;
    // let y = 5000;

    let light = 0;

    console.error("distance = " + distance);








    



    // ****************************************************************************************//



    const radarBlipCount = parseInt(readline());
    for (let i = 0; i < radarBlipCount; i++) {
        var inputs = readline().split(' ');
        const droneId = parseInt(inputs[0]);
        const creatureId = parseInt(inputs[1]);
        const radar = inputs[2];
    }
    for (let i = 0; i < myDroneCount; i++) {

        // Write an action using console.log()
        // To debug: console.error('Debug messages...');

        console.log("MOVE " + x + " " + y + " " + light);
        //console.log('WAIT 1');         // MOVE <x> <y> <light (1|0)> | WAIT <light (1|0)>

    }
}
