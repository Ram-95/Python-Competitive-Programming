import random
class Codec:
    def __init__(self):
        self.d = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # Generates a Random string of length 6
        name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
        self.d[name] = longUrl
        
        return name
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.d[shortUrl]
