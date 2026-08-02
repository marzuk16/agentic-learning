class EmptyDocumentError(Exception):
    """A document was loaded successfully but produced nothing to index.

    Typically a scanned / image-only PDF: the file parses fine and yields
    metadata, but no page carries a text layer, so chunking returns nothing.
    Without this the ingest would commit a document row with zero chunks and
    report success, leaving the document permanently unsearchable.
    """

    def __init__(
        self,
        source: str,
    ):
        self.source = source

        super().__init__(
            f"No extractable text found in '{source}'. "
            "The document appears to be scanned or image-only."
        )
