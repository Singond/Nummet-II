program Ising_2D
implicit none

integer, parameter :: L=32, NT=100, Navg=50
integer s(L,L), M, E, i,j
real beta, Tmin,Tmax, T(NT), Msamp(NT,Navg), Esamp(NT,Navg), &
     Mavg(NT), Eavg(NT), M2avg(NT), E2avg(NT), t1,t2

  s=1
  M=L**2
  E=-2*L**2
 
  Tmin=0.04
  Tmax=4.0
 
  call CPU_time(t1)
 
  do i=1,NT
    write(*,*) i
    T(i)=Tmin+(i-1)*(Tmax-Tmin)/(NT-1)
    beta=1/T(i)
  
    do j=1,Navg
      call sweep()
    end do
  
    do j=1,Navg
      call sweep()
      Msamp(i,j)=real(M)/L**2
      Esamp(i,j)=real(E)/L**2
    end do
 
  end do
 
  call CPU_time(t2)
  write(*,*) t2-t1,"s"

  Mavg=sum(Msamp,dim=2)/Navg
  Eavg=sum(Esamp,dim=2)/Navg

  M2avg=sum(Msamp**2,dim=2)/Navg
  E2avg=sum(Esamp**2,dim=2)/Navg

  open(1,file="xising2D")
  do i=1,NT
    write(1,*) T(i), Mavg(i), Eavg(i), &
     (M2avg(i)-Mavg(i)**2)/T(i), (E2avg(i)-Eavg(i)**2)/T(i)**2
  end do
  close(1)

contains

  subroutine sweep
    real probs(0:2),r
    integer i,j,im,ip,jm,jp,dE

     probs=[0.5,exp(-4*beta),exp(-8*beta)]

     do i=1,L
       im=i-1; if (i==1) im=L
       ip=i+1; if (i==L) ip=1
       do j=1,L
         jm=j-1; if (j==1) jm=L
         jp=j+1; if (j==L) jp=1

         dE=2*s(i,j)*(s(im,j)+s(ip,j)+s(i,jm)+s(i,jp))

         if (dE>=0) then
           call random_number(r)
           if (probs(dE/4)<r) cycle
         end if

         s(i,j)=-s(i,j)
         M=M+2*s(i,j)
         E=E+dE
       end do
     end do

  end subroutine

end program
