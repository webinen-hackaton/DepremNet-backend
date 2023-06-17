from django.conf import settings
import jwt
from rest_framework import exceptions
import geopy.distance

def parse_jwt_id(token:str) -> int:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        return (payload["id"])
    except Exception:
        raise exceptions.AuthenticalstionFailed("Unauthorized")
    
def check_distance(point1, point2, radius):
    # R-2r < actual distance < R+2r
    # R: calculated distance between points
    # r: tolerance radius
    # res = actual distance
    # ( r . r ) < R > ( r . r )

    R = geopy.distance.geodesic(point1, point2).m
    r = 50 # meter 
    return R-2*r < radius and radius < R+2*r