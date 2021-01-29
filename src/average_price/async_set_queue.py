import asyncio


class SetQueue(asyncio.Queue):
    '''
    asyncio.Queue with size of 0 or 1.
    '''
    def __init__(self):
        self._to_be_updated = False
        super().__init__()

    def put_nowait(self, item):
        if self._to_be_updated:
            return None
        self._to_be_updated = True
        return super().put_nowait(item)
    
    async def get(self):
        item = await super().get()
        self._to_be_updated = False
        return item
