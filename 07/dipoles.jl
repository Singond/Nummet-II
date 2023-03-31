using Optim
using Plots

f(x1, x2) = sin(x1) * sin(x2) - 2 * cos(x1) * cos(x2)
f(x) = f(x[1], x[2])

phis = 0:0.005:2
#xx = repeat(phis'*pi, length(phis), 1)
#yy = repeat(phis*pi, 1, length(phis))

fvals = [f(x,y) for x = phis*pi, y = phis*pi]
contour(phis, phis, fvals, fill = true)

x0 = [0.0, 0.0]
r = optimize(f, x0, NelderMead())
x = Optim.minimizer(r)

a = 2
g(x1, x2) = f(x1, x2) - a * (sin(x1) + sin(x2))
g(x) = g(x[1], x[2])
contour(phis, phis, [g(x,y) for x=phis*pi, y=phis*pi], fill = true, c = :viridis)

x0 = [0.0, 0.0]
r = optimize(g, x0)
xg = x = Optim.minimizer(r)
scatter!([xg[1]]/pi, [xg[2]]/pi)