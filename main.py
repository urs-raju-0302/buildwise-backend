from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Project(BaseModel):
    area: int
    floors: int
    location: str
    budget: float

@app.get("/")
def home():
    return {"message": "BuildWise Backend Running"}

@app.post("/generate-plan")
def generate_plan(project: Project):

    material_cost = project.area * 1800
    labor_cost = project.floors * 60000
    contingency = 0.1 * (material_cost + labor_cost)

    total_cost = material_cost + labor_cost + contingency

    return {
        "total_cost": total_cost,
        "material_cost": material_cost,
        "labor_cost": labor_cost,
        "contingency": contingency
    }
