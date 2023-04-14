import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse
import scipy.sparse.linalg

nodes=np.loadtxt("xnodes.txt")
links=np.loadtxt("xlinks.txt",dtype=int)-1 # indexing from 0

Nnode=nodes.shape[0]
Nlink=links.shape[0]

# construct the connectivity matrix in COO sparse format

vals=np.ones(2*Nlink)
rows=np.concatenate( (links[:,0],links[:,1]) )
cols=np.concatenate( (links[:,1],links[:,0]) )

A = scipy.sparse.coo_matrix( (vals,(rows,cols)), shape=(Nnode, Nnode))

# diagonalize the connectivity matrix to find the largest eigenvalue

eigval,eigvec = scipy.sparse.linalg.eigsh(A, k=1, which='LA')

# plot the network and show the dominant eigenvector by coloring the nodes

xlink=nodes[links[:,0],0]
ylink=nodes[links[:,0],1]
ulink=nodes[links[:,1],0]-xlink
vlink=nodes[links[:,1],1]-ylink

plt.quiver(xlink,ylink,ulink,vlink, angles='xy',scale_units='xy',scale=1, \
           headlength=0.001,headaxislength=0,linewidth=0.1,color="#aaaaaa")

vec=np.abs(eigvec[:,0])
plt.scatter(nodes[:,0],nodes[:,1],s=1+50*vec/np.max(vec),c=vec,cmap='jet')
         
plt.show()