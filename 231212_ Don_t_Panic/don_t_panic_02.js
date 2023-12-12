/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   don_t_panic_02.js                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/12 09:53:30 by pwolff            #+#    #+#             */
/*   Updated: 2023/12/12 09:53:54 by pwolff           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

a=[]
b=["WAIT","BLOCK","RIGHT","LEFT"]
c=readline().split(' ')
d=parseInt(c[4])
e=parseInt(c[7])
for(i=0;i<e;i++){f={};c=readline().split(' ');f.f=parseInt(c[0]);f.p=parseInt(c[1]);a[i]=f}
while(1){x=0;c=readline().split(' ');g=parseInt(c[0]);h=parseInt(c[1]);l=c[2]
if(g>-1 && g<e){m=0;for(i=0;i<e;i++)if(a[i].f==g) m=i;if((a[m].p-h<0&&l==b[2])||(a[m].p-h>0&&l==b[3])) x=1}
else if(g>-1&&((d-h<0&&l==b[2])||(d-h>0&&l==b[3]))) x=1
console.log(b[x])}