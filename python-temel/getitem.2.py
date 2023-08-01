class Sample:
    def __init__(self):
        self.dict = {}

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __getitem__(self, key):
        return self.dict[key]

s = Sample()
s['ali'] = 300
s['veli'] = 200
s[100] = 'kazım'

print(s['ali'])
print(s['veli'])
print(s[100])
