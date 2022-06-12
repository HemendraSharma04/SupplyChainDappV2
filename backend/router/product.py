from fastapi import APIRouter, Depends
from contract import *
from pydantic import BaseModel


class Unit(BaseModel):
    GLN  : str 
    GTIN : str
    GSIN : str
    SSCC : str
    SN   : str
    name : str
    data : str
    w_id : int
   
  
router = APIRouter(
    prefix='/unit',
    tags=['unit']
)


@router.get('/')
def index(id:int):
    return get_unit(id)

@router.post('/')
def index(unit: Unit):
    return addUnitInfo(unit.GLN, unit.GTIN, unit.GSIN,unit.SSCC,unit.name,unit.data,unit.w_id)

@router.post('/historyall')
def index():
    return historyAll()

@router.get("/history/{gtin}/{sn}")
def index(gtin:str,sn:str):
    return history(gtin,sn)
