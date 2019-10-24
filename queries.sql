-- 3. Given the entity relationship diagram below, code SQL sentences for:

-- a. Get all buses for “Concessionaire 1”.
Select b.* from bus as b left join concessionaire as c on b.concessionaireid = c.id where c.id = 1

-- b. Get all NVR devices for buses with type equal to “Bi-articulado”.
Select d.* from device as d left join devicetype as dt on d.devicetypeid = dt.id left join bus as b on d.busid = b.id where dt.id = 2 and b.type like "Bi-articulado"

-- c. Summarize the quantity of devices by status (Active / Inactive) and bus motor (Diesel / Gas / Electric / Hybrid).

Select	
	count(CASE WHEN status like 'Active' THEN status END) as status_active, 
	count(CASE WHEN status like 'Inactive' THEN status END) as status_inactive, 
	count(CASE WHEN motor like 'Diesel' THEN city END) as motor_diesel,
	count(CASE WHEN motor like 'Gas' THEN city END) as motor_gas,
	count(CASE WHEN motor like 'Electric' THEN city END) as motor_electric,
	count(CASE WHEN motor like 'Hybrid' THEN city END) as motor_hybrid
From device as d left join bus as b on d.busid = b.id
