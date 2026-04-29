class ArtifactError(Exception):
    def __init__(
        self,
        error_code: str,
        message: str,
        artifact_file: str | None = None,
        field: str | None = None,
        details: dict | None = None,
    ) -> None:
        self.error_code = error_code
        self.message = message
        self.artifact_file = artifact_file
        self.field = field
        self.details = details or {}
        super().__init__(message)


class ArtifactValidationError(ArtifactError):
    pass
