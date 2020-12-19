from punctuator import Punctuator
from typing import Optional
from pathlib import Path


class PunctuatorModelProvider:
    """Able to provide a punctuator model."""

    def __init__(self):
        self._punctuator_model: Optional[Punctuator] = None

    def get_punctuator_model(self) -> Punctuator:
        """Returns a punctuator model. It will reuse the same punctuator model when
        calling this method multiple times, i.e. a singleton.

        Returns:
            Punctuator: the punctuator model
        """
        if self._punctuator_model is None:
            print("Loading punctuator model..")
            MODEL = str(Path("/app/chappy/punctuator/INTERSPEECH-T-BRNN.pcl").resolve())
            self._punctuator_model = Punctuator(MODEL)  # use pretrained model
            print("Completed loading punctuator model.")
        return self._punctuator_model
