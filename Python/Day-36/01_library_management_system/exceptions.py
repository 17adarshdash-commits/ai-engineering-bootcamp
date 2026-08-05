class LibraryError(Exception):
    pass


class DuplicateBookIDError(LibraryError):
    pass


class BookNotFoundError(LibraryError):
    pass


class BookUnavailableError(LibraryError):
    pass


class BookAlreadyAvailableError(LibraryError):
    pass
