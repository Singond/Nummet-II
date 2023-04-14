using DelimitedFiles
using SparseArrays

(nodex, nodey) = eachcol(readdlm("data/xnodes.txt"))
links = readdlm("data/xlinks.txt", Int)

A = spzeros(length(nodex), length(nodex))
for (a, b) in eachrow(links)
    A[a,b] = 1;
    A[b,a] = 1;
end