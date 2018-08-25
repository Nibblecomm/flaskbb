class TopicService(ABC):
    """
    Used to manage the registration process. A default implementation is
    provided however, this interface is provided in case alternative
    flows are needed.
    """

    @abstractmethod
    def update(self, topic_info):
        """
        This method is abstract.

        :param topic_info: The provided user registration information.
        :type topic_info: :class:`~flaskbb.core.auth.registration.UserRegistrationInfo`
        """  # noqa
        pass
