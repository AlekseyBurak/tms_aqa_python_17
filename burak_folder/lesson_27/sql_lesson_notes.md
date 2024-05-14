https://sqlitebrowser.org/dl/

```
SELECT
	firstname,
	lastname,
	email
FROM
	Customer
```

```
SELECT
	firstname as [smth smth],
	lastname as 'smth smth',
	email as justsmth,
FROM
	Customer
```

```
SELECT
	firstname as [smth smth],
	lastname as 'smth smth',
	email as justsmth,
FROM
	Customer
ORDER BY
	lastname asc/desc
	firstname asc/desc
```

```
SELECT
	firstname as [smth smth]
	lastname as 'smth smth'
	email as justsmth
FROM
	Customer
ORDER BY
	lastname asc/desc
	firstname asc/desc
LIMIT 10
```

```
SELECT
	invoicedate
	billingaddress
	billingcity
	total
FROM
	invoice
WHERE
	total = 1.98
ORDER BY
	invoicedate
```

```
SELECT
	invoicedate
	billingaddress
	billingcity
	total
FROM
	invoice
WHERE
	total BETWEEN 1.98 AND 5.00
ORDER BY
	invoicedate
```

```
SELECT
	invoicedate
	billingaddress
	billingcity
	total
FROM
	invoice
WHERE
	total IN (1.98, 3,96)
ORDER BY
	invoicedate
```


```
SELECT
	invoicedate
	billingaddress
	billingcity
	total
FROM
	invoice
WHERE
	billingcity = 'brussels'
ORDER BY
	invoicedate
```

```
SELECT
	invoicedate
	billingaddress
	billingcity
	total
FROM
	invoice
WHERE
	billingcity IN ('brussels', 'orlando')
ORDER BY
	invoicedate
```

```
SELECT
	invoicedate
	billingaddress
	billingcity
	total
FROM
	invoice
WHERE
	billingcity LIKE 'B%' / '%B%'
ORDER BY
	invoicedate
```

```
SELECT
	invoicedate
	billingaddress
	billingcity
	total
FROM
	invoice
WHERE
	invoicedata = '2010-05-22 00:00:00'
	DATE(invoicedata) = '2010-05-22'
	DATE(invoicedata) > '2010-05-22' AND total < 3.00
ORDER BY
	invoicedate
```

```
SELECT
	invoicedate
	billingaddress
	billingcity
	total
FROM
	invoice
WHERE
	billingcity LIKE 'P%' OR billingcity LIKE 'D%'
ORDER BY
	invoicedate
```

```
SELECT
	invoicedate
	billingaddress
	billingcity
	total
FROM
	invoice
WHERE
	total > 1.98 AND (billingcity LIKE 'P%' OR billingcity LIKE 'D%')
ORDER BY
	invoicedate
```


```
SELECT
	invoicedate,
	billingaddress,
	billingcity,
	total,
	CASE
	WHEN total < 2.00 THEN "Baseline purr"
	WHEN total BEETWEEN 2.00 AND 6.99 THEN "LOW purr"
	WHEN total BEETWEEN 7.00 AND 15.00 THEN "TARGET purr"
	ELSE "TOP purr"
	END AS PURR TUPE
FROM
	invoice
ORDER BY
	invoicedate
```

```
SELECT
	invoicedate
	billingaddress
	billingcity
	total
	CASE
	WHEN total < 2.00 THEN "Baseline purr"
	WHEN total BEETWEEN 2.00 AND 6.99 THEN "LOW purr"
	WHEN total BEETWEEN 7.00 AND 15.00 THEN "TARGET purr"
	ELSE "TOP purr"
	AND AS PURRTUPE
FROM
	invoice
WHERE
	PURRTUPE = "TOP purr"
ORDER BY
	invoicedate
```

```
SELECT
	c.lastname
	c.firstname
	i.invoiceid
	i.customerid
	i.invoicedate
	i.total
FROM
	invoice as i
INNER JOIN
	Customer as c
ON
	Invoice.CUstomerID = Customer.CustomerID
ORDER BY
	customer.customerid
```

```
SELECT
	firstname
	lastname
	firstname || ' ' || Lastname as FIO
	length(postalcode)
	substring(postalcode, 1, 5) as '5 dig postal code'
	upper(firstname)
	lower(lastname)

FROM
	Customer
Where
	country = 'USA'
```

```
SELECT
	firstname
	lastname
	birthdate
	strftime('%Y-%m-%d', birthdate)
	strftime('%Y-%m-%d', 'now') - strftime('%Y-%m-%d', birthdate) as age
FROM
	Employee
```

```
SELECT
	sum(total)
	avg(total)
	max(total)
	min(total)
	count(*) -- number of rows
FROM
	invoice
```

```
SELECT
	round(avg(total), 2)
FROM
	invoice
```


```
SELECT
	billingcity,
	round(avg(total), 2)
FROM
	invoice
WHERE
	bllingcity LIKE 'L%'
GROUP BY
	bllingcity
ORDER BY 
	bllingcity
```

```
SELECT
	billingcity,
	round(avg(total), 2)
FROM
	invoice
GROUP BY
	bllingcity
HAVING
	avg(total) > 5
ORDER BY 
	bllingcity
```

```
SELECT
	billingcity,
	round(avg(total), 2)
FROM
	invoice
WHERE
	bllingcity LIKE 'B%'
GROUP BY
	bllingcity
HAVING
	avg(total) > 5
ORDER BY 
	bllingcity
```

```
SELECT
	billingcountry
	billingcity,
	round(avg(total), 2)
FROM
	invoice
WHERE
	bllingcity LIKE 'B%'
GROUP BY
	bllingcity, billingcountry
HAVING
	avg(total) > 5
ORDER BY 
	billingcountry
```

```
SELECT
	invoicedate
	billingaddress
	billingcity,
	total
FROM
	invoice
WHERE
	total <
ORDER BY 
	total desc
```

```
SELECT
	billingcity,
	avg(total),
	(select avg(total) from invoice)
FROM
	invoice
GROUP BY
	billing city
ORDER BY 
	total desc
```

```
SELECT
	billingcity,
	billingaddress
	invoicedate
FROM
	invoice
where
	invoicedate >
	(select
	invoice date
	from
	invoice
	where invoiceid = 251)
```

```
SELECT
	billingcity,
	billingaddress
	invoicedate
FROM
	invoice
where
	invoicedate in
	(select
	invoice date
	from
	invoice
	where invoiceid in (251, 252, 254))
```

```
selec
	trackid
	composer
	name

from
	track
where
	trackid not in

(select
	distinct
	trackid
from
	invoiceline
order by trackid)
```


```
insert into
	artist(name)
values ('bob marley')
```

```
update
artist
set name = 'Damien marley'
where
	artistid = 276
```

```
delete from
	artist
where
	artistid = 276
```