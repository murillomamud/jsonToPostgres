SELECT * FROM json_table WHERE data @> '{"company": "Semantix"}' AND
data @> '{"salary_low":8975}'; 

select *
from json_table
where data @@ '$.salary_low > 20000' and 
      data @@ '$.salary_low < 25000' 
      
select * from json_table 
where data->>'company' like '%Itau%'
and data @@ '$.salary_low > 20000'      