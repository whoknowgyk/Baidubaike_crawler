create table ENTINFO(
	id int not null,
	namech nvarchar(50) not null,
	nameen nvarchar(50) not null,
	area nvarchar(100) not null,
	code nvarchar(9) not null,
	nature nvarchar(50) not null,
	industrial nvarchar(50) not null,
	bus nvarchar(100) not null,
	contactch nvarchar(50) not null,
	contacten nvarchar(50) not null,
	contact_addr nvarchar(100) not null,
	zipcode varchar(6) not null,
	tel nvarchar(20) not null,
	fax nvarchar(50) not null,
	email nvarchar(50),
	primary key(id)
);