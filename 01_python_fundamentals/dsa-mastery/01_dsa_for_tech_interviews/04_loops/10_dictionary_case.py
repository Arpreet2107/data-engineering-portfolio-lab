users = [
    {"id":1,"total":100,"coupon":"P20"},
    {"id":2,"total":150,"coupon":"P10"},
    {"id":3,"total":80,"coupon":"P5"}                           
]

discounts ={
    "P20": (0.2,0),
    "P10": (0.5,0),
    "P5": (0,10)
}

for user in users:
    percent,fixed = discounts.get(user["coupon"],(0,0))
    discount = user["total"]*percent + fixed
    print(f"User {user['id']} has a discount of {discount}")