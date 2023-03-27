using FFTW
using Plots
using WAV

y1, freq1, _, _ = wavread("balik1/sample5a.wav")
y2, freq2, _, _ = wavread("balik1/sample5b.wav")

s1 = fft(y1)
s2 = fft(y2)

plot(abs.(s1), xlim=(200, 1000))
plot!(abs.(s2), xlim=(200, 1000))