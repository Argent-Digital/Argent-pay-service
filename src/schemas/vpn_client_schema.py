from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DeleteKeys(BaseModel):
    user_id: int
    server_key_if: str | None
    protocol: str
    vless_uuid: UUID | None

    model_config=ConfigDict(from_attributes=True)
