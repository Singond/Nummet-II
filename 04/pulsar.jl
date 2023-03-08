using FFTW
using Plots
using WAV

y, freq, _, _ = wavread("data/filter_pulsar/sample4.wav")

s = fft(y)
n = size(y, 1)
f = [0:1:(n/2 - 1); (-n/2):1:-1]

# Filter to keep only harmonics...

# ... by cutting off low-intensity frequencies
st = s
st[abs.(s) .< 500] .= 0
yt = ifft(st)

plot(f, abs.(st))
wavplay(abs.(yt[1:10000]), freq)
