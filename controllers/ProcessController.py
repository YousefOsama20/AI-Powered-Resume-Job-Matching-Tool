from .BaseController import BaseController
from .ProjectController import ProjectController
from .loaderController import load_pdf, load_docx

from langchain_text_splitters import RecursiveCharacterTextSplitter

import os

from models.enums import ProcessingEnum


class ProcessController(BaseController):

    def __init__(self, project_id: str):
        super().__init__()

        self.project_id = project_id

        self.project_path = ProjectController().get_project_path(project_id=project_id)

    def get_file_extension(self, file_id: str):

        return os.path.splitext(file_id)[-1].lower()

    def get_file_loader(self, file_id: str):

        file_ext = self.get_file_extension(file_id=file_id)

        file_path = os.path.join(self.project_path, file_id)

        if file_ext == ProcessingEnum.PDF.value:
            return load_pdf(file_path)

        if file_ext == ProcessingEnum.DOCX.value:
            return load_docx(file_path)

        return []

    def get_file_content(self, file_id: str):

        return self.get_file_loader(file_id=file_id)

    def process_file_content(self, file_content: list, file_id: str,
                                 chunk_size: int = 500, overlap_size: int = 50):

        pass

