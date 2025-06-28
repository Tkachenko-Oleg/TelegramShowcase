from app.config import Config


def is_admin(usr_id: int) -> bool:
    return str(usr_id) in Config.ADMIN_IDS
