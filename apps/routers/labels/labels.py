from fastapi import APIRouter, Depends, HTTPException
from apps.dependency.dependency import db_dependency
from apps.models import Label
from apps.routers.labels.label_schema import LabelCreateRequest
from apps.routers.auth.auth import user_dependency

router = APIRouter(prefix="/labels", tags=["Labels"])

@router.post("/create", response_model=dict)
def create_label( label_request: LabelCreateRequest, db: db_dependency, user: user_dependency ):
    # Check if label with the same name already exists
    existing_label = db.query(Label).filter(Label.label_name == label_request.label_name, Label.user_id == user.id).first()
    if existing_label:
        raise HTTPException(status_code=400, detail="Label with this name already exists.")

    new_label = Label(
        label_name=label_request.label_name,
        description=label_request.description,
        user_id= user.id  # Placeholder for user_id; replace with actual user identification logic
    )
    db.add(new_label)
    db.commit()
    db.refresh(new_label)
    return {"message": "Label created successfully", "label_id": new_label.id}

@router.get("/list", response_model=list)
def list_labels( db: db_dependency, user: user_dependency ):
    labels = db.query(Label).filter(Label.user_id == user.id).all()
    return labels

@router.delete("/delete/{label_id}", response_model=dict)
def delete_label( label_id: int, db: db_dependency, user: user_dependency ):
    label = db.query(Label).filter(Label.id == label_id, Label.user_id == user.id).first()
    if not label:
        raise HTTPException(status_code=404, detail="Label not found.")

    db.delete(label)
    db.commit()
    return {"message": "Label deleted successfully"}

@router.put("/update/{label_id}", response_model=dict)
def update_label( label_id: int, label_request: LabelCreateRequest, db: db_dependency, user: user_dependency ):
    label = db.query(Label).filter(Label.id == label_id, Label.user_id == user.id).first()
    if not label:
        raise HTTPException(status_code=404, detail="Label not found.")

    label.label_name = label_request.label_name # type: ignore
    label.description = label_request.description # type: ignore
    db.commit()
    db.refresh(label)
    return {"message": "Label updated successfully"}