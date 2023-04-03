using DelimitedFiles

using FFTW
using ImageView

function backproject(proj::Matrix{Float64}, N::Integer)
    x = range(-1, 1, length=N)
    y = range(-1, 1, length=N)
    ns = size(proj,1)
    img = zeros(N, N)

    for (m, ϕm) in enumerate(ϕ)
        ξ = x' * cos(ϕm) .+ y * sin(ϕm)
        idx = round.(Int, ns*(ξ.+1)./2)
        idxvalid = 1 .<= idx .<= ns
        idx[.!idxvalid] .= 1
        img[idxvalid] += proj[idx,m][idxvalid]
    end
    img
end

function filter_projection(proj::Matrix{Float64}, filter::Vector{Float64})
    filtered = similar(proj)
    for (c, p) in enumerate(eachcol(proj))
        pt = fft(p)
        pt = pt .* filter
        filtered[:,c] = real(ifft(pt))
    end
    filtered
end

ϕ = readdlm("CAT/projections_phi.txt")
proj = readdlm("CAT/projections_pxp.txt")

#ω = fftfreq(size(proj,1), size(proj,1)/2)
ω = fftfreq(size(proj,1))
filter = abs.(ω)
img = backproject(filter_projection(proj, filter), 400)

imshow(img, flipy=true)
