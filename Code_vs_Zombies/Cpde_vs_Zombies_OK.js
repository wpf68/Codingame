/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Cpde_vs_Zombies_OK.js                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/06 09:29:04 by pwolff            #+#    #+#             */
/*   Updated: 2023/12/06 09:31:05 by pwolff           ###   ########.fr       */
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


    let HumanIdProche = 0;
    let ZombieIdProche = 0;


    let DistHumanZombiePlusProche = [];

    let distMax = Math.sqrt((17000)**2 + (10000) ** 2);


    for (let i = 0; i < humans.length; i++){

        distMax = Math.sqrt((17000)**2 + (10000) ** 2);
        for (let j = 0; j < zombies.length; j++){
            let distHumanZombies = Math.sqrt((zombies[j].NextX - humans[i].x) ** 2 + (zombies[j].NextY - humans[i].y) ** 2);
            if (distHumanZombies < distMax){
                distMax = distHumanZombies;
            }
        }
        DistHumanZombiePlusProche.push(distMax);
    }

    if (DistHumanZombiePlusProche.length > 1){
        for (let i = 0; i < DistHumanZombiePlusProche.length - 1; i++){
           // console.error("** Human [" + i + "] = "  + DistHumanZombiePlusProche[i] + " -- Human [" + (i + 1) + "] = "  + DistHumanZombiePlusProche[i + 1])
            if(+DistHumanZombiePlusProche[i] > +DistHumanZombiePlusProche[i + 1]){
                HumanIdProche = i;
            }
            else {
                HumanIdProche = i + 1;
            }
            
        }
    }

    //console.error("Humain le plus proche : ID-" + HumanIdProche);

    ZombieIdProche = -1;
    {
        
        let dist = Math.sqrt((17000)**2 + (10000) ** 2);

        console.error("dist = " + dist);

        for (let j = 0; j < zombies.length; j++){

            let distZombie = Math.sqrt((zombies[j].NextX - humans[HumanIdProche].x) ** 2 + (zombies[j].NextY - humans[HumanIdProche].y) ** 2);

            if (distZombie < dist){
                ZombieIdProche = j;
                dist = distZombie;
            }
        }
    }

    destHumanX = zombies[ZombieIdProche].NextX;
    destHumanY = zombies[ZombieIdProche].NextY;

    console.log(destHumanX + " " + destHumanY);

}
