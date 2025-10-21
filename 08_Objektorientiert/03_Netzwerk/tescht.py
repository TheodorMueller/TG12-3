from pydantic import BaseModel, Field, field_validator, ValidationError

spieler_liste = []


def Anzeige_Spieler():
    line = ""
    i = 0
    for i in int(len(spieler_liste)):
        for line in spieler_liste:
            line = (f"{line} <br> ")
    return line


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


spieler_liste.append(s)
s = Spieler(name="Franz")
spieler_liste.append(s)

for i in spieler_liste:
    print(i)

#print(spieler_liste)

