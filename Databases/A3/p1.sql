create or replace function program1(cust_name char) returns table(vno char(20), t_date date, amount float(2)) as $$
	begin
		return query select Vname, transaction.T_Date, transaction.Amount
		from customer, transaction, vendor
		where Cname = cust_name and customer.Account = transaction.Account and transaction.Vno = vendor.Vno;
	end;
$$ language plpgsql;
