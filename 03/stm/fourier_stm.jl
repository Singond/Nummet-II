using FFTW
using Images
using ImageView

img = Gray.(load("stm-graphene.png"))
c = fft(gray.(img))
fx = fftfreq(size(c, 2))
fy = fftfreq(size(c, 1))
cc = c[sortperm(fy), sortperm(fx)]

imshow(abs.(cc), CLim(0,1000))
