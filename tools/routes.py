from enum import Enum
from config import settings

class AppRoute(str, Enum):
    LOGIN = f"{settings.app_url}/#/auth/login"
    REGISTRATION = f"{settings.app_url}/#/auth/registration"
    DASHBOARD = f"{settings.app_url}/#/dashboard"
    COURSES = f"{settings.app_url}/#/courses"
    COURSES_CREATE = f"{settings.app_url}/#/courses/create"

#class AppRoute(str, Enum):
    #LOGIN = "./#/auth/login"
    #REGISTRATION = "./#/auth/registration"
    #DASHBOARD = "./#/dashboard"
    #COURSES = "./#/courses"
    #COURSES_CREATE = "./#/courses/create"