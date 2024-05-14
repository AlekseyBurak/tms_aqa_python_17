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
	i.InvoiceDate,
	i.total
FROM
	Customer as c
OUTER LEFT JOIN
	Invoice as i
ON
	c.CustomerId = i.CustomerId
"""
)
print(cursor.fetchall()) # when many
print(cursor.fetchone())
print(cursor.fetchmany())# when one



db.commit() # when you mace changes in DB you have to call it at the end

db.close()