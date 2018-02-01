"""Profile picture components."""

from modules.element import Element, Component


class ProfilePicture(Component):
    """Definition of profile picture component."""

    add = Element(id_='profilePictureAddToggle')
    done = Element(id_='profilePictureDoneButton')
    default = Element(id_='profilePictureDefaultButton')
    default_image = Element(id_='profilePictureDefaultImageImg')
    image_link = Element(id_='profilePictureImageLinkButton')
    link = Element(id_='profilePictureLinkInput')
    gravatar = Element(id_='profilePictureGravatarButton')
    gravatar_email = Element(id_='profilePictureGravatarEmailInput')
