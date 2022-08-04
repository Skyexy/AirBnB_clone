from models.base_model import BaseModel


class Review(BaseModel):
    text = ""
    place_id = ""
    user_id = ""

    def __init__(self, *arg, **kwargs):
        super(Review, self).__init__(**kwargs)
