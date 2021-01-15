import e3db
from e3db.types import Search

# For this example, instantiate a third party client
third_party_config = e3db.Config(
    'b08ddc06-2b8b-4d0d-adb6-e0589610a05b',
    'dc206e9717e7ad5387c629553bf10db3055ed793376def7112ffa1624ec26f93',
    '7b2f1467d1d79d078696d69e7d8082337d60a4aee13b55499f8fd9b9412ecf60',
    'raT3LeDulPGJSddxY1GkvvZthoTZqsGmvS1AFszzJhs',
    'GPcrmq3k9vfEaKPd1sRQubfZ2umWbWF0iB2buUSQVEw',
    api_url = "https://api.e3db.com"
)

third_party_client = e3db.Client(third_party_config())

# Obtain records written by client from the third_party client
record_type = 'contact'
search_filter = Search(include_all_writers=True,include_data=True) \
                                .match(condition="AND", record_types=['contact'], writers=['2bdf5340-08da-43b3-8838-e2c6c7c44c71'])
results = third_party_client.search(search_filter)
for record in results:
    print(record.to_json())
