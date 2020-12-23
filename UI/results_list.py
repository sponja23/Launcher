from PyQt5.QtCore import Qt, QStringListModel, QSize
from PyQt5.QtWidgets import QListView, QAbstractItemView, QFrame
from typing import Any, Iterable, Mapping, List
from backend.settings import settings


class ResultsList(QListView):
    def __init__(self: "ResultsList", *args: Iterable[Any], **kwargs: Mapping[str, Any]) -> None:
        super().__init__(*args, **kwargs)

        self.setFrameShape(QFrame.NoFrame)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setUniformItemSizes(True)
        self.listModel = QStringListModel()

        self.setModel(self.listModel)
        self.listModel.setStringList(["PLACEHOLDER"] * 100)

    def sizeHint(self: "ResultsList") -> QSize:
        return QSize(self.width(), self.sizeHintForRow(0) * min(len(self.listModel.stringList()),
                                                                settings["max_list_items"]))

    def minimumSizeHint(self: "ResultsList") -> QSize:
        return QSize(0, 0)

    def setList(self: "ResultsList", lst: List[str]) -> None:
        self.listModel.setStringList(lst)
        self.updateGeometries()
