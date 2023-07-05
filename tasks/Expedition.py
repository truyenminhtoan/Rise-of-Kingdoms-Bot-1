from filepath.file_relative_paths import ImagePathAndProps
from tasks.Task import Task
import traceback

from tasks.constants import TaskName


class Expedition(Task):
    def __init__(self, bot):
        super().__init__(bot)

    def do(self, next_task=TaskName.MYSTERY_MERCHANT.value):
        self.set_text(title='Expedition')
        campaign_btn_pos = (830, 670)
        self.back_to_home_gui()
        self.menu_should_open(True)
        x, y = campaign_btn_pos
        self.tap(x, y, 1)

        found, _, pos = self.gui.check_any(ImagePathAndProps.EXPEDITION_IMAGE_PATH.value)
        if not found:
            self.set_text(insert='Expedition not found', index=0)
            return next_task

        self.set_text(insert='Open Expedition')
        x, y = pos
        self.tap(x, y, 1)


