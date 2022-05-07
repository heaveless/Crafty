from playhouse.shortcuts import model_to_dict
from app.classes.web.base_api_handler import BaseApiHandler


class ApiRolesIndexHandler(BaseApiHandler):
    def get(self):
        auth_data = self.authenticate_user()
        if not auth_data:
            return
        (
            _,
            _,
            _,
            superuser,
            _,
        ) = auth_data

        # GET /api/v2/roles?ids=true
        get_only_ids = self.get_query_argument("ids", None) == "true"

        if not superuser:
            return self.finish_json(400, {"status": "error", "error": "NOT_AUTHORIZED"})

        # TODO: permissions
        self.finish_json(
            200,
            {
                "status": "ok",
                "data": self.controller.roles.get_all_role_ids()
                if get_only_ids
                else [model_to_dict(r) for r in self.controller.roles.get_all_roles()],
            },
        )
