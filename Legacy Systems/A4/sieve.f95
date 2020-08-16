! Compile with "gfortran -Wall sieve.f95"
! Execute with "./a.out"

PROGRAM SIEVE
    integer, dimension (:,:), allocatable :: numArray   !creating a dynamic array for the prime numbers
    integer :: N        !the upper limit
    integer :: i, j     !variables used as counters
    
    write(*,*) "Enter upper limit: "
    read(*,'(i10)', iostat = istat) N
    allocate(numArray(1,N))
    open (unit = 1, file = "fortranOutput.txt")
    
    do i = 1, N
        numArray(1,i) = i     !initializing the array
    end do
    
    i = 2
    do while(i * i <= N)      !iterating from 2 to the square root of the upper limit
        if(numArray(1, i) /= 0) then
            j = i * 2
            do while(j <= N)
                numArray(1, j) = 0      !loop iterates and sets the non-primes to 0
                j = j + i
            end do
        end if
        i = i + 1
    end do
    
    do i = 2, N
        if(numArray(1, i) /= 0) then
            write(1,*) numArray(1, i)    !loop prints the primes to the file
        end if
    end do
    deallocate(numArray)
END
