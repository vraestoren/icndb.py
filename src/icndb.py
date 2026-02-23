from requests import Session

class ICNDB:
    def __init__(self) -> None:
        self.api = "https://api.icndb.com"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        }

    def get_random_joke(
            self,
            count: int = 1,
            first_name: str = None,
            last_name: str = None,
            limit_to: str = "nerdy",
            exclude: str = None) -> dict:
        params = {
            "firstName": first_name,
            "lastName": last_name,
            "exclude": exclude
        }
        filtered_params = {
            key: value for key, value in params.items() if value is not None
        }
        return self.session.get(
            f"{self.api}/jokes/random/{count}?limitTo=[{limit_to}]",
            params=filtered_params,
            verify=False).json()

    def get_specific_joke(self, joke_id: int) -> dict:
        return self.session.get(
            f"{self.api}/jokes/{joke_id}", verify=False).json()

    def get_jokes_count(self) -> dict:
        return self.session.get(
            f"{self.api}/jokes/count", verify=False).json()

    def get_joke_categories(self) -> dict:
        return self.session.get(
            f"{self.api}/categories", verify=False).json()

    def get_all_jokes(self) -> dict:
        return self.session.get(self.api, verify=False).json()
