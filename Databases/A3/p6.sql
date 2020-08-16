create or replace function program6() returns void as $$
	declare
		c1 cursor for select vno, vbalance from vendor;
		
		vend_vno char(5);
		vend_vbalance float(2);
		serv_fee float(2);
	begin
	serv_fee = 0;
		open c1;
		loop
			fetch c1 into vend_vno, vend_vbalance;
			exit when not found;
			serv_fee = vend_vbalance * 0.04;
			update vendor set vbalance = vbalance - serv_fee where vno = vend_vno;
			raise notice 'Vendor Name: %, Fee Charged: %, New Balance: %', vend_vno, serv_fee, vend_vbalance - serv_fee;
			serv_fee = 0;
		end loop;
		close c1;
	end;
$$ language plpgsql;
