import e3db
from e3db.types import Search

# For this example, instantiate a third party client
third_party_config = e3db.Config(
    'a08ddc06-fake-fake-fake-e0589610a05b',
    'fake6e9717e7ad5387c629553bf10db3055ed793376def7112ffa1624ec2fake',
    'fake1467d1d79d078696d69e7d8082337d60a4aee13b55499f8fd9b9412efake',
    'fakeLeDulPGJSddxY1GkvvZthoTZqsGmvS1AFszfake',
    'fakemq3k9vfEaKPd1sRQubfZ2umWbWF0iB2buUSfake',
    api_url = "https://api.e3db.com"
)

third_party_client = e3db.Client(third_party_config())

# Obtain records written by client from the third_party client
record_type = 'contact'
search_filter = Search(include_all_writers=True,include_data=True) \
                                .match(condition="AND", record_types=['contact'], writers=['tozny-client-id-that-shared-with-you'])
results = third_party_client.search(search_filter)
for record in results:
    print(record.to_json())
