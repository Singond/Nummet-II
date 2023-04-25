using Plots

function randomwalk2(steps; d = 1, x0 = 0, y0 = 0)
    x = zeros(steps)
    y = zeros(steps)
    x[1] = x0
    y[1] = y0
    for k in 2:steps
        a = 2pi * rand()
        x[k] = x[k-1] + d * cos(a)
        y[k] = y[k-1] + d * sin(a)
    end
    (x, y)
end

cummean(x) = cumsum(x) ./ (1:length(x))

function meandist(x, y)
    r = hypot.(x, y)
    cummean(r)
end

function nwalks(walkf; walks = 1, steps = 1)
    xx = zeros(steps, walks)
    yy = zeros(steps, walks)
    r = zeros(steps)
    for k = 1:walks
        x, y = walkf(steps)
        xx[:,k], yy[:,k] = x, y
        r += meandist(x, y)
    end
    (xx, yy, r)
end

xx, yy, r = nwalks(randomwalk2, walks=1000, steps=1000)

steps = 1000
walks = [1 10 100 1000]
rr = zeros(steps, length(walks))
for (k, wk) in enumerate(walks)
    _, _, rr[:,k] = nwalks(randomwalk2, walks=wk, steps=steps)
end

plot(rr ./ walks, label = map(w -> "Nwalks = $w", walks))
gui() #Display the plot

# For large number of simulations, do not store x and y
walks = 1e4
r = zeros(steps)
for k = 1:walks
    xk, yk = randomwalk2(steps)
    global r += meandist(xk, yk)
end
