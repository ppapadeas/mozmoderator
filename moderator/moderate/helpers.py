from jingo import register

from utils import is_admin


@register.function
def user_voted(question, user):
    """Check if a user has already voted."""
    return question.votes.filter(user=user).exists()


@register.function
def user_is_admin(user):
    """Check is a user is in Admin group"""
    return is_admin(user)
