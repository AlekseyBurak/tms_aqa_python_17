import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="qwerty@123"
)

cursor = db.cursor(dictionary=True)
cursor.execute("""
SELECT
    c.LastName,
	c.FirstName,
	i.InvoiceId,
	i.CustomerId,
	i.InvoiceId,
	i.total
FROM
	Invoice as i
OUTER LEFT JOIN
	Customer as c
on
	i.CustomerId=c.CustomerId
"""
)



print(cursor.fetchall())
print(cursor.fetchone())
print(cursor.fetchmany())



db.commit()