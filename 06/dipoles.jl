# Finding the equilibrium configuration of two magnetic dipoles.

using Optim
using Plots

# Let x1 and x2 be the orientation of dipoles 1 and 2.
# The potential energy reduces to this form
# (up to a constant scaling factor):
f(x1, x2) = sin(x1) * sin(x2) - 2 * cos(x1) * cos(x2)
f(x) = f(x[1], x[2])

# The orientation can take any value between 0 and 2 pi.
phis = 0:0.005:2

# Plot the potential.
fvals = [f(x,y) for x = phis*pi, y = phis*pi]
contour(phis, phis, fvals, fill = true)
title!("Potential of two magnetic dipoles")

# Find the minimum of the potential
x0 = [0.0, 0.0]  # Starting point
r = optimize(f, x0, NelderMead())
x = Optim.minimizer(r)

# Now consider the dipoles are in an external magnetic field.
a = 10.0
g(x1, x2) = f(x1, x2) - a * (sin(x1) + sin(x2))
g(x) = g(x[1], x[2])

# Find the minimum
x0 = [0.0, 0.0]  # Starting point
r = optimize(g, x0)
xg = x = Optim.minimizer(r)

# Plot the result
with(size=(600,600),
    aspect_ratio=:equal,
    top_margin=(12, :mm),
    annotationfontsize=9,
    annotationhalign=:left) do
    contour(phis, phis, [g(x,y) for x=phis*pi, y=phis*pi], fill = true,
        c = :viridis)
    scatter!([xg[1]]/pi, [xg[2]]/pi, label = "minimum")
    title!("Potential of two magnetic dipoles in external field")
    xlabel!("\\phi_1 [rad]")
    ylabel!("\\phi_2 [rad]")
    annotate!(0.0, 2.3,  "\\alpha = $(a)", )
    annotate!(1.0, 2.3,  "\\phi_1 = $(xg[1])")
    annotate!(1.0, 2.15, "\\phi_2 = $(xg[2])")
end
