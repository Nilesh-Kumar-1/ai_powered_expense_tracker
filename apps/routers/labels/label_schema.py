from pydantic import BaseModel

class LabelCreateRequest(BaseModel):
    label_name: str  # Name of the label
    # color: str       # Color associated with the label (e.g., hex code)
    description: str # Description of the label