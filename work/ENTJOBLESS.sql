CREATE TABLE ENTJOBLESS(
    id int not null PRIMARY KEY,
    ent_id nvarchar(50) not null,
    time datetime not null,
    first_num int(10) not null,
    now_num int(10) not null,
    reduce_type nvarchar(50) null,
    reason1 nvarchar(100) null,
    reason1info nvarchar(100) null,
    reason2 nvarchar(100) null,
    reason2info nvarchar(100) null,
    reason3 nvarchar(100) null,
    reason3info nvarchar(100) null,
    reason0 nvarchar(100) null,
    status int(3) null
);
