# TEAM 4 [![LES SEMIS CROUSTILLANTS](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/diffusioncon/Team-4#readme)
 
 LES SEMIS CROUSTILLANTS


## Problematic
The problem we hope to solve is that 1 billion people in Africa are living without affordable and reliable energy. This is problematic not only due to the need of basic human needs and for hospitals to give their patients the best possible help. Women feel insecure walking home in the nights due to the lack of streetlights and therefore either say no to job opportunities that includes walking home late or choose to walk home in fear. It is therefore not only a question about energy accessibility but also equality.

Moreover, Africa is almost always exposed to sun and there are no seasons  and there is therefore a big opportunity for solar cells in this region. Even though solar cells requires a big initial investments, there are relatively cheap to maintain and are environmental friendly.  

## Solution
Based on these problems and opportunities, we will now present our solution. 

To start with, we need donations to be able to invest in and maintain our solar cell. Once the solar cells are up running, we have decided that the hospitals have priority to the electricity produced.

The remaining electricity will be distributed equally among all villagers in the city through a token system. The habitants now have a choice to either use all of the electricity given to them or to sell the remaining of the token to the businesses in the city. We created a simulation as close as possible to the reality and the revenues of the businesses depends on the number of employees and percentage of energy needs covered. Furthermore, when the businesses have excess money they hire employees and when they are in lack of money they fire them. This creates an equilibrium between businesses and villagers. Moreover, the bid-ask between the businesses and villagers regulates itselves through the ask of villagers and the bid of businesses. Thus, the bid-ask price is fixed in regard to supply and demand, as in the real stock market (see attached bid-ask). Thus, it regulates itself and create a balance. Since most villagers might not have economic knowledge, we made automated transactions at the end of every month so that inactive traders don't take up all the storage. 

Our intentions with this project is not only to provide affordable and reliable energy but also to help the habitants to help themselves by engaging and inspiring them to do business with the businesses in the city. Hence, we have created a stock market on which villagers exchange their tokens for money with the businesses. We believe that this project have the potential to change the mindset of the habitants in a positive direction (see attached model 1). 

Apart from our initial investment, the idea is to create a system that in the long run will be self driven without any need of further donations. To pay for the maintenance of the solar panel, our system takes a given commission for every token transaction. If these commissions isn’t enough to cover the maintenance costs, the money needed will come from donations. Thus, at the end of every month, in regard to the money received from commissions and in some cases also donations, we will do the reparations needed (reparations are only needed when the solar panel lost x percent of its capacity) . If there is enough money left, we will build a new solar panel with new storage (solar panel + storage = greed). 


## Biggest challenge for us to pursue with this project: 
The biggest challenge to us has been to integrate cadCAD and learn how to use it. We used the API in an Object Oriented style, instead of the procedural style suggested in the Juypter Notebook. We made a "Central" class which acted as the village townhall and was responsible for calling the methods of all other agents. We then made wrapper functions to update cadCAD's state.

## Opinion on cadCAD:  
cadCAD has been very useful to log the progression of the simulation. However, its procedural nature was a big drawback and we had to do a lot of "hacks" to use it with our preferred coding style. Besides, it seems like cadCAD is trying to use Python `thread` library which only makes it run slower rather than faster because `Python` doesn't have CPU bound `multithreading` (because of the GIL.) [Read about the GIL](https://www.geeksforgeeks.org/what-is-the-python-global-interpreter-lock-gil/)
