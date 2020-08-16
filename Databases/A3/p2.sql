create or replace function program2(vend_name char) returns table(acc char(5), cust_name char(20), prov char(20)) as $$
	begin
		return query select customer.Account, Cname, Province
		from customer, transaction, vendor
		where Vname = vend_name and customer.Account = transaction.Account and transaction.Vno = vendor.Vno;
	end;
$$ language plpgsql;
