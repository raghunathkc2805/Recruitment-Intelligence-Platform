from pydantic import BaseModel


class BulkRequest(BaseModel):

    jobs: list


class BulkResponse(BaseModel):

    processed: int

    failed: int

    results: list

    errors: list

