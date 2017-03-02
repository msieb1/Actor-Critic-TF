import tensorflow as tf


class BaseModel:
    """The base class for the actor and critic estimators"""

    def build_shared_model(self):
        pass


class Actor(BaseModel):
    """The actor class"""

    def __init__(self, sess, config):
        self._sess = sess

    def predict(self):
        pass

    def update(self):
        pass


class Critic(BaseModel):
    """The critic class"""

    def __init__(self, sess, config):
        self._sess = sess

    def predict(self):
        pass

    def update(self):
        pass
