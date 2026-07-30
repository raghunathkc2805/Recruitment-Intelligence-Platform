from fastapi import APIRouter

from api.diagnostics.runtime_diagnostics import runtime_diagnostics
from api.diagnostics.self_healing import self_healing
from api.diagnostics.dependency_checker import dependency_checker

router = APIRouter(tags=["Diagnostics"])

@router.get("/diagnostics")

def diagnostics():

    return {

        "runtime":runtime_diagnostics.collect(),

        "dependencies":dependency_checker.check()

    }

@router.post("/diagnostics/self-heal")

def heal():

    return self_healing.execute()
