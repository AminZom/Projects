with ada.Text_IO; use ada.Text_IO;
with ada.Integer_Text_IO; use ada.Integer_Text_IO;

procedure sieve is
	type preArray is array(Integer range <>) of Integer;    --creating a dynamic array for the prime numbers
	N : Integer;              --the upper limit
	outputFile : file_type;   --the output file
	i, j : Integer := 0;      --variables used as counters
begin
	create(outputFile, out_file, "adaOutput.txt");
	put_line("Enter upper limit: ");
	get(N);
	declare
		numArray : preArray(0 .. N);   --allocating the memory required for the array based on the upper limit
	begin
		for i in 0 .. N loop
			numArray(i) := i;    --initializing the array
		end loop;
		i := 2;
		while(i * i <= N) loop   --iterating from 2 to the square root of the upper limit
			if numArray(i) /= 0 then
				j := i * 2;
				while(j <= N) loop
					numArray(j) := 0;   --loop iterates and sets the non-primes to 0
					j := j + i;
				end loop;
			end if;
			i := i + 1;
		end loop;
		for i in 2 .. N loop
			if numArray(i) /= 0 then
				put_line(outputFile, Integer'Image(numArray(i)));    --loop prints the primes to the file
			end if;
		end loop;
	end;
	close(outputFile);
end sieve;
