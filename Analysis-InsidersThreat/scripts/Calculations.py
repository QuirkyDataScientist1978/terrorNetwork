
# coding: utf-8

# In[35]:


from collections import OrderedDict
import pickle

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import networkx as nx
from mpl_toolkits.basemap import Basemap


# In[32]:


def getGeoCoding(name):
	g = geocoder.google(name)
	return g.latlng

def getCountryGeo(locations,name):
	if name in ["''","'.'",0]:
		return locations
	else:
		
		if locations.get(name,''):
			if locations[name]==None:
				locations[name]=getGeoCoding(name)
		else:
			locations[name]=getGeoCoding(name)
		return locations

lower_left_lon=-180
lower_left_lat= -90
upper_right_lon=180
upper_right_lat= 90
def plotNetworkGraph(year,waveMatrix,locations,nodeNames, filename, nodeSize,targetWeights):
	resolution='l'
	#Bmap_Amplitude = Basemap(projection='merc',llcrnrlon=lower_left_lon,llcrnrlat=lower_left_lat,urcrnrlon=upper_right_lon,urcrnrlat=upper_right_lat,lat_ts=0,resolution=resolution,suppress_ticks=True)
	cmap=plt.get_cmap("jet")
	Bmap_Amplitude=Basemap(projection='merc',llcrnrlat=-61.4,urcrnrlat=71.56,\
			llcrnrlon=-163.7,urcrnrlon=165.65,lat_ts=20,resolution='f')
	G_Amplitude = nx.DiGraph()
	for name in nodeNames:
	
		latitude=locations[name][0]
		longitude=locations[name][1]
		x,y=Bmap_Amplitude(longitude,latitude)
		G_Amplitude.add_node(name,pos=(x,y))
	   
	for nm in waveMatrix[year]:
		if nm[0] not in ['','.','0']:
			if targetWeights[nm[1]]==0.38:
				G_Amplitude.add_edge(nm[0], nm[1], weight = targetWeights[nm[1]])

			   

	plt.close()
	#plt.axis('off')


	plt.title(year,fontsize = 8)
	edgewidth_Amplitude = [ d['weight'] for (u,v,d) in G_Amplitude.edges(data=True)]
	pos=nx.get_node_attributes(G_Amplitude,'pos')
	nx.draw_networkx_nodes(G_Amplitude,pos, node_color = 'y', node_size = nodeSize, alpha = 0.7)
	#nx.draw_networkx_edges(G_Amplitude, pos, edge_color = edgewidth_Amplitude, width=edgewidth_Amplitude, alpha = edgewidth_Amplitude)
	nx.draw_networkx_edges(G_Amplitude, pos, width=[0.5 for i in edgewidth_Amplitude] ,cmap=cmap,edge_color =  [cmap(i) for i in edgewidth_Amplitude], alpha = [cmap(0.95) for i in edgewidth_Amplitude])

	Bmap_Amplitude.drawcountries()
	Bmap_Amplitude.drawstates()
	Bmap_Amplitude.bluemarble()
	

	#plt.axis('off')
	print(year)
	plt.savefig("{}.png".format(year), dpi = 300,bbox_inches='tight')
	#plt.show()



# In[9]:


file="pipeFormat.csv"
f=open(file,"r")
print(f.readline())
data=OrderedDict()
for l in f:
	row=l.split("|")
	year=int(row[3])
	target=row[8]
	support=row[38]
	
	if year not in data:
		data[year]=[]
	data[year].append((support,target,))
   
  
	
waveMatrix=data  
nodeSize=1
locations=pickle.load(open("locations.pickle","rb"))
nodeNames=pickle.load(open("nodenames.pickle","rb"))  
targetWeights=pickle.load(open("targetWeights.pickle","rb"))  
filename="plot5"
for year in list(data.keys()):
	plotNetworkGraph(year,waveMatrix,locations,nodeNames, filename, nodeSize,targetWeights)
   


