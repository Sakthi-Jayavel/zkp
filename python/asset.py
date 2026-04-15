class Asset:
    def __init__(self, asset_id, asset_type, owner, value, location):
        self.asset_id = asset_id
        self.asset_type = asset_type
        self.owner = owner
        self.value = value
        self.location = location
        self.state = "UNREGISTERED"
        self.is_tokenized = False