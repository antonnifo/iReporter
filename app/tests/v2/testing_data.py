from werkzeug.security import generate_password_hash

password = generate_password_hash("hello123")
test_user = {
        "first_name": "john",
        "last_name": "doe",
        "email": "johndoe@example.com",
        "phone": "0707741793",
        "isAdmin": True,
        "registered": "Thu, 13 Dec 2018 21:00:00 GMT",
        "password": password
}

user = {
    "first_name" : "John",
    "last_name" : "Doe",
    "email" : "john@doe.com",
    "phone" :"0727426274",   
    "password" : "hello123",
    "isAdmin" : False
}

user2 = {
    "first_name" : "John",
    "last_name" : "Doe",
    "email" : "john@doe.com",
    "phone" : "0727426274",
    "password" : "hello123",
    "isAdmin" : False
}

user3 = {
    "first_name" : "anthony",
    "last_name" : "mwas",
    "email" : "anthony@mwas.com",
    "phone" : "0727426274",
    "password" : "hello123",
    "isAdmin" : False
}

user4 = {
    "first_name" : "anthony",
    "last_name" : "mwas",
    "email" : "anthony@mwas.com",
    "phoneNumber" : "0727426274",
    "password" : "hello123",
    "isAdmin" : True

}

data5 = {
    "email" : "john@doe.com",
    "password" : "hello123"
}

data6 = {
    "email" : "john@doe.com",
    "password" : "hello1234"
}

data7 = {
    "email" : "john123@doe.com",
    "password" : "hello123"
}

redflag_data = {
    "createdOn": "Tue, 27 Nov 2018 21:18:13 GMT",
    "createdBy": 1,
    "type": "redflag",
    "location": "-90.000, -180.0000",
    "status": "draft",
    "images": "",
    "title": "Mercury in sugar",
    "comment": "Lorem ipsum dolor sit amet."
}
redflag_data2 = {
    "createdOn": "Tue, 27 Nov 2018 21:18:13 GMT",
    "createdByfhh": 2,
    "type": "redflag",
    "location": "-90, -180",
    "status": "draft",
    "images": "", 
    "title": "Mercury in sugar",
    "comment": "Lorem ipsum dolor sit amet."
}
redflag_data3 = {
    "createdOn": "Tue, 27 Nov 2018 21:18:13 GMT",
    "type": "redflag",
    "location": "-90, -180",
    "status": "draft",
    "images": "",
    "comment": "Lorem ipsum dolor sit amet."
}
intervention_data = {
            "createdBy": 1,
            "type": "intervention",
            "location": "66, 12",
            "status": "draft",
            "title": "NYS scandal",
            "comment": "act soon",
            "createdon": "Thu, 13 Dec 2018 14:31:20 GMT"
        }