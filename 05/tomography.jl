using DelimitedFiles

using FFTW
using ImageView

ϕ = readdlm("CAT/projections_phi.txt")
proj = readdlm("CAT/projections_pxp.txt")

#ω = fftfreq(size(proj,1), size(proj,1)/2)
ω = fftfreq(size(proj,1))
filter = abs.(ω)
filtered = similar(proj)
for (c, p) in enumerate(eachcol(proj))
    pt = fft(p)
    pt = pt .* filter
    filtered[:,c] = real(ifft(pt))
end

N = 400
x = range(-1, 1, length=N)
y = range(-1, 1, length=N)

img = zeros(N, N)
for (k, xk) in enumerate(x), (l, yl) in enumerate(y), (m, ϕm) in enumerate(ϕ)
    ξ = xk * cos(ϕm) + yl * sin(ϕm)
    if -1 <= ξ <= 1
        idx = round(Int, size(filtered, 1)*(ξ+1)/2)
        if 1 < idx
        img[l,k] += filtered[idx,m]
        end
    end
end

imshow(img, flipy=true)
