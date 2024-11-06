from abc import ABC, abstractmethod

# Abstract class for user profile
class UserProfile(ABC):
    @abstractmethod
    def get_features(self):
        pass

    @abstractmethod
    def cost(self):
        pass

# Basic profile with core features
class BasicProfile(UserProfile):
    def get_features(self):
        return "Basic Profile Features: Text Posts, Comments, Likes"

    def cost(self):
        return 0  # Free basic profile

# Abstract decorator
class ProfileDecorator(UserProfile):
    def __init__(self, user_profile):
        self._user_profile = user_profile

    @abstractmethod
    def get_features(self):
        pass

# Decorator for adding photo sharing feature
class PhotoSharing(ProfileDecorator):
    def get_features(self):
        return self._user_profile.get_features() + ", Photo Sharing"

    def cost(self):
        return self._user_profile.cost() + 5  # Additional cost for photo sharing

# Decorator for adding story sharing feature
class StorySharing(ProfileDecorator):
    def get_features(self):
        return self._user_profile.get_features() + ", Story Sharing"

    def cost(self):
        return self._user_profile.cost() + 3  # Additional cost for story sharing

# Decorator for adding live streaming feature
class LiveStreaming(ProfileDecorator):
    def get_features(self):
        return self._user_profile.get_features() + ", Live Streaming"

    def cost(self):
        return self._user_profile.cost() + 10  # Additional cost for live streaming

if __name__ == "__main__":
    # Create a basic profile
    basic_profile = BasicProfile()
    print("{} - Cost: ${}".format(basic_profile.get_features(), basic_profile.cost()))

    # Add photo sharing feature
    photo_profile = PhotoSharing(basic_profile)
    print("{} - Cost: ${}".format(photo_profile.get_features(), photo_profile.cost()))

    # Add story sharing to the profile
    story_profile = StorySharing(photo_profile)
    print("{} - Cost: ${}".format(story_profile.get_features(), story_profile.cost()))

    # Full profile with all features
    full_profile = LiveStreaming(StorySharing(PhotoSharing(basic_profile)))
    print("{} - Cost: ${}".format(full_profile.get_features(), full_profile.cost()))
