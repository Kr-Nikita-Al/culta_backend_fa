from enum import Enum


class PortalRole(str, Enum):
    ROLE_PORTAL_USER = 'ROLE_PORTAL_USER'
    ROLE_PORTAL_STAFF = 'ROLE_PORTAL_STAFF'
    ROLE_PORTAL_ADMIN = 'ROLE_PORTAL_ADMIN'
    ROLE_PORTAL_SUPER_ADMIN = 'ROLE_PORTAL_SUPER_ADMIN'
