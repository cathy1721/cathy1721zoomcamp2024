if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print('Preprocessing: rows with zero passengers: ', data['passenger_count'].isin([0]).sum() )
    print('Preprocessing: rows with tripdisctance: ', data['trip_distance'].isin([0]).sum() )
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data.columns = (data.columns
                   .str.replace(' ', '_')
                   .str.lower()
                   )
    return data[(data['passenger_count'] > 0) | (data['trip_distance'] >0) ]

@test
def test_output(output, *args):
   assert output['passenger_count'].isin([0]).sum() > 0 , 'There are rides with zero passengers'

@test
def test_output1(output, *args):
   assert output['trip_distance'].isin([0]).sum() > 0 , 'There are trips with zero distance'


@test
def test_output3(output, *args):
   assert output['vendorid'].isin([1,2]).any() , 'There are trips with zero distance'

