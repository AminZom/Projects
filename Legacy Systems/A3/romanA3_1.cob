identification division.
program-id. romannumerals.
environment division.
input-output section.
file-control.
    select standard-input assign to keyboard.
    select standard-output assign to display.
    select myFile assign to dynamic fileName
		organization is line sequential.

data division.
file section.
fd myFile.
01 input-record.
	05 num pic x(30).
fd standard-input.
    01 stdin-record   pic x(80).
fd standard-output.
    01 stdout-record  pic x(80).
working-storage section.
77  fileName	pic		x(30).
77  countSpaces pic s99 usage is computational.
77  inputLength pic s99 usage is computational.
77  n    		pic s99 usage is computational.
77  temp 		pic s9(8) usage is computational.
77  ret  		pic s9 usage is computational-3.
77  eof-switch	pic	 9  value  1.
01  out-record.
	05 out1   pic X(8) value "number =".
	05 filler pic X.
	05 out2   pic 99.
01  input-area.
    02 in-r   pic x(30).
    02 filler pic x(79).
01  title-line.
    02 filler pic x(11) value spaces.
    02 filler pic x(24) value 'Roman Number Equivalents'.
01  underline-1.
    02 filler pic x(45) value 
       ' --------------------------------------------'.
01  col-heads.
    02 filler pic x(3) value spaces.
    02 filler pic x(12) value 'Roman Number'.
    02 filler pic x(17) value spaces.
    02 filler pic x(11) value 'Dec. Equiv.'.
01  file-heads.
    02 filler pic x(18) value spaces.
    02 filler pic x(12) value 'File Input'.
01  keyboard-heads.
    02 filler pic x(16) value spaces.
    02 filler pic x(14) value 'Keyboard Input'.
01  underline-2.
    02 filler pic x(45) value
       ' --------------------------------------------'.
01  print-line.
    02 filler pic x value space.
    02 out-r  pic x(30).
    02 filler pic x(3) value spaces.
    02 out-eq pic z(9).

procedure division.
    open input standard-input, output standard-output.
    write stdout-record from title-line after advancing 0 lines.
    write stdout-record from underline-1 after advancing 1 line.
    display " ".
    display "Enter '1' for file input, or '2' to for keyboard input".
    read standard-input into input-area
    end-read.
    evaluate in-r
		when "1" perform fileInput
		when "2" perform keyboardInput
		when other display "Invalid choice! Try again.".
	stop run.
keyboardInput.
	write stdout-record from keyboard-heads after advancing 1 line.
	write stdout-record from underline-1 after advancing 1 line.
	display " ".
	display "Enter a roman number below: " 
	read standard-input into input-area at end close standard-input, standard-output
	end-read.
    move zero to countSpaces.
    inspect function reverse (in-r)
		tallying countSpaces for leading space.
	compute inputLength = length of in-r - countSpaces.
	move inputLength to n.
    call "conv" using input-area, n, ret, temp.
    if ret is not equal to 2
		move temp to out-eq
		move input-area to out-r
		write stdout-record from col-heads after advancing 1 line
		write stdout-record from underline-2 after advancing 1 line
		display " "
		write stdout-record from print-line after advancing 1 line
	end-if.
	display " ".
	close standard-input, standard-output.
end-keyboardInput.
fileInput.
	write stdout-record from file-heads after advancing 1 line.
	write stdout-record from underline-1 after advancing 1 line.
	display " ".
	display "Enter file name below: ".
	accept fileName.
	write stdout-record from col-heads after advancing 1 line.
    write stdout-record from underline-2 after advancing 1 line.
    display " ".
	open input myFile.
	perform getLine until eof-switch = 0.
	close myFile.
	stop run.
getLine.
	read myFile into input-area
		at end move 0 to eof-switch
	end-read.
	if eof-switch is not equal to zero then
		move zero to countSpaces
		inspect function reverse (in-r)
			tallying countSpaces for leading space
		compute inputLength = length of in-r - countSpaces
		move inputLength to n
		call "conv" using input-area, n, ret, temp
		if ret is not equal to 2 then
			move temp to out-eq
			move input-area to out-r
			write stdout-record from print-line after advancing 1 line
		end-if
		display " "
	end-if.
end-getLine.
end-fileInput.
