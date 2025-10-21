from pydantic import BaseModel, Field, field_validator, ValidationError

class Spieler(BaseModel):
    name: str = Field(default="Unbekannt")
    jahrgang: int = Field(default=2000, ge=1975, le=2007)
    staerke: int = Field(default=0, ge=1, le=10)
    torschuss: int = Field(default=0, ge=1, le=10)
    motivation: int = Field(default=0, ge=1, le=10)
    
    model_config = {"validate_assignment":True}

s = Spieler()
print(s)
print(s.model_dump())