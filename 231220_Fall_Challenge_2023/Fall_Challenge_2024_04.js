/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Fall_Challenge_2024_04.js                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/01/04 07:19:25 by pwolff            #+#    #+#             */
/*   Updated: 2024/01/04 07:19:41 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Score points by scanning valuable fish faster than your opponent.
 **/
let mouveX = [600, 600];
let mouveY = [600, 600];
let x = 0;
let y = 0;
let light = 0;
let countTours = 0;


const creatureCount = parseInt(readline());
for (let i = 0; i < creatureCount; i++) {
    var inputs = readline().split(' ');
    const creatureId = parseInt(inputs[0]);
    const color = parseInt(inputs[1]);
    const type = parseInt(inputs[2]);
}

// game loop
while (true) {
    countTours++;
    let tabDrone = new Array();
    const myScore = parseInt(readline());
    const foeScore = parseInt(readline());
    const myScanCount = parseInt(readline());
    for (let i = 0; i < myScanCount; i++) {
        const creatureId = parseInt(readline());
    }
    const foeScanCount = parseInt(readline());
    for (let i = 0; i < foeScanCount; i++) {
        const creatureId = parseInt(readline());
    }
    const myDroneCount = parseInt(readline());
    console.error("myDroneCount : " + myDroneCount);
    for (let i = 0; i < myDroneCount; i++) {
        var inputs = readline().split(' ');
        let drone = {
            droneId : parseInt(inputs[0]),
            droneX : parseInt(inputs[1]),
            droneY : parseInt(inputs[2]),
            emergency : parseInt(inputs[3]),
            battery : parseInt(inputs[4])

        }
        console.error("Done : X : " + drone.droneX + " Y : " + drone.droneY);
        //tabDrone[i] = drone;
        tabDrone.push(drone);
    }
    //console.error("Done[0] : X : " + tabDrone[0].droneX + " Y : " + tabDrone[0].droneY);
    console.error(tabDrone);
    console.error("Done[0] : X : " + tabDrone[0].droneX + " Y : " + tabDrone[0].droneY);



    const foeDroneCount = parseInt(readline());
    for (let i = 0; i < foeDroneCount; i++) {
        var inputs = readline().split(' ');
        const droneId = parseInt(inputs[0]);
        const droneX = parseInt(inputs[1]);
        const droneY = parseInt(inputs[2]);
        const emergency = parseInt(inputs[3]);
        const battery = parseInt(inputs[4]);
    }
    let scanCount = [0,0];
    droneScanCount = parseInt(readline());
    for (let i = 0; i < droneScanCount; i++) {
        var inputs = readline().split(' ');
        const droneId = parseInt(inputs[0]);
        const creatureId = parseInt(inputs[1]);
        console.error("droneId : " + droneId + " -- creatureId : " + creatureId);
        if (droneId == 0){
            scanCount[0] += 1;
        }
        else if (droneId == 2){
            scanCount[1] += 1;
        }
    }
    const visibleCreatureCount = parseInt(readline());
    for (let i = 0; i < visibleCreatureCount; i++) {
        var inputs = readline().split(' ');
        const creatureId = parseInt(inputs[0]);
        const creatureX = parseInt(inputs[1]);
        const creatureY = parseInt(inputs[2]);
        const creatureVx = parseInt(inputs[3]);
        const creatureVy = parseInt(inputs[4]);
    }
    const radarBlipCount = parseInt(readline());
    for (let i = 0; i < radarBlipCount; i++) {
        var inputs = readline().split(' ');
        const droneId = parseInt(inputs[0]);
        const creatureId = parseInt(inputs[1]);
        const radar = inputs[2];
    }
    for (let i = 0; i < myDroneCount; i++) {

        x = tabDrone[i].droneX + mouveX[i];
        y = tabDrone[i].droneY + mouveY[i];
        light = 1;

        if (x > 9000){
            x = 9000;
            mouveX[i] = -600;
        }
        if (x < 1000){
            x = 1000;
            mouveX[i] = 600;
        }
        if (y > 9500){
            y = 9500;
            mouveY[i] = -600;
        }
        if (y < 3000){
            y = 3000;
            mouveY[i] = 600;
            light = 0;
        }
        if (scanCount[i] > 1 || countTours > 180){
            y = 0;
            light = 0;
        }
        console.error("droneScanCount : " + droneScanCount);
        console.error("myScanCount : " + myScanCount);
        console.error("scanCount[0] : " + scanCount[0]);
        console.error("scanCount[1] : " + scanCount[1]);

        // Write an action using console.log()
        // To debug: console.error('Debug messages...');

        //console.log('WAIT 1');         // MOVE <x> <y> <light (1|0)> | WAIT <light (1|0)>
        console.log("MOVE " + x + " " + y + " " + light);

    }
}
