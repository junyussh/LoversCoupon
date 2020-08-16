BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "coupon" (
	"Id"	INTEGER,
	"UserId"	TEXT,
	"CouponName"	TEXT,
	"CouponContent"	TEXT,
	"ExpireDate"	TEXT,
	"FromUser"	TEXT,
	"CouponStatus"	INTEGER,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
COMMIT;
