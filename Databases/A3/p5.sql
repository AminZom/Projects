create or replace function program5() returns table(return_vno char(5), return_vname char(20), return_vbalance float(2)) as $$
	declare
		c1 cursor for select vno, amount from transaction;
		
		trans_vno char(5);
		trans_amount float(2);
	begin
		open c1;
		loop
			fetch c1 into trans_vno, trans_amount;
			exit when not found;
			update vendor set vbalance = vbalance + trans_amount where vno = trans_vno;
		end loop;
		close c1;
		return query select vno, vname, vbalance from vendor;
	end;
$$ language plpgsql;
