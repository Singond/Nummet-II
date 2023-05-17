using FFTW
using Images
using ImageView

img = Gray.(load("stm-graphene.png"))
c = fft(gray.(img))

imshow(abs.(c), CLim(0,1000))
