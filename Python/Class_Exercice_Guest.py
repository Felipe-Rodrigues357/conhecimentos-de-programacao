class Guest:
    # dict = {"John": "A011", "Kyle": "A009", "Jake": "BQ02", "Tamra": "A015", "Josh": "BQ03"}
    dict = {"John": "A011",
            "Kyle": "A009",
            "Jake": "BQ02",
            "Tamra": "A015",
            "Josh": "BQ03"}
    kys = ['A010', 'A012', 'A014', 'BQ01']

    def __init__(self, name):
        self.name = str(name.lower()).capitalize()
        self.regd = self.name in self.dict
        # self.dict = {"John": "A011", "Kyle": "A009", "Jake": "BQ02", "Tamra": "A015", "Josh": "BQ03"}
        # self.kys = ['A0010', 'A012', 'A014', 'BQ01']

    def is_regd(self):
        if self.regd:
            print('Registered')
        else:
            print('Not Registered')

    # if self.Name in self.dict:
    #     print('Registered')
    # else:
    #     print('Not registered')
    def get_key(self):
        if self.regd:
            print(f'Key : {self.dict[self.name]}')
        #else:
          #  print('Not registered')
    def reg(self):
        if len(self.kys) < 1:
            print('Sorry, no vacant rooms available')
        else:
            self.dict[self.name] = self.kys[0]
            self.kys.pop(0)
            self.regd = True

for guest_name in ['Josh', 'Hans', 'Evan', 'Kyle', 'Ted', 'Karl', 'Sam']:
    gst = Guest(guest_name)
    print(gst.name)
    gst.is_regd()
    if gst.regd:
        gst.get_key()
    else:
        gst.reg()
        gst.get_key()