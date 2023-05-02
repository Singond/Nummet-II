function sweep(beta,L,s)

  probs=[0.5,exp(-4*beta),exp(-8*beta)]

  dMtot=0
  dEtot=0

  for i in 1:L
    im=i-1; if i==1 im=L end
    ip=i+1; if i==L ip=1 end
    for j in 1:L
      jm=j-1; if j==1 jm=L end
      jp=j+1; if j==L jp=1 end
   
      dE=2*s[i,j]*(s[im,j]+s[ip,j]+s[i,jm]+s[i,jp])
   
      if dE>=0 && probs[1+div(dE,4)]<rand()
        continue
      end
  
      s[i,j]=-s[i,j]
      dMtot+=2*s[i,j]
      dEtot+=dE
  
    end
  end
 
  return dMtot,dEtot
end


function runMC(L,NT,T,Navg)

  s=ones(Int,L,L)
  M=L^2
  E=-2*L^2

  Msamp=zeros(NT,Navg)
  Esamp=zeros(NT,Navg)

  for i in 1:NT
    println(i)
    beta=1/T[i]
  
    for j in 1:Navg
      dM,dE=sweep(beta,L,s)
      M+=dM
      E+=dE
    end
  
    for j in 1:Navg
      dM,dE=sweep(beta,L,s)
      M+=dM
      E+=dE
      Msamp[i,j]=M/L^2
      Esamp[i,j]=E/L^2
    end
  
  end

  Mavg=sum(Msamp,dims=2)/Navg
  Eavg=sum(Esamp,dims=2)/Navg
  
  M2avg=sum(Msamp.^2,dims=2)/Navg
  E2avg=sum(Esamp.^2,dims=2)/Navg

  return Mavg,Eavg,M2avg,E2avg
end


L=32
NT=100
T=LinRange(0.04,4.0,NT)
Navg=50

t1=time()
Mavg,Eavg,M2avg,E2avg = runMC(L,NT,T,Navg)
t2=time()
println(t2-t1,"s")

suscept=(M2avg-Mavg.^2)./T
heatcap=(E2avg-Eavg.^2)./T.^2


using Plots
gr()

p1=plot(T,Mavg,label="M")
p2=plot(T,Eavg,label="E")
p3=plot(T,suscept,label="χ")
p4=plot(T,heatcap,label="C")

display(plot(p1,p2,p3,p4,layout=(2,2)))
