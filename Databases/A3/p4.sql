create or replace function program4() returns table(return_acc char(5), return_name char(20), return_amount float(2), return_vname char(20)) as $$
	declare
		c1 cursor for select Account, Cname from customer;
		c2 cursor for select Account, T_Date, Amount, Vname from transaction natural join vendor;
		cust_acc char(5);
		cust_name char(20);
		
		trans_acc char(5);
		trans_date date;
		trans_amount float(2);
		vendor_name char(20);
		
		recent_date date;
		recent_amount float(2);
		recent_vendor char(20);
		checkTrans integer;
	begin
		recent_date = '0001-01-01';
		checkTrans = 0;
		open c1;
		loop
			fetch c1 into cust_acc, cust_name;
			exit when not found;
			open c2;
			loop
				fetch c2 into trans_acc, trans_date, trans_amount, vendor_name;
				exit when not found;
				if(trans_acc = cust_acc and trans_date > recent_date) then
					checkTrans = 1;
					recent_date = trans_date;
					recent_amount = trans_amount;
					recent_vendor = vendor_name;
				end if;
			end loop;
			close c2;
			if(checkTrans = 0) then
				raise notice 'Account Number % (%) has no transactions', cust_acc, cust_name;
			else
				raise notice 'Account Number: %, Customer Name: %, Amount: %, Vendor Name: %', cust_acc, cust_name, recent_amount, recent_vendor;
				recent_date = '0001-01-01';
				recent_amount = 0;
				recent_vendor = 0;
				checkTrans = 0;
			end if;
		end loop;
		close c1;
	end;
$$ language plpgsql;
