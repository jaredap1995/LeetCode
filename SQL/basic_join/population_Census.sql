select sum(city.population) from city
inner join countries ctr on
ctr.code = city.countrycode
where ctr.continent = 'Asia';