using LinearAlgebra

using Plots
using SpecialFunctions

"""
Estimate the volume of a unit hypersphere of dimension dim
using Monte Carlo integration.
"""
function hypersphere_mc(dim, N)
    S = 0
    for k = 1:N
        x = 2 * rand(dim) .- 1
        S += norm(x) < 1
    end
    2^dim * S / N
end

"""
Return the volume of a unit hypersphere of dimension dim.
"""
hypersphere_exact(dim) = 2pi^(dim / 2) / (dim * gamma(dim / 2))

Dmax = 16
N = 1e6

D = 1:Dmax
V = [hypersphere_mc(dim, N) for dim in D]

scatter(D, V, label = "Monte Carlo", xlabel = "dimension", ylabel = "volume")
dd = hypersphere_exact.(D)
plot!(hypersphere_exact, label = "exact")
