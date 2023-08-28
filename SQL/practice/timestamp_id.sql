--Given a hypothetical table named wearables and two columns (device_id, timestamp)
--Write a query that returns the most recent timestamp for each device

--Window approach
with RankedEntries as (
    SELECT *, ROW_NUMBER() OVER(PARTITION BY device_id ORDER BY timestamp desc) as rn
    from wearables
)

select*from ranked_entries where rn = 1;