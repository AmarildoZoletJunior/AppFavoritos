class FavoriteDTO:
    def __init__(self, favorite_id, url, url_image, created_at, category, user, excerpts, tags):
        self.favorite_id = favorite_id
        self.url = url
        self.url_image = url_image
        self.created_at = created_at
        self.category = category
        self.user = user
        self.excerpts = excerpts
        self.tags = tags
        
    def to_dict(self):
        return {
            "category": self.category.to_dict() if self.category else None,
            "user": self.user.to_dict() if self.user else None,
            "excerpts": [excerpt.to_dict() for excerpt in self.excerpts],
            "tags": [tag.to_dict() for tag in self.tags],
            "favorite_id": self.favorite_id,
            "url": self.url,
            "url_image": self.url_image
        }


class CategoryDTO:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name
        
    def to_dict(self):
        return {
            "category_id": self.category_id,
            "category_name": self.category_name,
        }

class UserDTO:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
        }
class ExcerptDTO:
    def __init__(self, excerpt_id, excerpt_text, created_at):
        self.excerpt_id = excerpt_id
        self.excerpt_text = excerpt_text
        
    def to_dict(self):
        return {
            "excerpt_id": self.excerpt_id,
            "excerpt_text": self.excerpt_text
        }
        
class TagDTO:
    def __init__(self, tag_id, tag_name):
        self.tag_id = tag_id
        self.tag_name = tag_name
        
    def to_dict(self):
        return {
            "tag_id": self.tag_id,
            "tag_name": self.tag_name,
        }