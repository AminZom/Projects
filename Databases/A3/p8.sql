create or replace function program8(trans_num char, vend_vno char, cust_acc char, trans_amount float) returns void as $$
	declare
		c1 cursor for select vno, vname, city, vbalance from vendor;
		c2 cursor for select account, cname, province, cbalance, crlimit from customer;
		
		curr_date DATE;
		
		updated_vno char(5);
		updated_vname char(20);
		updated_city char(20);
		updated_vbalance float(2);
		
		updated_acc char(5);
		updated_cname char(20);
		updated_province char(20);
		updated_cbalance float(2);
		updated_crlimit integer;
	begin
		curr_date = current_date;
		insert into transaction values(trans_num, vend_vno, cust_acc, curr_date, trans_amount);
		update customer set cbalance = cbalance + trans_amount where account = cust_acc;
		update vendor set vbalance = vbalance + trans_amount where vno = vend_vno;
		raise notice 'New Transaction:';
		raise notice '	Tno: %', trans_num;
		raise notice '	Vno: %', vend_vno;
		raise notice '	Account: %', cust_acc;
		raise notice '	Date: %', curr_date;
		raise notice '	Amount: %', trans_amount;
		open c1;
		loop
			fetch c1 into updated_vno, updated_vname, updated_city, updated_vbalance;
			exit when not found;
			if(updated_vno = vend_vno) then
				raise notice 'Updated Vendor:';
				raise notice '	Vno: %', updated_vno;
				raise notice '	Vname: %', updated_vname;
				raise notice '	City: %', updated_city;
				raise notice '	Vbalance: %', updated_vbalance;
			end if;
		end loop;
		close c1;
		open c2;
		loop
			fetch c2 into updated_acc, updated_cname, updated_province, updated_cbalance, updated_crlimit;
			exit when not found;
			if(updated_acc = cust_acc) then
				raise notice 'Updated Customer:';
				raise notice '	Account: %', updated_acc;
				raise notice '	Cname: %', updated_cname;
				raise notice '	Province: %', updated_province;
				raise notice '	Cbalance: %', updated_cbalance;
				raise notice '	Crlimit: %', updated_crlimit;
			end if;
		end loop;
		close c2;
	end;
$$ language plpgsql;
