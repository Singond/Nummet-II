using DelimitedFiles

using LsqFit
using Plots

x, y, ey = eachcol(readdlm("data/xdata5"))

@. lorentz(x, p) = p[1] / (p[2] + (x - p[3])^2)
fit = curve_fit(lorentz, x, y, [1.0, 1.0, 1.0])
fitw = curve_fit(lorentz, x, y, ey, [1.0, 1.0, 1.0])

f(x) = lorentz(x, coef(fit))
g(x) = lorentz(x, coef(fitw))

scatter(x, y, yerr=ey, label="data")
plot!(f, color = 1, label="simple fit")
plot!(g, color = 2, label="weighted fit")

# 2 1 1/2
# non-weighted
# weighted 1.897 0.952 0.498
# errors 0.125 0.037 0.023
