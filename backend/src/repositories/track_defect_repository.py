from src.seed import seed
class TrackDefectRepository:
    def find_all(self):
        return seed["trackDefect"]
