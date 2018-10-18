I used Graph-based visualization. Vertices (yellow points) represent locations and directed edges represent the relationship from 1945 to 2010. We are displaying relationship between a country supporting NAG and Target of the NAG. (This is the first draft of visualization, I think, it requires multiple improvements before finalizing).

NAG can be terrorist or revolutionist who is causing violence! 

For an instance, Pakistan is supporting Al-Kaeda (support) and Al-Kaeda is targeting India (target). So, their is a support->target relationship i.e. Pakistan->India.


Attached Images:
Evolution of NAGID: Illustrates various NAGIDs namely Ethno-National, Religious, Leftist etc and how they changed over the years across the world.

Evolution_of_States_in_Disguise: Illustrates support-target relationship with different color of each target continent. For an instance, European target counties are colored with Cyan. 

Target_Asia: Filters above ' Evolution of NAGID ' image to only Asian Targets.

<img src='Comp_5.gif'/>


Target_Europe: Filters above '  Evolution_of_States_in_Disguise  ' image to only European Targets.

Procedure 
1.    Year, Target, Support, NAGID attributes are extracted from the data. 
2     Target and Support countries are Geocoded to Latitudes and Longitudes. 
3.    Blue marble basemap is used to depict global political map.
4.    The graph is created with networkx DiGraph. Nodes are depicted by yellow points and edges are depicted by various colors for distinction.
5.    For the evolution of states_in_disguise.gif, continent colors are coded by using TarNum_COW.
6.    For Evotion_of_NAGIDs.gif, colors are according to NSAIDs. If a relationship is associated with multiple IDs then it is depicted that way only. 
