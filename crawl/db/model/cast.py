from crawl.db.model.schedule import Schedule


class Cast(Schedule):
    def __init__(self, schedule:Schedule , cast):
        super().__init__(schedule.musical_id, schedule.date, schedule.time)
        self.cast = cast
