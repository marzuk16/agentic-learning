from sqlalchemy.orm import Session

from src.db.models.document import Document


class DocumentRepository:

    def __init__(
        self,
        session: Session,
    ):
        self.session = session


    def create(
        self,
        document: Document,
    ) -> Document:

        self.session.add(document)

        self.session.flush()

        return document