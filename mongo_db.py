from pymongo import MongoClient


import pprint



client=MongoClient()

db=client['stock-database']

gainers=db.gainers

loosers=db.loosers
loosers.drop()
gainers.drop()

arr_stocks=[
    {
    'Name': 'ITC',
    'Price':'123.4'
},
{
    'Name': 'ANSYS',
    'Price':'500.4'
},
{
    'Name': 'BURGER_KING',
    'Price':'143.4'
},{
    'Name': 'SBI',
    'Price':'323.4'
},{
    'Name': 'EROS',
    'Price':'13.4'
}
]

brr_stocks=[
    {
    'Name': 'COLGATE',
    'Price':'1033.4'
},
{
    'Name': 'RUCHI_SOYA',
    'Price':'100.4'
},
{
    'Name': 'AMERICAN_EXPRESS',
    'Price':'43.4'
},{
    'Name': 'TATAIQ',
    'Price':'323.4'
},{
    'Name': 'ZEE_MEDIA',
    'Price':'130.4'
}
]



results=gainers.insert_many(arr_stocks)


results=loosers.insert_many(brr_stocks)



# for obj_id in results.inserted_ids:
#     print("Stock Added "+str(obj_id))

# result=stocks.insert_one(stock)
# print(result)

# if result.acknowledged:
#     print("Stock Added "+str(result.inserted_id))


# tupple=gainers.find()
# for t in tupple:
#     pprint.pprint(t)