from sqlalchemy.orm import Session, joinedload
from sqlalchemy import desc

from models.Suggestion import Suggestion
from models.SuggestionCategory import SuggestionCategory


# 意見一覧取得
def getSuggestions(db: Session):
    return (
        db.query(Suggestion)
        .options(
            joinedload(Suggestion.suggestionCategory).joinedload(
                SuggestionCategory.category
            )
        )
        .order_by(desc(Suggestion.created_at))
        .all()
    )
