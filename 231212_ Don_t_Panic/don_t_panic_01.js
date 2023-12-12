/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   don_t_panic_01.js                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/12 08:55:51 by pwolff            #+#    #+#             */
/*   Updated: 2023/12/12 08:56:21 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/


let tabElevator = [];

var inputs = readline().split(' ');
const nbFloors = parseInt(inputs[0]); // number of floors
const width = parseInt(inputs[1]); // width of the area
const nbRounds = parseInt(inputs[2]); // maximum number of rounds
const exitFloor = parseInt(inputs[3]); // floor on which the exit is found
const exitPos = parseInt(inputs[4]); // position of the exit on its floor
const nbTotalClones = parseInt(inputs[5]); // number of generated clones
const nbAdditionalElevators = parseInt(inputs[6]); // ignore (always zero)
const nbElevators = parseInt(inputs[7]); // number of elevators
for (let i = 0; i < nbElevators; i++) {
    let Elevator = {};
    var inputs = readline().split(' ');
    //const elevatorFloor = parseInt(inputs[0]); // floor on which this elevator is found
    Elevator.floor = parseInt(inputs[0]);
    //const elevatorPos = parseInt(inputs[1]); // position of the elevator on its floor
    Elevator.pos = parseInt(inputs[1]);

    tabElevator[i] = Elevator;

    //console.error(i + " - Elevator Floor: " + elevatorFloor + " - Pos : " + elevatorPos);
    console.error(i + " Elevator : Floor " + tabElevator[i].floor + " - Pos : " + tabElevator[i].pos);
}

// *************  test
console.error("************ test ************");
for (let i = 0; i < nbElevators; i++){

    console.error(i + " Elevator : Floor " + tabElevator[i].floor + " - Pos : " + tabElevator[i].pos);

}




//console.table(" ***** Elevator : " + tabElevator);
console.error("Nbr d'etages : " + nbFloors + " -- Largeur Max : " + width + " -- Nbr de tours : " + nbRounds); 
console.error("Aspirateur : Etage : " + exitFloor + " -- Pos : " + exitPos);
console.error("Nbr de clones : " + nbTotalClones + " -- Nbr d'ascenseurs : " + nbElevators);


// game loop
while (true) {
    let result = "WAIT";
    var inputs = readline().split(' ');
    const cloneFloor = parseInt(inputs[0]); // floor of the leading clone
    const clonePos = parseInt(inputs[1]); // position of the leading clone on its floor
    const direction = inputs[2]; // direction of the leading clone: LEFT or RIGHT

    console.error("Clone : Floor : " + cloneFloor + " - Pos : " + clonePos + " - direction : " + direction);


    //test si ascenseur sur etage
    if (cloneFloor > -1 && cloneFloor < nbElevators){
        let indexFloor = 0;
       // console.error("**** CloneFloor : " + cloneFloor + " ** nbElevators : " + nbElevators );
        for (let i = 0; i < nbElevators; i++){
           // console.error("========= Floor Elevator : " + tabElevator[i] + "   clone Floor : " + cloneFloor);
            if (tabElevator[i].floor == cloneFloor){
                //console.error("****** Match Floor **********");
                indexFloor = i;
                break;
            }
        }
        
        console.error("++++ Elevator : Floor " + tabElevator[indexFloor].floor + " - Pos : " + tabElevator[indexFloor].pos + "  indexFloor = " + indexFloor) ;
       // console.error("*********** Pos Clone : " + clonePos + "  Pos Elevator : " + tabElevator[indexFloor].Pos);
        if (tabElevator[indexFloor].pos - clonePos < 0 && direction == "RIGHT"){
            result = "BLOCK";
        }
        else if (tabElevator[indexFloor].pos - clonePos > 0 && direction == "LEFT"){
            result = "BLOCK";
        }


    }
    //plus d'ascenseurs --> cherche sortie

    else if (cloneFloor > -1){
        if (exitPos - clonePos < 0 && direction == "RIGHT"){
            result = "BLOCK";
        }
        else if (exitPos - clonePos > 0 && direction == "LEFT"){
            result = "BLOCK";
        }



    }
    // else {
    
    //     if (direction == "RIGHT" && clonePos >= width - 1){
    //         result = "BLOCK";
    //     }
    //     else if (direction == "LEFT" && clonePos <= 0){
    //         result = "BLOCK";
    //     }
    // }



    // Write an action using console.log()
    // To debug: console.error('Debug messages...');

    console.log(result);     // action: WAIT or BLOCK

}
