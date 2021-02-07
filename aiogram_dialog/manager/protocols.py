from typing import Optional, Any, Protocol, Union, Type

from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram_dialog.manager.intent import Intent, Data, DialogUpdateEvent


class ManagedDialogProto(Protocol):
    def register(self, registry: "DialogRegistryProto", dp: Dispatcher, *args, **kwargs):
        pass

    def states_group_name(self) -> str:
        pass

    def states_group(self) -> Type[StatesGroup]:
        pass

    async def start(self, manager: "DialogManagerProto", state: Optional[State] = None):
        pass

    async def show(self, manager: "DialogManagerProto"):
        pass

    async def process_result(self, result: Any, manager: "DialogManagerProto"):
        pass


class DialogRegistryProto(Protocol):
    def find_dialog(self, state: Union[State, str]) -> ManagedDialogProto:
        pass

    async def register_update_handler(self, callback, *custom_filters, run_task=None, **kwargs) -> None:
        pass

    async def notify(self, event: DialogUpdateEvent) -> None:
        pass


class DialogManagerProto(Protocol):

    def dialog(self) -> ManagedDialogProto:
        pass

    def current_intent(self) -> Intent:
        pass

    async def close(self):
        pass

    async def done(self, result: Any = None):
        pass

    async def start(self, state: State, data: Data = None, reset_stack: bool = False):
        pass

    async def switch_to(self, state):
        pass
