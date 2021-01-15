import e3db

token = 'XXXXYourToznyClientRegistrationTokenHereXXXXX'
client_name = 'Sally'

public_key, private_key = e3db.Client.generate_keypair()

client_info = e3db.Client.register(token, client_name, public_key)

# For this example, instantiate a client
config = e3db.Config(
    client_info.client_id,
    client_info.api_key_id,
    client_info.api_secret,
    public_key,
    private_key,
    api_url = "https://api.e3db.com"
)

# Instantiate your client to communicate with TozStore
client = e3db.Client(config())

#Create a record
record_type = 'contact'
data = {
    'first_name': 'Harry',
    'last_name': 'Sally',
    'phone': '555-555-1212'
}

metadata = { 'house' : 'New York'
 }

#write the record to TozStore
record = client.write(record_type, data, metadata)
print(record)

#grant share operation
record_type = 'contact'
client.share(record_type, 'tozny-client-id-of-the-third-party-you-want-share-with')
