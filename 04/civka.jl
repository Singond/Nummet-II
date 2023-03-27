using DelimitedFiles
using FFTW

data = readdlm("data/civka/civka.dat")
t, y = eachcol(data)

# Convolve with g = exp(-1E4 t^2) (normalized to sum 1)
g = exp.(-1E4 .* t.^2)
yf = fft(y)
gf = fft(y)
#yf = abs.(fft(y))
#gf = abs.(fft(y))
yc = ifft(yf .* gf)