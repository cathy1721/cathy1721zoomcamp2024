with 

source as (

    select * from {{ source('staging', 'fhv_tripdata') }}

),

renamed as (

    select 
      dispatching_base_num,
      pickup_datetime,
      dropOff_datetime,
      PUlocationID,
      DOlocationID,
      SR_Flag,
      Affiliated_base_number
    from
      source

)

select * from renamed

-- dbt build --select <model.sql> --vars '{'is_test_run: false}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}