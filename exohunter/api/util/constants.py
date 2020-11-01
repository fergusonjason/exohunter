import datetime

missions = ("TESS","Kepler","K2",)

kepler_quarters = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)

k2_campaigns = ("C0", "C1", "C2", "C3", "C4", "C5","C6","C7","C8","C9a","C9b","C10","C11","C12","C13","C14","C15","C16","C17","C18","C19")

VIZIER_CATALOGS = {
    "TESS": "IV/38",
    "Kepler": "V/133",
    "K2": None
}

{
    "descriptor":"",
    "data":[
        {
            "text":"",
            "start":None,
            "stop":None
        }
    ]
}

# kepler_quarters = {
#     "descriptor":"quarter",
#     "data":[
#         {
#             "text":"1",
#             "start":None,
#             "stop":None
#         }
#     ]
# }

# k2_campaigns = {
#     "descriptor":"campaign",
#     "data":[
#         {
#             "text":"",
#             "start":None,
#             "stop":None
#         }
#     ]
# }

# tess_campaigns = {1:datetime.date(2018,7,25),
#     2:datetime.date(2018,8, 22),
#     3:datetime.date(2018,9.20),
#     4:datetime.date(2018,10,18),
#     5:datetime.date(2018,11,15),
#     6:datetime.date(2018,12,11),
#     7:datetime.date(2019,1,7),
#     8:datetime.date(2019,2,2),
#     9:datetime.date(2019,3,26),
#     10:datetime.date(2019,4,22)}