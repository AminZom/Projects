identification division.
program-id. conv.
environment division.
input-output section.
file-control.
    select standard-output assign to display.

data division.
file section.
fd standard-output.
    01 stdout-record  pic x(80).

working-storage section.
77  i    		pic s99 usage is computational.
77  prev 		pic s9(8) usage is computational.
77  d    		pic s9(4) usage is computational.
77  checkValid  pic s9(4) usage is computational.

01 error-mess.
    02 filler pic x(22) value 'Illegal Roman Numeral!'.
01 quit-mess.
    02 filler pic x(22) value 'Quitting program...'.

linkage section.
77  m    pic s99 usage is computational.
77  err  pic s9 usage is computational-3.
77  sum1 pic s9(8) usage is computational.
01  array-area.
    02 s pic x(1) occurs 30 times.

procedure division using array-area, m, err, sum1.
    move zero to sum1. move 1001 to prev.
    perform loop thru end-loop varying i from 1 by 1
       until i is greater than m.
    move 1 to err. goback.
loop.
	move 0 to checkValid.
    if s(i) is equal to 'I'
		move 1 to d
		move 1 to checkValid
	end-if.
	if s(i) is equal to 'i'
		move 1 to d
		move 1 to checkValid
	end-if.
	if s(i) is equal to 'V'
		move 5 to d
		move 1 to checkValid
	end-if.
	if s(i) is equal to 'v'
		move 5 to d
		move 1 to checkValid
	end-if.
	if s(i) is equal to 'X'
		move 10 to d
		move 1 to checkValid
	end-if.
	if s(i) is equal to 'x'
		move 10 to d
		move 1 to checkValid
	end-if.
	if s(i) is equal to 'L'
		move 50 to d
		move 1 to checkValid
	end-if.
	if s(i) is equal to 'l'
		move 50 to d
		move 1 to checkValid
	end-if.
	if s(i) is equal to 'C'
		move 100 to d
		move 1 to checkValid
	end-if.
	if s(i) is equal to 'c'
		move 100 to d
		move 1 to checkValid
	end-if.
	if s(i) is equal to 'D'
		move 500 to d
		move 1 to checkValid
	end-if.
	if s(i) is equal to 'd'
		move 500 to d
		move 1 to checkValid
	end-if.
	if s(i) is equal to 'M'
		move 1000 to d
		move 1 to checkValid
	end-if.
	if s(i) is equal to 'm'
		move 1000 to d
		move 1 to checkValid
	end-if.
	if s(i) is equal to 'Q'
		open output standard-output
		write stdout-record from quit-mess after advancing 1 line
		move 3 to err
		close standard-output
		goback
	end-if.
	if checkValid is equal to 0
		open output standard-output
		write stdout-record from error-mess after advancing 1 line
		move 2 to err
		close standard-output
		goback
	end-if.
	add d to sum1.
    if d is greater than prev
		compute sum1 = sum1 - 2 * prev
    end-if.
end-loop.
move d to prev.
