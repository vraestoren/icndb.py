from requests import Session

class IcnDb:
    def __init__(self) -> None:
        self.api = "https://api.icndb.com"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        }

    def _get(self, endpoint: str, params: dict = None) -> dict:
        return self.session.get(
            f"{self.api}{endpoint}", params=params, verify=False).json()

    def _filter(self, data: dict) -> dict:
        return {key: value for key, value in data.items() if value is not None}

    def get_random_joke(
            self,
            count: int = 1,
            first_name: str = None,
            last_name: str = None,
            limit_to: str = "nerdy",
            exclude: str = None) -> dict:
        params = self._filter({
            "firstName": first_name,
            "lastName": last_name,
            "exclude": exclude
        })
        return self._get(f"/jokes/random/{count}?limitTo=[{limit_to}]", params)

    def get_specific_joke(self, joke_id: int) -> dict:
        return self._get(f"/jokes/{joke_id}")

    def get_jokes_count(self) -> dict:
        return self._get("/jokes/count")

    def get_joke_categories(self) -> dict:
        return self._get("/categories")
