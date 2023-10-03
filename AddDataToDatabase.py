import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-3551e-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "11":
        {
            "name": "Thắng đẹp trai",
            "major": "Computer science",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "T",
            "year": 4,
            "last_attendance_time": "2023-09-11 00:12:30"
        },
    "852741":
        {
            "name": "Bạn xinh",
            "major": "economics",
            "starting_year": 2019,
            "total_attendance": 1,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2023-06-11 00:12:30"
        },
    "963852":
        {
            "name": "Elon musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 2,
            "standing": "T",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:12:30"
        }
}

for key, value in data.items():
    ref.child(key).set(value)