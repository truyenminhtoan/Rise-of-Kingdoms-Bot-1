import traceback

from filepath.file_relative_paths import ImagePathAndProps
from tasks.constants import BuildingNames
from tasks.constants import TaskName
from tasks.Task import Task
import time

class Title(Task):
    def __init__(self, bot):
        super().__init__(bot)

    def do(self, next_task=TaskName.COLLECTING):
        super().set_text(title='Title-bot', remove=True)
        super().set_text(insert='Init view')
       
        ref = super().getdb()

        titles = ref.order_by_child("time").limit_to_first(1).get()

        if titles is not None:
            for key, value in titles.items():
                if(value["name"] and value["x"] and value["y"]):
                    print("Name: {}", value["name"])
                    print("X: {}", value["x"])
                    print("Y: {}", value["y"])
                    ref.child(key).set({})

                    super().back_to_home_gui()
                    super().back_to_map_gui()


                    super().tap(316, 20, 1)
                    super().tap(636, 140, 1)
                    super().input(value["x"])
                    super().tap(1174, 650, 1)
                    super().tap(794, 140, 1)
                    super().input(value["y"])
                    super().tap(1174, 650, 1)
                    super().tap(882, 140, 1)
                    

                    # 666 330 City
                    super().tap(666, 330, 2)

                    #164 158 Icon tuoc
                    # super().tap(164, 158, 2)
                    _, _, tavern_btn_pos = self.gui.check_any(ImagePathAndProps.TITLE_ICON_IMAGE_PATH.value)
                    if tavern_btn_pos is None:
                        return next_task
                    x, y = tavern_btn_pos
                    super().tap(x, y, 2)

                    # 288 394 Jus
                    if(value["name"] == "jus"):
                        super().tap(288, 394, 2)
                    # 516 394 Duke
                    if(value["name"] == "duke"):
                        super().tap(516, 394, 2)

                    # 746 394 Arch
                    if(value["name"] == "arch"):
                        super().tap(746, 394, 2)

                    # 974 394 Sci
                    if(value["name"] == "sci"):
                        super().tap(974, 394, 2)

                    # 640 634 Confirm
                    super().tap(640, 634, 2)

        time.sleep(30)
        return next_task
