select city.name from city
inner join countries ctr on
ctr.code = city.countrycode
where continent = 'Africa';