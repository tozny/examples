import e3db

token = '9579d32bdd92ff16e10cc400fd555b057fe02160d2e8a7beea42e4fcf86b01d6'
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
client.share(record_type, 'b08ddc06-2b8b-4d0d-adb6-e0589610a05b')
