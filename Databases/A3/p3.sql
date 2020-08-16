create or replace function program3(cust_acc char, cust_name char, prov char, lim integer) returns table(return_acc char(5), return_name char(20), return_prov char(20), return_bal float(2), return_lim integer) as $$
	begin
		insert into customer values (cust_acc, cust_name, prov, 0, lim);
		return query select * from customer;
	end;
$$ language plpgsql;
