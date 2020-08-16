create or replace function program7() returns void as $$
	declare
		c1 cursor for select account, cname, cbalance, crlimit from customer;
		
		cust_acc char(5);
		cust_name char(20);
		cust_cbalance float(2);
		cust_limit integer;
		
		diff float(2);
	begin
		open c1;
		loop
			fetch c1 into cust_acc, cust_name, cust_cbalance, cust_limit;
			exit when not found;
			if(cust_cbalance > cust_limit) then
				diff = cust_cbalance - cust_limit;
				diff = diff * 0.1;
				update customer set cbalance = cbalance + diff where account = cust_acc;
				raise notice 'Customer Name: %, New Balance: %', cust_name, cust_cbalance + diff;
			end if;
			diff = 0;
		end loop;
		close c1;
	end;
$$ language plpgsql;
