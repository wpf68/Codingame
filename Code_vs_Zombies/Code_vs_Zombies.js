/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Code_vs_Zombies.js                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/06 08:37:09 by pwolff            #+#    #+#             */
/*   Updated: 2023/12/06 09:29:23 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/**
 * Save humans, destroy zombies!
 **/


// game loop
while (true) {
    var inputs = readline().split(' ');
    const x = parseInt(inputs[0]);
    const y = parseInt(inputs[1]);
    const humanCount = parseInt(readline());

    let destHumanX = 0;
    let destHumanY = 0;

    console.error("x = " + x + " y = " + y + " vies : " + humanCount);

    let humans = [];  // Tableau d'objet d'humains

    for (let i = 0; i < humanCount; i++) {
        var inputs = readline().split(' ');
        let temp = {
            Id : parseInt(inputs[0]),
            x : parseInt(inputs[1]),
            y : parseInt(inputs[2])
        }
        humans.push(temp);
    }

        //console.error("ID : " + humanId + " humanX = " + humanX + " humanY = " + humanY);

    // console.error("*******  HUMAN Obj *********");
    // for (let i = 0; i < humans.length; i++){
    //     console.error("ID : " + humans[i].Id);
    //     console.error("X : " + humans[i].x + " Y :" + humans[i].y);
    // }

    const zombieCount = parseInt(readline());
    let zombies = [];       // Tableau d'objets Zombies

    for (let i = 0; i < zombieCount; i++) {
        var inputs = readline().split(' ');

        temp = {
            Id : parseInt(inputs[0]),
            OrigineX : parseInt(inputs[1]),
            OrigineY : parseInt(inputs[2]),
            NextX : parseInt(inputs[3]),
            NextY : parseInt(inputs[4])
        }

        zombies.push(temp);
    }

    // console.error("*******  ZOMBIES Obj *********");
    // for (let i = 0; i < zombies.length; i++){
    //     console.error("ID : " + zombies[i].Id);
    //     console.error("OrigineX : " + zombies[i].OrigineX + " OrigineY :" + zombies[i].OrigineY);
    //     console.error("NextX : " + zombies[i].NextX + " NextY :" + zombies[i].NextY);
    // }

    // Write an action using console.log()
    // To debug: console.error('Debug messages...');

    // Humain le plus proche :  distance : ``` d=sqrt((x2-x1)² + (y2-y1)²) ``` 
    let HumanIdProche = -1;
    let ZombieIdProche = -1;

    {
        
        let dist = Math.sqrt((17000)**2 + (10000) ** 2);

        console.error("dist = " + dist);

        for (let i = 0; i < humans.length; i++){
            console.error("ID : " + humans[i].Id);
            console.error("X : " + humans[i].x + " Y :" + humans[i].y);
            let distHuman = Math.sqrt((x - humans[i].x) ** 2 + (y - humans[i].y) ** 2);
            if (distHuman < dist){
                // // ZombieIdProche = -1;
                // // {
        
                // //     let dist2 = Math.sqrt((17000)**2 + (10000) ** 2);
            
                // //     console.error("dist = " + dist);
            
                // //     for (let j = 0; j < zombies.length; j++){
                // //         // console.error("ID : " + humans[i].Id);
                // //         // console.error("X : " + humans[i].x + " Y :" + humans[i].y);
                // //         let distZombie = Math.sqrt((zombies[j].NextX - humans[i].x) ** 2 + (zombies[j].NextY - humans[i].y) ** 2);
                // //         // ZombieIdProche = distZombie < dist ? i : ZombieIdProche;
                // //         // dist = distZombie < dist ? distZombie : dist; 
                // //         if (distZombie < dist2){
                // //             ZombieIdProche = j;
                // //             dist2 = distZombie;
                // //         }
                // //     }
                // // }
                // // let distHumanZombie = Math.sqrt((humans[i].x - zombies[ZombieIdProche].NextX) ** 2 + (humans[i].y - zombies[ZombieIdProche].NextY) ** 2);
                // // let distHunterZombie = Math.sqrt((x - zombies[ZombieIdProche].NextX) ** 2 + (y - zombies[ZombieIdProche].NextY) ** 2);
                // // if (distHumanZombie > distHunterZombie){
                // //     dist = distHuman;
                // //     HumanIdProche = i;
                // // }


                // let testDist = 1;
                // for (let j = 0; j < zombies.length; j++){
                //     let distZombieHuman = Math.sqrt((zombies[j].NextX - humans[i].x) ** 2 + (zombies[j].NextY - humans[i].y) ** 2);
                //     let distZombieHunter = Math.sqrt((zombies[j].NextX - x) ** 2 + (zombies[j].NextY - y) ** 2);
                //     if (distZombieHuman < distZombieHunter - 2000 && i < humans.length - 1){
                //         //testDist = 0;
                //         break;
                //     }
                // }
                // if (testDist){
                //     dist = distHuman;
                //     HumanIdProche = i;
                // }
                // // else {
                // //     i++;
                // // }

                dist = distHuman;
                HumanIdProche = i;


            }
        }
        console.error("Humain le plus proche : ID-" + HumanIdProche);
    }

    // Zombie le plus proche de HumanProche:  distance : ``` d=sqrt((x2-x1)² + (y2-y1)²) ```     
    ZombieIdProche = -1;
    {
        
        let dist = Math.sqrt((17000)**2 + (10000) ** 2);

        console.error("dist = " + dist);

        for (let j = 0; j < zombies.length; j++){
            // console.error("ID : " + humans[i].Id);
            // console.error("X : " + humans[i].x + " Y :" + humans[i].y);
            let distZombie = Math.sqrt((zombies[j].NextX - humans[HumanIdProche].x) ** 2 + (zombies[j].NextY - humans[HumanIdProche].y) ** 2);
            // ZombieIdProche = distZombie < dist ? i : ZombieIdProche;
            // dist = distZombie < dist ? distZombie : dist; 
            if (distZombie < dist){
                ZombieIdProche = j;
                dist = distZombie;
            }
        }
    }




    {
        destHumanX = zombies[ZombieIdProche].NextX;
        destHumanY = zombies[ZombieIdProche].NextY;

    }




    console.log(destHumanX + " " + destHumanY);
    // console.log('0 0');     // Your destination coordinates

}
