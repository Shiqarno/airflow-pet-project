{{ config(
    materialized='table',
    contracts={"enforced": true}
) }}

SELECT
    id::integer AS id,
    date::timestamp AS date,
    amount::float AS amount,
    comment::text AS comment
FROM raw_transaction_data
