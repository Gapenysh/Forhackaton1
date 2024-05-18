from project.user_model_database import DataBase
from flask_jwt_extended import create_access_token
class RefactData:

    @staticmethod
    def refactor_data_to_json_from_name(name: str):
        data = DataBase.get_info_by_name(name)
        if data is not None and len(data) > 0:
            keys = ["id", "name", "video_URL"]
            res = dict(zip(keys, data))
            print(res)
            return res
        else:
            return 401